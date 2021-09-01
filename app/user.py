from infrastructure import UserRepository
from core import User


async def register(user: User, repo: UserRepository):
    return await repo.register(user.username, user.password)


async def login(user: User, repo: UserRepository):
    return await repo.login(user.username, user.password)
