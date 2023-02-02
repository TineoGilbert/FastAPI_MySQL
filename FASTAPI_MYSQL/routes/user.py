from fastapi import APIRouter
from config.db import connection
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()

@user.get("/users")
async def get_users():
    return connection.execute(users.select()).fetchall()

@user.post("/users")
async def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = connection.execute(users.insert().values(new_user))
    return connection.execute(users.select().where(users.columns.id == result.lastrowid)).first()