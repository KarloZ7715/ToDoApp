from datetime import datetime, timezone
from bson import ObjectId


class Todo:
    """Modelo para las tareas de la ToDo App"""

    def __init__(
        self,
        text: str,
        completed: bool = False,
        priority: str = "Media",
        dueDate: datetime = None,
        user_id: str = None,
    ):
        self.text = text
        self.completed = completed
        self.priority = priority
        self.dueDate = dueDate if dueDate else None
        self.user_id = ObjectId(user_id) if user_id else None
        self.createdAt = datetime.now(timezone.utc)
        self.updatedAt = datetime.now(timezone.utc)

    def to_dict(self) -> dict:
        """Convierte la instancia de Todo a un diccionario para almacenar en la base de datos"""
        todo_dict = {
            "text": self.text,
            "completed": self.completed,
            "priority": self.priority,
            "dueDate": self.dueDate,
            "user_id": self.user_id,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }
        return todo_dict

    @staticmethod
    def from_dict(data: dict) -> "Todo":
        """Crea una instancia de Todo a partir de un diccionario obtenido de la base de datos"""
        return Todo(
            text=data.get("text", ""),
            completed=data.get("completed", False),
            priority=data.get("priority", "Media"),
            dueDate=data.get("dueDate"),
            user_id=str(data.get("userId")) if data.get("userId") else None,
        )
