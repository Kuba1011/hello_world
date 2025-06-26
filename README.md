# hello_world

Modularna aplikacja webowa napisana w Pythonie (Flask), której zadaniem jest zwrócenie JSON-a pod endpointem `/`.

---

## Funkcjonalność

Po wywołaniu endpointu `GET /` aplikacja zwraca odpowiedź:

```json
{ "message": "hello world" }


##Struktura projektu

hello_world/
├── app/                  # Moduł aplikacji Flask
│   ├── __init__.py       # Fabryka aplikacji
│   └── routes.py         # Trasa "/" zwracająca JSON
├── tests/                # Test jednostkowy w pytest
│   └── test_routes.py
├── requirements.txt      # Lista zależności (flask, pytest)
├── Dockerfile            # Konfiguracja budowy obrazu kontenera
├── docker-compose.yml    # Uruchomienie aplikacji w kontenerze
└── .github/
    └── workflows/
        └── ci.yml        # GitHub Actions workflow (CI)



##Uruchomienie lokalne

1. Zainstaluj zależności:

python -m pip install -r requirements.txt


2. Ustaw zmienną środowiskową i uruchom aplikację:

$env:FLASK_APP = "app"      # Windows PowerShell
python -m flask run


3. Przeglądarka:

http://localhost:5000/

## Uruchomienie w Dockerze

Aby uruchomić aplikację w kontenerze Dockera:

1. Upewnij się, że masz zainstalowany [Docker Desktop](https://www.docker.com/products/docker-desktop/)

2. W katalogu projektu uruchom:

   ```bash
   docker-compose up --build

3. Otwórz przeglądarkę i przejdź do:

http://localhost:5000
Powinieneś zobaczyć odpowiedź:

{ "message": "hello world" }

4. Aby zatrzymać kontener naciśnij CTRL + C, a żeby go całkowicie wyłączyć:

docker-compose down



##GitHub Actions – CI
Workflow znajduje się w pliku .github/workflows/ci.yml.

Automatycznie uruchamia się przy każdym:

pushu do main,

pull request do main.

Wykonuje:

instalację zależności,

uruchomienie testów pytest.

Działa na systemie windows-latest z użyciem Python 3.11.