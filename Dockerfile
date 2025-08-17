#imagen base de python
FROM python:3.10-slim
#Directorio de trabajo
WORKDIR /app
#Copiar los archivos necesarios
COPY . .
#Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

#Exponer el puerto de la aplicación
EXPOSE 8080

#Comando para ejecutar la aplicación
CMD ["python", "app.py"]
# para correr un programa se necesita un declarador y este seria el declarador de las API
