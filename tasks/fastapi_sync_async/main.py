from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import SessionLocal
from models import User

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/form", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/form")
async def post_form(name: str = Form(...), email: str = Form(...)):
    db = SessionLocal()
    db.add(User(name=name, email=email))
    db.commit()
    db.close()
    return RedirectResponse("/thankyou", status_code=302)

@app.get("/thankyou", response_class=HTMLResponse)
async def thank_you(request: Request):
    return templates.TemplateResponse("thankyou.html", {"request": request})

@app.get("/async-form", response_class=HTMLResponse)
async def get_async_form(request: Request):
    return templates.TemplateResponse("async_form.html", {"request": request})

@app.post("/async-form")
async def post_async_form(name: str = Form(...), email: str = Form(...)):
    from celery_app import save_user_async
    save_user_async.delay(name, email)
    return RedirectResponse("/thankyou_async", status_code=302)

@app.get("/thankyou_async", response_class=HTMLResponse)
async def thank_you_async(request: Request):
    return templates.TemplateResponse("thankyou_async.html", {"request": request})

