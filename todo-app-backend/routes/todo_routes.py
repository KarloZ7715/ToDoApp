from flask import Blueprint, request, jsonify
from services.todo_service import TodoService

todo_bp = Blueprint("todos", __name__)


@todo_bp.route("/", methods=["GET"])
def get_todos():
    todos = TodoService.get_all_todos()
    return jsonify(todos)


@todo_bp.route("/", methods=["POST"])
def create_todo():
    data = request.get_json()
    todo = TodoService.create_todo(data)
    return jsonify(todo), 201


@todo_bp.route("/<id>", methods=["PUT"])
def update_todo(id):
    data = request.get_json()
    update_todo = TodoService.update_todo(id, data)
    return jsonify(update_todo)


@todo_bp.route("/<id>", methods=["DELETE"])
def delete_todo(id):
    TodoService.delete_todo(id)
    return "", 204
