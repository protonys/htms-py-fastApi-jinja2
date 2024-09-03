import uvicorn
from fastapi import FastAPI, Request, Response, Form, status
from fastapi.responses import RedirectResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates

from db.dbc import CheckUsersByLogin

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "name": 123 })   

@app.post("/")
async def home(request: Request, login = Form(), password=Form()):
    res, token = CheckUsersByLogin(login, password)
    if res:
        response = templates.TemplateResponse("home.html", {"request": request, "name": f'login:{login} password:{password}' })   
        response.set_cookie(key="token", value=token)        
        return response
    else:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    

@app.get("/home")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "name": "Привет home"})   

@app.get("/login")
async def home(request: Request):  
    headers = {'Content-Type': 'application', 'X_Print': 'True', 'MyHeader': 'SimpleText'}
    return templates.TemplateResponse(request, "login.html", {"name": "Привет login"}, 201, headers)  


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
