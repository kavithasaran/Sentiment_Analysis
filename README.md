# Sentiment Analysis WebApp

## Project Overview

A Machine Learning web application built using FastAPI to predict customer review sentiment.

The application supports two trained Machine Learning models:

1. **TF-IDF + Logistic Regression**
2. **Word2Vec + Logistic Regression**

The user can enter a review heading and customer review, select a model from the dropdown, and predict whether the sentiment is Positive, Negative, or Neutral.

## Technologies Used

- Python
- FastAPI
- Scikit-learn
- Gensim
- NumPy
- Pandas
- HTML, CSS, JavaScript
- Jinja2
- Pytest

## Project Structure

```text
Sentiment_Analysis_WebApp/
├── app/
│   ├── routes/
│   ├── services/
│   ├── schemas/
│   ├── templates/
│   └── static/
├── models/
├── tests/
├── data/
├── notebooks/
├── requirements.txt
├── Dockerfile
├── render.yaml
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Sentiment_Analysis_WebApp
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
python -m pip install pytest httpx
```

### 5. Run the application

```bash
python -m uvicorn app.main:app --reload
```

### 6. Open the application

Web application:

http://127.0.0.1:8000/

API documentation:

http://127.0.0.1:8000/docs

## Model Files

Place the four trained model files inside the `models/` directory:

- tfidf_vectorizer.pkl
- logistic_regression_tfidf.pkl
- word2vec_model.model
- logistic_regression_word2vec.pkl

## Running Tests

Run all project tests:

```bash
python -m pytest
```

## Features

- Customer review sentiment prediction.
- Two Machine Learning model options.
- Interactive web interface.
- FastAPI prediction endpoint.
- Automated testing using Pytest.
