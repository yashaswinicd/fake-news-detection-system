# 🔍 Fake News Detection System



![Python](https://img.shields.io/badge/Python-3.8+-blue)




![Accuracy](https://img.shields.io/badge/Accuracy-98.61%25-brightgreen)




![AUC](https://img.shields.io/badge/AUC-0.9981-orange)




![Flask](https://img.shields.io/badge/Flask-3.1-green)




![Live](https://img.shields.io/badge/Live-Demo-red)




![Last Commit](https://img.shields.io/github/last-commit/yashaswinicd/fake-news-detection-system)




![License](https://img.shields.io/github/license/yashaswinicd/fake-news-detection-system)




![Stars](https://img.shields.io/github/stars/yashaswinicd/fake-news-detection-system)



## 🌐 Live Demo
👉 **[Click here to try the app](https://fake-news-detection-system-21yi.onrender.com)**

## 📌 Project Overview
A Machine Learning web app that detects whether a news article is **Real or Fake** using NLP and Logistic Regression.

## ✨ Features
- ✅ 98.61% Accuracy
- ✅ AUC Score: 0.9981
- ✅ Real-time prediction
- ✅ Confidence score display
- ✅ Beautiful web UI

## 🏗️ Architecture


![Architecture](screenshots/architecture.png)



## 📸 Screenshots

### Home Page


![Home](screenshots/home.png)



### Prediction Result


![Result](screenshots/result.png)



### Model Performance


![Confusion Matrix](screenshots/confusion_matrix.png)




![ROC Curve](screenshots/roc_curve.png)



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
git clone https://github.com/yashaswinicd/fake-news-detection-system.git
cd fake-news-detection-system
pip install -r requirements.txt
python train.py
python app.py