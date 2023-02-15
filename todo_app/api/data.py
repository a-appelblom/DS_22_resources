from pyodbc import IntegrityError
import bcrypt
from sqlalchemy.orm import Session
from db_models import User
from api_models import Login


def check_user_exists(email: str, db: Session):
    data = db.query(User).filter(User.email == email).first()

    if data is None:
        return False
    else:
        return True


def create_user(login: Login, db: Session):
    try:
        pwd = bcrypt.hashpw(login.password.encode("utf-8"), bcrypt.gensalt())
        new_user = User(display_name=login.email, email=login.email, password=pwd)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        print("Could not create user")
        return None
    return new_user
