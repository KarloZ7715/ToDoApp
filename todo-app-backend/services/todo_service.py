from bson import ObjectId
from pymongo import ReturnDocument
from typing import List, Optional, Any
from models.todo import Todo
from utils.database import get_db


class TodoService:
    """Servicio para manejar operaciones relacionadas con las tareas"""

    @staticmethod
    def get_all_todos(user_id: Optional[str] = None) -> List[Todo]:
        """Obtiene todas las tareas si se proporciona un id de usuario"""
        db = get_db()
        query = {}
        if user_id:
            try:
                query["user_id"] = ObjectId(user_id)
            except Exception:
                raise ValueError("user_id inválido")
        todos_cursor = db.todos.find(query)
        todos = []
        for todo in todos_cursor:
            todo["_id"] = str(todo["_id"])
            if todo.get("user_id"):
                todo["user_id"] = str(todo["user_id"])
            todos.append(todo)
        return todos
