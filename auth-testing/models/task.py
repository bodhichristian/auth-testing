import uuid
from enum import Enum
from datetime import date
from models.user import User

class Task:
    def __init__(self, title: str, description: str, creator_id: str, assigned_id: str=None, id: str=None, created_on: date=None, due_date: date=None, completed: bool=False):
        self.title = title
        self.description = description
        self.creator_id = creator_id
        self.assigned_id = assigned_id or creator_id
        self.id = id or str(uuid.uuid4())
        self.created_on = created_on or date.today()
        self.due_date = due_date or None
        self.completed = completed

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'creator_id': self.creator_id,
            'assigned_id': self.assigned_id,
            'id': self.id,
            'created_on': self.created_on.isoformat(),
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data: dict):
        return Task(
            title=data.get('title'),
            description=data.get('description'),
            creator_id=data.get('creator_id'),
            assigned_id=data.get('assigned_id'),
            id=data.get('id'),
            due_date=data.get('due_date'),
            completed=data.get('completed')
        )