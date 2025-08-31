```markdown
 🕹 Retro Sentiment Analyzer

A retro-style web app that analyzes the sentiment of text (Positive, Negative, Neutral) using TextBlob and NLTK’s VADER Sentiment Analyzer.

---

 🚀 Features
- 🎨 Beautiful retro terminal-style UI
- ✍️ Input any sentence or review
- 🧠 TextBlob → Polarity & Subjectivity
- 📊 VADER → Detailed sentiment scores
- ✅ Outputs: Positive / Negative / Neutral with emoji

---

 📂 Project Structure
```

sentiment-analysis-project/
│
├── app.py                # Main Flask app
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
│
├── templates/            # HTML templates
│   └── index.html        # Retro-styled frontend
│
└── static/               # Optional CSS/JS/images
└── style.css         # If you separate CSS

````

---

 ⚡ Installation & Usage

 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/sentiment-analysis-project.git
cd sentiment-analysis-project
````

 2️⃣ Create virtual environment (optional but recommended)

```bash
python -m venv venv
# Activate it:
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
python -m textblob.download_corpora
python -c "import nltk; nltk.download('vader_lexicon')"
```

 4️⃣ Run the app

```bash
python app.py
```

 5️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

 🎯 Example

Input:

```
I love this project, it looks amazing!
```

Output:

```
😊 Positive
```

Extra details:

* TextBlob Polarity: `0.5`
* TextBlob Subjectivity: `0.6`
* VADER Scores: `{ 'neg': 0.0, 'neu': 0.45, 'pos': 0.55, 'compound': 0.73 }`

---

 🛠️ Technologies Used

* Python
* Flask
* TextBlob
* NLTK (VADER Sentiment Analyzer)

---

 📜 License

This project is open-source. Feel free to use and modify.

```

---
```
