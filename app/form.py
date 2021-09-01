from infrastructure import FormRepository
from typing import List
from core import Form


async def get_all(repo: FormRepository) -> List[Form]:
    return await repo.all()


async def create(content: dict, repo: FormRepository):
    return await repo.create(content)


async def by_id(form_id: str, repo: FormRepository):
    return await repo.read(form_id)


async def update(form_id: str, content: dict, repo: FormRepository):
    return await repo.update(form_id, content)


async def delete(form_id: str, repo: FormRepository):
    return await repo.delete(form_id)
