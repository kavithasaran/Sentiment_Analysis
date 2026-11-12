
import re


def clean_review_text(text):
    """
    Clean review text using the preprocessing steps
    used during model training.
    """
    if not isinstance(text, str):
        text = str(text)

    text = text.lower()

    # Remove HTML tags
    text = re.sub(r"<.*?>", " ", text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove punctuation
    text = re.sub(r"[^\w\s]", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


def tokenize_review(text):
    """
    Tokenize cleaned review text for Word2Vec.
    """
    cleaned_text = clean_review_text(text)
    return cleaned_text.split()
