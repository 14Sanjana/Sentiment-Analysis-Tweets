import joblib
from preprocess import clean_text

def predict_sentiment(text, vectorizer_path, model_path):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    text_cleaned = clean_text(text)
    X = vectorizer.transform([text_cleaned])
    prediction = model.predict(X)
    return prediction[0]
