from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes.prediction import router
from app.services.model_loader import load_models


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Load trained models when the application starts
    app.state.models = load_models()

    yield


app = FastAPI(
    title="Sentiment Analysis WebApp",
    description="Sentiment prediction using TF-IDF and Word2Vec",
    version="1.0.0",
    lifespan=lifespan,
)


# Load static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configure HTML templates
templates = Jinja2Templates(directory="app/templates")


# Register prediction API
app.include_router(router)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"request": request}
    )
