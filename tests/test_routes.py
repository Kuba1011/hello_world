import pytest                           # Importuje pytest
from app import create_app              # Importuje funkcję tworzącą aplikację

@pytest.fixture
def client():
    app = create_app()                  # Tworzy instancję aplikacji
    return app.test_client()            # Tworzy klienta testowego

def test_hello(client):
    response = client.get("/")          # Wysyła zapytanie GET do "/"
    assert response.status_code == 200
    assert response.json == {"message": "hello world"}  # Sprawdza odpowiedź JSON
