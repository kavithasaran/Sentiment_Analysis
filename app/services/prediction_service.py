
import numpy as np

from app.services.preprocessing import (
    clean_review_text,
    tokenize_review
)


def get_word2vec_vector(tokens, word2vec_model):

    vectors = [
        word2vec_model.wv[word]
        for word in tokens
        if word in word2vec_model.wv
    ]

    if not vectors:
        return np.zeros(word2vec_model.vector_size)

    return np.mean(vectors, axis=0)


def predict_sentiment(review, selected_model, models):

    (
        tfidf_vectorizer,
        tfidf_model,
        word2vec_model,
        word2vec_classifier
    ) = models

    cleaned_review = clean_review_text(review)

    if not cleaned_review:
        raise ValueError("Please enter a valid review.")

    if selected_model == "tfidf":

        review_vector = tfidf_vectorizer.transform(
            [cleaned_review]
        )

        prediction = tfidf_model.predict(review_vector)[0]

    elif selected_model == "word2vec":

        tokens = tokenize_review(cleaned_review)

        review_vector = get_word2vec_vector(
            tokens,
            word2vec_model
        )

        prediction = word2vec_classifier.predict(
            [review_vector]
        )[0]

    else:
        raise ValueError("Invalid model selection.")

    return str(prediction)
