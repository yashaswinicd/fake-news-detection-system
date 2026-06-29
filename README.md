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
📄 **[Project Page](https://yashaswinicd.github.io/fake-news-detection-system)**

## 🎬 Demo
🎥 **[Watch Demo on YouTube](https://youtu.be/Ci_ZUK16QH0)**



![Demo](screenshots/demo.gif)



## 📌 Project Overview
A Machine Learning web app that detects whether a news article is **Real or Fake** using NLP and Logistic Regression.

## ⚙️ How It Works
1. 📝 User pastes a news article into the web app
2. 🧹 Text is cleaned — lowercase, remove special characters
3. 🔤 NLTK removes stopwords and applies stemming
4. 📐 TF-IDF Vectorizer converts text to numbers
5. 🧠 Logistic Regression model predicts Real or Fake
6. 📊 Confidence score is displayed to the user

## ✨ Features
- ✅ 98.61% Accuracy
- ✅ AUC Score: 0.9981
- ✅ Real-time prediction
- ✅ Confidence score display
- ✅ Beautiful web UI

## 💻 System Requirements
- Python 3.8+
- RAM: 4GB minimum
- OS: Windows / Linux / macOS
- Browser: Chrome / Firefox / Edge

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
```

## 📊 Model Results

| Metric | Value |
|--------|-------|
| Accuracy | 98.61% |
| Precision | 98.7% |
| Recall | 98.6% |
| F1 Score | 98.6% |
| ROC AUC | 0.9981 |

## ⚠️ Known Limitations
- Works only on English news articles
- Performance depends on training dataset
- May not detect highly sophisticated fake news
- Free hosting may have 50 second cold start delay

## 📁 Project Structure

```
fake-news-detection-system/
├── data/
│   └── raw/
├── models/
│   ├── fake_news_model.pkl
│   └── vectorizer.pkl
├── notebooks/
├── screenshots/
├── static/
├── templates/
├── tests/
├── utils/
├── app.py
├── train.py
├── predict.py
└── requirements.txt
```

## 🔮 Future Improvements
- 🤖 BERT/RoBERTa model for better accuracy
- 🌐 Multilingual support (Hindi, Kannada)
- 🔍 Explainable AI using SHAP/LIME
- 🚀 REST API for mobile apps
- 🐳 Docker deployment
- 📱 Mobile app integration

## 👩‍💻 Built By
**Yashaswini C D** | CSE Student | Aspiring AI/ML Engineer

---

## ❓ FAQ

**Q: What types of news can this detect?**  
A: English language news articles and headlines.

**Q: How accurate is the model?**  
A: 98.61% accuracy on the test dataset with AUC score of 0.9981.

**Q: Can I use my own dataset?**  
A: Yes! Replace the CSV files in `data/raw/` and retrain using `train.py`.

**Q: Does it work on Kannada or Hindi news?**  
A: Currently English only. Multilingual support is a planned future improvement.

**Q: Why is the app slow to load sometimes?**  
A: Free Render hosting has a ~50 second cold start delay when inactive.

---

## 📚 References

- [Kaggle - Fake and Real News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [NLTK Documentation](https://www.nltk.org/)
- [TF-IDF - Wikipedia](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

---

## 🙏 Acknowledgements

- Dataset by **Clément Bisaillon** on Kaggle
- Built as part of **BE CSE Project** at Akshaya Institute of Technology, Tumakuru
- Thanks to the open-source community for Python, Flask, and Scikit-learn

---

## 📋 Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0.0 | June 2026 | Initial release — 98.61% accuracy, Flask web app, CI/CD pipeline |