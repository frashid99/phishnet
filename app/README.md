# PhishNet 
**AI-Powered Email Phishing Detector**

PhishNet is a lightweight Flask web app that uses machine learning and natural language processing to detect whether an email is a phishing attempt or a legitimate message.

---

# Features

- Classifies emails as **Phishing** or **Legitimate**
- Displays prediction **confidence percentage**
- Built using **TF-IDF + Multinomial Naive Bayes**
- Trained on 17,000+ real phishing and safe emails
- Clean web UI for pasting and analyzing email text

---

# Tech Stack

- Python
- Flask
- scikit-learn
- Pandas
- HTML/CSS
- Jinja2

---

# Project Structure

phishnet/
├── app/
│ ├── model.py
│ ├── routes.py
│ ├── templates/
│ │ └── index.html
│ └── static/
│ └── style.css
├── models/
│ └── phishing_model.pkl
├── data/
│ └── phishing_emails.csv
├── train_model.py
├── run.py
├── requirements.txt
└── README.md

---

# How to Run Locally

1. Clone the repo
git clone https://github.com/frashid99/phishnet.git
cd phishnet

2. Install dependencies
pip install -r requirements.txt

3. Train the model (optional if model is already provided)
python train_model.py

4. Run the web app
python run.py

5. Open in browser:
http://localhost:5000

# Dataset

Used a labeled dataset of phishing and safe emails from public sources (e.g., Enron, Ling-Spam). The model is trained using TF-IDF vectorization with bigrams and a Naive Bayes classifier.

    Columns: Email Text, Email Type

    Classes: "Phishing Email" (1), "Safe Email" (0)

# Future Improvements

    Add sender/domain reputation scoring

    Use transformer models like BERT for better context understanding

    Visualize attention weights or explain predictions

    Deploy on Streamlit or Hugging Face Spaces