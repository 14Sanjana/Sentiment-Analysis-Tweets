# 💬 Tweet Sentiment Analysis using **NLP**

This project focuses on analyzing the **sentiment of tweets** using both **Logistic Regression** and **LSTM** techniques. It includes the full pipeline from text preprocessing to model evaluation and prediction.

---

## 🎯 Objective

Classify tweets into one of the following sentiments:

- 😄 **Positive**
- 😞 **Negative**
- 😐 **Neutral** *(if applicable in extended dataset)*

---

## 🧠 Technologies Used

### 📝 **Languages**
- Python

### 📚 **Libraries**
- `Pandas`, `NumPy` – Data manipulation  
- `NLTK`, `re` – Text preprocessing  
- `Scikit-learn` – TF-IDF, Logistic Regression  
- `TensorFlow`, `Keras` – LSTM model  

---

## 📦 Dataset

- **Source:** Kaggle Twitter Sentiment Dataset  
- Loaded using Pandas for processing and analysis.

---

## 🔄 Project Pipeline

### 📥 1. Dataset Import
- Load Twitter sentiment data from a CSV file.

### 🧹 2. Text Preprocessing
- Lowercase text  
- Remove URLs, hashtags, mentions, stopwords, punctuation, etc.

### 🧪 3. Feature Engineering
- Convert cleaned text into numerical vectors using **TF-IDF Vectorizer**

### 🧠 4. Model Building
- **Logistic Regression** (ML approach)  
- **LSTM** (DL approach using TensorFlow/Keras)

### 📊 5. Model Evaluation
- Accuracy Score  
- Confusion Matrix  
- Classification Report

### 🤖 6. Prediction System
- Input: Tweet index or custom tweet  
- Output: Sentiment label + Confidence Score

---

## 🧾 Output Format

```text
Input Tweet: "I love the new features in this update!"
Predicted Sentiment: Positive 😄
Confidence: 91.24%

Enter Tweet Index (from dataset): 0
Tweet: "My whole body feels itchy and like it’s on fire"
Prediction: Negative 😞
Confidence: 51.24%

```
![Screenshot 2025-04-06 212737](https://github.com/user-attachments/assets/c0b14513-b773-437d-8d28-42cba98a8552)

⚙️ How to Run

1.Clone the repository
git clone https://github.com/yourusername/tweet-sentiment-analysis.git
cd tweet-sentiment-analysis


2.Install dependencies
pip install -r requirements.txt


3.Run the notebook
Open Sentiment_analysis_tweets.ipynb in Jupyter Notebook or Google Colab


