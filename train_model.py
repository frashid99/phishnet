import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Load and preprocess data
df = pd.read_csv('data/phishing_emails.csv')

# Rename columns for simplicity
df = df.rename(columns={'Email Text': 'text', 'Email Type': 'label'})

# Remove extremely short ones
df = df[df['text'].str.len() > 50]

# Clean data
df = df.dropna(subset=['text'])
df = df[df['text'].apply(lambda x: isinstance(x, str) and x.strip() != '')]

# Map labels to 0/1
df['label'] = df['label'].map({'Safe Email': 0, 'Phishing Email': 1})

X = df['text']
y = df['label']

# Define ML pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=10000, ngram_range=(1, 2))),
    ('clf', MultinomialNB())
])

# Train and save model
pipeline.fit(X, y)
joblib.dump(pipeline, 'models/phishing_model.pkl')

print("Model trained and saved to models/phishing_model.pkl")
print("Final dataset shape:", df.shape)

