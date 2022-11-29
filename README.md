# App de vehiculos

Este es un proyecto para el cuarto ciclo de aprendizaje de programación básica de MINTIC Colombia

### ¿Para qué es este repositorio?

* Sistema para una app para app de venta de vehiculos.
* El sistema gestiona el control de compras del contenido visto.
* El sistema está construído con Django y postgresql.

### ¿Cómo lo configuro?

* Clona este repositorio
* Instala Python 3.5
* Crea un [entorno virtual](https://docs.python.org/3/library/venv.html)
* Activa el entorno virtual (`"directorio_padre"\"carpeta_entorno_virtual"\Scripts\activate`)
* Instala los requerimientos (`pip install -r requirements.txt`)
* ejecuta el comando makemigrations (`python manage.py makemigrations`)
* ejecuta el comando migrate para hacer las migraciones (`python manage.py migrate`)
* Corre el servidor (`python manage.py runserver`)
* Crea un superusuario (`python manage.py createsuperuser`)
* Visita http://localhost:8000/admin
