"""
Создать API для добавления нового пользователя в базу данных. Приложение
должно иметь возможность принимать POST запросы с данными нового
пользователя и сохранять их в базу данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для добавления нового пользователя (метод POST).
Реализуйте валидацию данных запроса и ответа.


"""
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="templates")
users = []


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


class UserIn(BaseModel):
    name: str
    email: str
    password: str


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Главная"}
    )


@app.get("/users/", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse(
        "users.html", {"request": request, "users": users, "title": "Пользователи"}
    )


@app.post("/users/")
async def add_user():
    return RedirectResponse("/login/", status_code=302)


@app.get("/login/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse(
        "registration.html", {"request": request, "title": "Новый пользователь"}
    )


@app.post("/login/", response_class=RedirectResponse)
async def create_user(
    request: Request,
    name=Form(min_length=2, max_length=20),
    email=Form(),
    password=Form(min_length=6),
):
    users.append(
        User(
            id=len(users) + 1,
            name=name,
            email=email,
            password=password,
        )
    )
    return templates.TemplateResponse(
        "success.html",
        context={"request": request, "name": name, "title": "Успешно"},
        status_code=302,
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return templates.TemplateResponse(
        "error.html", {"request": request, "title": "Ошибка", "exc": exc}
    )


@app.put("/users/", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    for user in users:
        if user.id == user_id:
            user.name = new_user.name
            user.email = new_user.email
            user.password = new_user.password
            return user
        else:
            raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/", response_model=dict)
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": f"User with id = {user_id} was deleted."}

        else:
            raise HTTPException(status_code=404, detail="User not found")


if __name__ == "__main__":
    uvicorn.run("hw5:app", host="127.0.0.1", port=8000, reload=True)
