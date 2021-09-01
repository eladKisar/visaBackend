from infrastructure.repository import UserRepository, FormRepository
from infrastructure.entity import UserEntity, FormEntity
from mongoengine.errors import InvalidDocumentError
from typing import Optional
from core import User, Form
from typing import List


class MongoUserRepo(UserRepository):
    async def register(self, username: str, password: str) -> bool:
        try:
            UserEntity(
                username=username,
                password=bytes(password, 'ascii'),
                salt=b"test"
            ).save()
            return True
        except InvalidDocumentError:
            return False

    async def login(self, username: str, password: str) -> Optional[User]:
        user_query = UserEntity.objects.get(username=username)
        if isinstance(user_query, list):
            users = [document for document in UserEntity.objects.get(username=username)]
            if len(users) == 0:
                return None
            return users[0]
        else:
            return user_query


class MongoFormRepo(FormRepository):
    async def all(self) -> List[Form]:
        return [
            document.to_dict() for document in
            FormEntity.objects
        ]

    async def create(self, content: dict):
        try:
            FormEntity(
                content=content
            ).save()
            return True
        except:
            return False

    async def read(self, form_id: str):
        return [
            document for document in
            FormEntity.objects.get(form_id=form_id)
        ][0]

    async def update(self, form_id: str, content: dict):
        for form in FormEntity.objects.get(form_id=form_id):
            form.content = content
            form.save()

    async def delete(self, form_id: str):
        for form in FormEntity.objects.get(form_id=form_id):
            form.delete()
