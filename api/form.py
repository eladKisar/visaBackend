from fastapi import APIRouter, HTTPException
from infrastructure import MongoFormRepo
from starlette.status import *
from app import form_actions
from typing import List
from core import Form

router = APIRouter()

repo = MongoFormRepo()


@router.get("/")
async def get_all() -> List[Form]:
    return await form_actions.get_all(repo)


@router.post("/")
async def post(content: dict):
    if not await form_actions.create(content, repo):
        raise HTTPException(HTTP_400_BAD_REQUEST)


@router.get("/{form_id}")
async def by_id(form_id: str) -> Form:
    return await form_actions.by_id(form_id, repo)


@router.put("/{form_id}")
async def update(form_id: str, content: dict):
    if not await form_actions.update(form_id, content, repo):
        raise HTTPException(HTTP_400_BAD_REQUEST)


@router.delete("/{form_id}")
async def delete(form_id: str):
    if not await form_actions.delete(form_id, repo):
        raise HTTPException(HTTP_400_BAD_REQUEST)
