from flask import Flask, render_template, request
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download vader_lexicon once
nltk.download('vader_lexicon')

app = Flask(__name__)

# Initialize VADER sentiment analyzer
vader = SentimentIntensityAnalyzer()

@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    user_input = ""
    details = {}

    if request.method == "POST":
        user_input = request.form.get("sentence", "")

        if user_input.strip():
            # TextBlob analysis
            blob = TextBlob(user_input)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            # Vader analysis
            vader_scores = vader.polarity_scores(user_input)

            # Decide sentiment based on vader compound score (more precise)
            compound = vader_scores["compound"]
            if compound >= 0.05:
                sentiment = "😊 Positive"
            elif compound <= -0.05:
                sentiment = "😞 Negative"
            else:
                sentiment = "😐 Neutral"

            # Provide extra details
            details = {
                "TextBlob Polarity": round(polarity, 2),
                "TextBlob Subjectivity": round(subjectivity, 2),
                "VADER Scores": vader_scores
            }

    return render_template("index.html", sentiment=sentiment, user_input=user_input, details=details)

if __name__ == "__main__":
    app.run(debug=True)
