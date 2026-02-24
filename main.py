from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests
import json

app = FastAPI()

# Static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="templates")

# 🔑 Replace this with your real API key
API_KEY = "pub_7b1275cfbebc4faab0cd704bc2d5285e"


@app.get("/", response_class=HTMLResponse)
def home(request: Request, category: str = "top"):

    # Base URL
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&country=in&language=en"

    # Add category if selected
    if category != "top":
        url += f"&category={category}"

    try:
        response = requests.get(url)
        data = response.json()
    except Exception:
        data = {"results": []}

    # Save JSON to file
    with open("news_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    # Extract articles safely
    articles = data.get("results", [])

    return templates.TemplateResponse("index.html", {
        "request": request,
        "articles": articles,
        "selected_category": category
    })


# Optional: Direct JSON endpoint
@app.get("/api/news")
def get_news(category: str = "top"):

    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&country=in&language=en"

    if category != "top":
        url += f"&category={category}"

    response = requests.get(url)
    return response.json()