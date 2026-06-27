# 🔍 Fake News Detection System



![Python](https://img.shields.io/badge/Python-3.8+-blue)




![Accuracy](https://img.shields.io/badge/Accuracy-98.61%25-brightgreen)




![AUC](https://img.shields.io/badge/AUC-0.9981-orange)




![Flask](https://img.shields.io/badge/Flask-3.1-green)



## 📌 Project Overview
A Machine Learning web app that detects whether a news article is **Real or Fake** using NLP and Logistic Regression.

## ✨ Features
- 98.61% Accuracy
- AUC Score: 0.9981
- Real-time prediction
- Confidence score display
- Beautiful web UI

## 🛠️ Tech Stack
- Python | Scikit-learn | NLTK
- TF-IDF Vectorization
- Logistic Regression
- Flask | Bootstrap 5

## 📊 Dataset
- Source: Kaggle
- Fake news: 23,481 articles
- Real news: 21,417 articles
- Total: 44,898 articles

## 🚀 Installation
```bash
git clone https://github.com/yashaswinicd/fake-news-detection.git
cd fake-news-detection
pip install -r requirements.txt
python train.py
python app.py