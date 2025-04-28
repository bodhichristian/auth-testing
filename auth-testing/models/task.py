import uuid
from enum import Enum
from datetime import date

class Task:
    def __init__(self, title: str, description: str, created_by: User.id, assigned_to: User.id=None, id: str=None, created_on: date=None, due_date: date=None):
        self.title = title
        self.description = description
        self.created_by = created_by
        self.assigned_to = assigned_to
        self.id = id or str(uuid.uuid4())
        self.created_on = created_on or date.today()
        self.due_date = due_date

    def to_dict(self):
        return {
            'title': self.titledescription,
            'description': self.description,
            'created_by': self.created_by,
            'assigned_to': self.assigned_to,
            'id': self.id,
            'created_on': self.created_on.isoformat()
            'due_date': self.due_date.isoformat() if self.due_date else None
        }

    @staticmethod
    def from_dict(data: dict):
        return User(
            title=data.get('title'),
            description=data.get('description'),
            created_by=data.get('created_by'),
            assigned_to=data.get('assigned_to'),
            id=data.get('id'),
            created_on=data.get('created_on'),
            due_date=data.get('due_date')
        )