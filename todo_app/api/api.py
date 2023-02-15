from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api_models import User, Login
from db import get_db
import data

app = FastAPI()


@app.post("/auth/sign_up")
def sign_up(login: Login, db: Session = Depends(get_db)):
    # existing_user: bool = data.check_user_exists(login.email, db)
    # if existing_user:
    new_user = data.create_user(login=login, db=db)
    if new_user is None:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, "User with that email already exists"
        )
    return new_user


@app.post("/auth/login")
def login(login: Login):
    pass


# @app.get("/todos")
# def get_todos(user_id):
#     print("user", user)
#     pass


if __name__ == "__main__":
    sign_up(Login(email="anton@email.com", password="test"))
