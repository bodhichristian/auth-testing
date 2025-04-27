import uuid
from enum import Enum
from datetime import date

class TaskType(Enum):
    REQUEST = 'request'
    TODO = 'todo'

class Task:
    def __init__(self, title: str, description: str, task_type: TaskType, id: str=None, created_on: date=None, due_date: date=None):
        self.title = title
        self.description = description
        self.task_type = task_type
        self.id = id or str(uuid.uuid4())
        self.created_on = created_on or date.today()
        self.due_date = due_date
