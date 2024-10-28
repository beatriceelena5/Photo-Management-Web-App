FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p static/uploads metadata && chmod -R 755 static metadata

COPY static/uploads /init_data/static/uploads
COPY metadata /init_data/metadata

EXPOSE 5000

CMD ["sh", "-c", "cp -r /init_data/static/uploads/* /app/static/uploads/ && cp -r /init_data/metadata/* /app/metadata/ && flask run --host=0.0.0.0"]
