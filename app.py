from flask import Flask, render_template, request
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

app = Flask(__name__)

# Load model
model = joblib.load('models/fake_news_model.pkl')
tfidf = joblib.load('models/vectorizer.pkl')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    words = [stemmer.stem(w) for w in words if w not in stop_words]
    return ' '.join(words)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    news_text = request.form['news_text']
    
    # Preprocess
    clean = preprocess_text(news_text)
    vector = tfidf.transform([clean])
    
    # Predict
    prediction = model.predict(vector)[0]
    confidence = model.predict_proba(vector)[0]
    
    if prediction == 0:
        result = 'FAKE NEWS'
        confidence_score = f"{confidence[0]*100:.2f}%"
        color = 'danger'
        emoji = '🚨'
    else:
        result = 'REAL NEWS'
        confidence_score = f"{confidence[1]*100:.2f}%"
        color = 'success'
        emoji = '✅'
    
    return render_template('result.html',
                         news_text=news_text,
                         result=result,
                         confidence=confidence_score,
                         color=color,
                         emoji=emoji)

if __name__ == '__main__':
    import webbrowser
    webbrowser.open('http://localhost:5000')
    app.run(debug=True)
    