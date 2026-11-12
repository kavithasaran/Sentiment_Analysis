from app.services.preprocessing import clean_review_text, tokenize_review


def test_clean_review_text():
    text = "<p>This is a GREAT product!</p> https://example.com"

    result = clean_review_text(text)

    assert result == "this is a great product"


def test_tokenize_review():
    text = "This is a great product!"

    result = tokenize_review(text)

    assert result == ["this", "is", "a", "great", "product"]


def test_empty_review():
    result = clean_review_text("")

    assert result == ""
