from fastapi import APIRouter, HTTPException
from infrastructure import MongoUserRepo
from starlette.status import *
from app import user_actions
from core import User

router = APIRouter()


@router.post("/login")
async def login(user: User):
    if not await user_actions.login(user, MongoUserRepo()):
        raise HTTPException(HTTP_401_UNAUTHORIZED)


@router.post("/register")
async def register(user: User):
    if not await user_actions.register(user, MongoUserRepo()):
        raise HTTPException(HTTP_400_BAD_REQUEST)
