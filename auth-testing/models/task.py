import uuid
from enum import Enum
from datetime import date
from models.user import User

class Task:
    def __init__(self, title: str, description: str, creator_id: str, assigned_id: str=None, id: str=None, created_on: date=None, due_date: date=None):
        self.title = title
        self.description = description
        self.creator_id = creator_id
        self.assigned_to = assigned_id
        self.id = id or str(uuid.uuid4())
        self.created_on = created_on or date.today()
        self.due_date = due_date or None

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'created_by': self.creator_id,
            'assigned_id': self.assigned_to,
            'id': self.id,
            'created_on': self.created_on.isoformat(),
            'due_date': self.due_date.isoformat() if self.due_date else None
        }

    @staticmethod
    def from_dict(data: dict):
        return User(
            title=data.get('title'),
            description=data.get('description'),
            created_by=data.get('creator_id'),
            assigned_to=data.get('assigned_id'),
            uuid=data.get('id'),
            created_on=data.get('created_on'),
            due_date=data.get('due_date')
        )