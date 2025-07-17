Tweet Sentiment Analysis using ML & DL
This project focuses on analyzing the sentiment of tweets using Machine Learning (Logistic Regression) and Deep Learning (LSTM). It includes the full pipeline: text cleaning, feature extraction (TF-IDF), model training, evaluation, and prediction.

The goal is to classify tweets into:

Positive 😄

Negative 😞

Neutral 😐 (if applicable in extended dataset)

🧠 Technologies Used
Languages: Python

Libraries:

Pandas, NumPy – Data manipulation

NLTK, re – Text preprocessing

Scikit-learn – TF-IDF, Logistic Regression

TensorFlow, Keras – LSTM model

Matplotlib, Seaborn – Data visualization

Steps in the Project
Dataset Import:

Twitter Sentiment dataset imported from Kaggle.

Text Preprocessing:

Lowercasing, removing punctuation, stopwords, URLs, hashtags, etc.

Feature Engineering:

Using TF-IDF vectorizer to convert text to numeric features.

Model Building:

Logistic Regression for baseline classification.

LSTM model using TensorFlow/Keras for deep learning approach.

Model Evaluation:

Accuracy, Confusion Matrix, Classification Report, etc.

Prediction System:

Takes user input as tweet index or text and returns sentiment + confidence.

🧾 Output Format
Input Tweet: "I love the new features in this update!"
Predicted Sentiment: Positive 😄
Confidence: 91.24%

Enter Tweet Index (from dataset): 0
Tweet: "My whole body feels itchy and like it’s on fire"
Prediction: Negative 😞
Confidence: 51.24%


![Screenshot 2025-04-06 212737](https://github.com/user-attachments/assets/c0b14513-b773-437d-8d28-42cba98a8552)

📌 How to Run
Clone the repository

Install dependencies from requirements.txt

Run Sentiment_analysis_tweets.ipynb in Jupyter or Colab

