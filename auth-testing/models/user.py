from datetime import date

class User:
    def __init__(self, username: str, password_hash: str, created_on: str = None):
        self.username = username
        self.password_hash = password_hash
        self.created_at = created_on or date.today().isoformat()  # YYYY-MM-DD

    def to_dict(self):
        return {
            "username": self.username,
            "password_hash": self.password_hash,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data: dict):
        return User(
            username=data["username"],
            password_hash=data["password_hash"],
            created_on=data.get("created_at")
        )