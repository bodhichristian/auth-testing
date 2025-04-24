import uuid
from datetime import date

class User:
    def __init__(self, username: str, password_hash: str, id: str=None, created_on: date=None):
        self.username = username
        self.password_hash = password_hash
        self.id = id or str(uuid.uuid4())
        self.created_on = created_on or date.today()

    def to_dict(self):
        return {
            "username": self.username,
            "password_hash": self.password_hash,
            "id": self.id,
            "created_on": self.created_on.isoformat()
        }

    @staticmethod
    def from_dict(data: dict):
        return User(
            username=data['username'],
            password_hash=data['password_hash'],
            id=data['id'],
            created_on=date.fromisoformat(data.get('created_on'))
        )