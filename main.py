from fastapi import FastAPI,Request 
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

Templates = Jinja2Templates (directory = "templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/create')
def home_page(request:Request):
    return Templates.TemplateResponse("home_page.html",{"request":request})
