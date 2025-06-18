# Imagen base con Python
FROM python:3.11-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo Python
COPY app.py .

# Comando que se ejecuta al iniciar el contenedor
CMD ["python", "app.py"]
