from flask import Blueprint, jsonify       # Import blueprintu i JSON-owej odpowiedzi

bp = Blueprint('main', __name__)           # Tworzy blueprint o nazwie 'main'

@bp.route("/")                             # Definiuje endpoint GET "/"
def hello():
    return jsonify(message="hello world")  # Zwraca odpowiedź w formacie JSON
