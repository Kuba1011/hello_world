FROM python:3.11-slim                         # Używa lekkiego obrazu Pythona
WORKDIR /app                                  # Ustawia katalog roboczy w kontenerze
COPY requirements.txt .                       # Kopiuje plik z zależnościami
RUN pip install -r requirements.txt           # Instaluje zależności
COPY . .                                      # Kopiuje całą zawartość projektu
ENV FLASK_APP=app                             # Ustawia zmienną środowiskową
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]  # Uruchamia aplikację
