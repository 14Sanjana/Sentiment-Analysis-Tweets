from sklearn.linear_model import LogisticRegression
import joblib

def train_logistic_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, "../models/logistic_model.pkl")
    return model
