# Imagen base de Python
FROM python:3.11-slim

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar todo el contenido del proyecto dentro del contenedor
COPY . /app

# Instalar dependencias si tenés un requirements.txt
# (si no lo tenés, este paso no hace nada)
RUN pip install --no-cache-dir -r requirements.txt || true

# Comando para ejecutar la app (ajustá el nombre si tu archivo se llama distinto)
CMD ["python", "convertir_txt_excel.py"]
