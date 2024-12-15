import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path, override=True)


class Config:
    """Configuración base"""

    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious_secret_key")
    DEBUG = False
    TESTING = False
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/todoAppDB")


class DevelopmentConfig(Config):
    """Configuración de desarrollo"""

    DEBUG = True
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/todoAppDB_dev")


class TestingConfig(Config):
    """Configuración para pruebas"""

    TESTING = True
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/todoAppDB_test")


class ProductionConfig(Config):
    """Configuración de producción"""

    SECRET_KEY = os.getenv("SECRET_KEY")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/todoAppDB_prod")


def get_config():
    """Obtener la configuración adecuada según el entorno"""
    env = os.getenv("FLASK_ENV", "development").lower()
    if env == "production":
        return ProductionConfig()
    elif env == "testing":
        return TestingConfig()
    else:
        return DevelopmentConfig()
