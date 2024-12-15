from flask import Flask
from routes.todo_routes import todo_bp
from config import get_config

app = Flask(__name__)
app.config.from_object(get_config())

app.register_blueprint(todo_bp, url_prefix="/api/todos")

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
