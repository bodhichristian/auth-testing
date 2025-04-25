import uuid
from enum import Enum
from datetime import date

class UserType(Enum):
    ADMIN = 'admin'
    STANDARD = 'standard'

class User:
    def __init__(self, username: str, password_hash: str, user_type=UserType.STANDARD, id: str=None, created_on: date=None):
        self.username = username
        self.password_hash = password_hash
        self.user_type = user_type
        self.id = id or str(uuid.uuid4())
        self.created_on = created_on or date.today()

    def to_dict(self):
        return {
            "username": self.username,
            "password_hash": self.password_hash,
            "user_type": self.user_type.value,
            "id": self.id,
            "created_on": self.created_on.isoformat()
        }

    @staticmethod
    def from_dict(data: dict):
        return User(
            username=data['username'],
            password_hash=data['password_hash'],
            user_type=UserType(data.get("user_type", "standard")),
            id=data['id'],
            created_on=date.fromisoformat(data.get('created_on'))
        )