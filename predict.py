import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Load model
model = joblib.load('models/fake_news_model.pkl')
tfidf = joblib.load('models/vectorizer.pkl')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    words = [stemmer.stem(w) for w in words if w not in stop_words]
    return ' '.join(words)

def predict_news(news_text):
    # Preprocess
    clean = preprocess_text(news_text)
    # Vectorize
    vector = tfidf.transform([clean])
    # Predict
    prediction = model.predict(vector)[0]
    confidence = model.predict_proba(vector)[0]
    
    if prediction == 0:
        return {
            'result': 'FAKE NEWS',
            'confidence': f"{confidence[0]*100:.2f}%",
            'emoji': '🚨'
        }
    else:
        return {
            'result': 'REAL NEWS',
            'confidence': f"{confidence[1]*100:.2f}%",
            'emoji': '✅'
        }

# Test
if __name__ == '__main__':
    test = "Donald Trump says vaccines cause autism"
    result = predict_news(test)
    print(f"Result: {result['emoji']} {result['result']}")
    print(f"Confidence: {result['confidence']}")