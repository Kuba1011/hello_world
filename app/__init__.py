from flask import Flask            # Importuje główną klasę Flask
from app.routes import bp          # Importuje blueprint z pliku routes

def create_app():
    app = Flask(__name__)          # Tworzy instancję aplikacji Flask
    app.register_blueprint(bp)     # Rejestruje blueprint z trasami
    return app                     # Zwraca gotową aplikację
