import joblib
import os

def load_model():
    """Load trained model and vectorizer"""
    model_path = 'models/fake_news_model.pkl'
    vectorizer_path = 'models/vectorizer.pkl'
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            "Model not found! Run train.py first.")
    
    model = joblib.load(model_path)
    tfidf = joblib.load(vectorizer_path)
    return model, tfidf

def get_confidence_label(confidence):
    """Return confidence level label"""
    if confidence >= 90:
        return "Very High ✅"
    elif confidence >= 75:
        return "High 👍"
    elif confidence >= 60:
        return "Medium ⚠️"
    else:
        return "Low ❓"

def format_result(prediction, confidence):
    """Format prediction result"""
    if prediction == 0:
        return {
            'result': 'FAKE NEWS',
            'confidence': f"{confidence[0]*100:.2f}%",
            'level': get_confidence_label(
                confidence[0]*100),
            'color': 'danger',
            'emoji': '🚨'
        }
    else:
        return {
            'result': 'REAL NEWS',
            'confidence': f"{confidence[1]*100:.2f}%",
            'level': get_confidence_label(
                confidence[1]*100),
            'color': 'success',
            'emoji': '✅'
        }