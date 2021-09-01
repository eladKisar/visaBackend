from mongoengine.document import Document
import mongoengine.fields
from typing import Any


# noinspection PyProtectedMember
def parse_dict(obj: Any):
    return_data = []

    if isinstance(obj, Document):
        return_data.append(("id", str(obj.id)))

    for field_name in obj._fields:

        if field_name in ("id",):
            continue

        data = obj._data[field_name]

        if isinstance(obj._fields[field_name], mongoengine.fields.DateTimeField):
            return_data.append((field_name, str(data.isoformat())))
        elif isinstance(obj._fields[field_name], mongoengine.fields.StringField):
            return_data.append((field_name, str(data)))
        elif isinstance(obj._fields[field_name], mongoengine.fields.FloatField):
            return_data.append((field_name, float(data)))
        elif isinstance(obj._fields[field_name], mongoengine.fields.IntField):
            return_data.append((field_name, int(data)))
        elif isinstance(obj._fields[field_name], mongoengine.fields.ListField):
            return_data.append((field_name, data))
        elif isinstance(obj._fields[field_name], mongoengine.fields.DictField):
            return_data.append((field_name, data))
        elif isinstance(obj._fields[field_name], mongoengine.fields.EmbeddedDocumentField):
            return_data.append((field_name, parse_dict(data)))

    return dict(return_data)


class UserEntity(Document):
    user_id = mongoengine.fields.UUIDField()
    username = mongoengine.fields.StringField()
    password = mongoengine.fields.BinaryField()
    salt = mongoengine.fields.BinaryField()

    def to_dict(self):
        return parse_dict(self)


class FormEntity(Document):
    form_id = mongoengine.fields.UUIDField()
    content = mongoengine.fields.DictField()

    def to_dict(self):
        return parse_dict(self)
