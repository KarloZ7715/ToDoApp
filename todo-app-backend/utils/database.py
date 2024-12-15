from flask import current_app
from pymongo import MongoClient


def get_db():
    client = MongoClient(current_app.config["MONGO_URI"])
    db = client.get_default_database()
    return db
