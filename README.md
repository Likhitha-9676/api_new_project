# 📰 Dynamic News Portal using FastAPI

A dynamic news web application built using FastAPI, Jinja2, HTML, and CSS.  
The application fetches real-time news from the NewsData API and displays category-based news with search functionality.

---

## 🚀 Features

- 🔎 Search news by keyword
- 🏷 Category-based filtering (Top, Sports, Entertainment, Education)
- 🌐 Real-time API integration
- 📄 JSON response saved locally
- 🎨 Responsive UI with styled navigation buttons
- ⚡ FastAPI backend
- 🧠 Jinja2 templating for dynamic rendering

---

## 🛠 Technologies Used

- Python
- FastAPI
- Jinja2
- HTML5
- CSS3
- NewsData.io API

---

## 📂 Project Structure

news_fastapi_project/

├── main.py  
├── news_data.json  
├── README.md  
├── templates/  
│   └── index.html  
└── static/  
    └── style.css  

---

## 🔑 API Setup

1. Go to https://newsdata.io  
2. Create a free account  
3. Generate your API key  
4. Open `main.py`  
5. Replace:

```python
API_KEY = "YOUR_API_KEY_HERE"
