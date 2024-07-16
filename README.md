# Administración del recinto

## Descripción

Proyecto destinado a prácticar Django.
Su estructura se baso en el tutorial de Youtube creado en el canal
[Develoteca - Oscar Uh](https://www.youtube.com/watch?v=ezIj71CX944)
y adaptado a una necesidad real de planillas de Google Sheets pertenecientes
a la administración de un recinto de artes marciales.

## Requerimientos

El proyecto utiliza **Python 3.12.3** y se ejecuta en un entorno virtual
creado con el comando `python -m venv entornovirtual`. Dentro del entorno
mediante el instalador de paquetes **pip (versión 24.1.2)**, se instalo
**Django 5.0.7 y Pillow 10.4.0** (para el manejo de imagenes),
con los comandos `pip install django` y `pip install Pillow` respectivamente.
Junto a Django se instalan las siguientes dependencias: **asgiref 3.8.1,**
**sqlparse 0.5.1 y tzdata==2024.1**.
Por último, dado que el proyecto utiliza una base de datos SQL creada con
**MySQL Workbench 8.0 CE** se debe instalar **pymysql 1.1.1** con el comando
`pip install pymysql`.

## Ejecutar localmente el proyecto

Primero se debe configurar la información sobre el acceso a tu base de datos en
el archivo **settings.py** que se encuentra en _sistema/sistema_, en el apartado:

```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nombre-de-la-base-de-datos',
            'USER': 'nombre-de-usuario',
            'PASSWORD': 'password-de-usuario',
            'HOST': 'localhost',
            'PORT': '3306',
    }
}
```

Luego nos situamos en la ruta _entornovirtual/Scripts_ ejecutamos el comando `activate`
desde la terminal. Luego nos desplazamos a la carpeta _sistema_ tipeamos el comando
`python manage.py runserver`.
Para detener el servidor presionamos **Ctrol + C** y para desactivar el entorno virtual
tipeamos en la terminal `deactivate`.

## Contribuir

1. Haz un **fork** del proyecto.
2. Crea una nueva rama `git checkout -b feature-name`.
3. Haz commit a tus cambios `git commit -am "título de la nueva funcionalidad"`.
4. Haz push a la rama `git push origin feature-name`.
5. Crea un **pull request**.

## Versiones

### v. 1.0.0

- Cuenta con una página de inicio donde se puede apreciar el listado de alumnos presentes en la base de datos.
- Además posee botones para acceder a las secciones de agregar y editar alumnos desde un formulario y permite borrar alumnos desde otro botón destinado a ello.
- Toda la interfaz de usuario (UI) se desarrollo mediante el uso de **Bootstrap 5.3.3**.
