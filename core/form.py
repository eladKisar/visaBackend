from pydantic import BaseModel


class Form(BaseModel):
    form_id: str
    content: dict
