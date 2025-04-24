FROM aksacr9098.azurecr.io/uaac/python:3.10-alpine

WORKDIR /app
COPY .  /app

# Remove local .env file
RUN rm .env

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]
