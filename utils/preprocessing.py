import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords', quiet=True)

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    """
    Clean and preprocess text for ML model.
    Steps:
    1. Lowercase
    2. Remove special characters  
    3. Remove stopwords
    4. Stemming
    """
    # Lowercase
    text = text.lower()
    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokenize
    words = text.split()
    # Remove stopwords and stem
    words = [stemmer.stem(w) for w in words 
             if w not in stop_words]
    return ' '.join(words)

def clean_dataset(df):
    """Apply preprocessing to entire dataset"""
    df['clean_text'] = df['text'].apply(preprocess_text)
    return df