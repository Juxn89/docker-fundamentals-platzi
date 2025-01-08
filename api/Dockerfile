FROM python:3.13.1-alpine3.20

# Workind directory: Create a directory into container, allthe files of the application will be hosted
WORKDIR /app

# Copy files or directory from local to the container.
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]

#Tuve un problema con el puerto que comunica el contenedor a la aplicación (el segundo puerto), a 
#diferencia de la página web, que nginx utiliza el puerto 80, flask utiliza por defecto el puerto 5000,
#por lo que si se quiere utilizar los puertos 8085:80 flask arrojara un error, ya que con el puerto 
#8085 el local se comunica al contenedor (Funciona siempre y cuando no estes ocupando ya ese puerto) 
#y despues el contenedor intenta comunicarse al puerto 80 lo cual no tendrá nada ya que Flask está en el 5000.