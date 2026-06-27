import pandas as pd
import re
import nltk
import joblib
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    words = [stemmer.stem(w) for w in words if w not in stop_words]
    return ' '.join(words)

# Load data
fake = pd.read_csv('data/raw/Fake.csv')
true = pd.read_csv('data/raw/True.csv')
fake['label'] = 0
true['label'] = 1
df = pd.concat([fake, true], ignore_index=True)

# Preprocess
df['clean_text'] = df['text'].apply(preprocess_text)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    df['clean_text'], df['label'], test_size=0.2, random_state=42)

# TF-IDF
tfidf = TfidfVectorizer(max_features=5000)
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Train
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# Evaluate
accuracy = accuracy_score(y_test, model.predict(X_test_tfidf))
print(f"Accuracy: {accuracy * 100:.2f}%")

# Save
joblib.dump(model, 'models/fake_news_model.pkl')
joblib.dump(tfidf, 'models/vectorizer.pkl')
print("Model saved!")