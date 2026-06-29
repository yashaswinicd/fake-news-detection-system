from flask import Flask, render_template, request, jsonify
import joblib
import re
import nltk
import logging
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

# ── Logging Setup ──────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

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

# ── Home ───────────────────────────────────────────────────
@app.route('/')
def home():
    return render_template('index.html')

# ── Main Predict (Form) ────────────────────────────────────
@app.route('/predict', methods=['POST'])
def predict():
    news_text = request.form.get('news_text', '').strip()

    # Handle empty input
    if not news_text:
        logger.warning("Empty input received")
        return render_template('index.html',
                               error="⚠️ Please enter some news text!")

    # Handle very long text
    if len(news_text) > 10000:
        logger.warning(f"Long input truncated: {len(news_text)} chars")
        news_text = news_text[:10000]

    logger.info(f"Prediction requested | Length: {len(news_text)} chars")

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

    logger.info(f"Result: {result} | Confidence: {confidence_score}")

    return render_template('result.html',
                           news_text=news_text,
                           result=result,
                           confidence=confidence_score,
                           color=color,
                           emoji=emoji)

# ── REST API Endpoint ──────────────────────────────────────
@app.route('/api/predict', methods=['POST'])
def api_predict():
    """
    REST API endpoint
    Request  → JSON: {"text": "your news here"}
    Response → JSON: {"result": "FAKE NEWS", "confidence": "93.27%", "emoji": "🚨"}
    """
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'Missing "text" field'}), 400

    text = data['text'].strip()

    if not text:
        return jsonify({'error': 'Text cannot be empty'}), 400

    if len(text) > 10000:
        text = text[:10000]

    logger.info(f"API prediction | Length: {len(text)} chars")

    clean = preprocess_text(text)
    vector = tfidf.transform([clean])
    prediction = model.predict(vector)[0]
    confidence = model.predict_proba(vector)[0]

    if prediction == 0:
        result = 'FAKE NEWS'
        confidence_score = f"{confidence[0]*100:.2f}%"
        emoji = '🚨'
    else:
        result = 'REAL NEWS'
        confidence_score = f"{confidence[1]*100:.2f}%"
        emoji = '✅'

    logger.info(f"API Result: {result} | Confidence: {confidence_score}")

    return jsonify({
        'result': result,
        'confidence': confidence_score,
        'emoji': emoji
    })

# ── Health Check ───────────────────────────────────────────
@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'model': 'loaded'})

if __name__ == '__main__':
    import webbrowser
    webbrowser.open('http://localhost:5000')
    app.run(debug=True)