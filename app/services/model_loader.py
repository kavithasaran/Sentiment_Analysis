from pathlib import Path

import joblib
from gensim.models import Word2Vec

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Models directory
MODEL_DIR = BASE_DIR / "models"


def load_models():

    # Load TF-IDF vectorizer and Logistic Regression model
    tfidf_vectorizer = joblib.load(MODEL_DIR / "tfidf_vectorizer.pkl")

    tfidf_model = joblib.load(MODEL_DIR / "logistic_regression_tfidf.pkl")

    # Load Word2Vec model and Logistic Regression model
    word2vec_model = Word2Vec.load(str(MODEL_DIR / "word2vec_model.model"))

    word2vec_classifier = joblib.load(MODEL_DIR / "logistic_regression_word2vec.pkl")

    return (tfidf_vectorizer, tfidf_model, word2vec_model, word2vec_classifier)
