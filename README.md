# Code API

### Permissions

Cuando se ejecutan los comandos desde dentro del contenedor de docker, se ejecutan con el usuario root. Esto impide luego editar la estructura de directorios adecuadamente. Una vez que se crean el proyecto y/o las aplicaciones de Django, es conveniente ejecutar el comando `sudo chown -R $USER:$USER .` para dar permisos al usuario:grupo sobre todo el proyecto.

Así mismo, y debido a que la carpeta de `data` que contiene la base de datos es necesario que el owner sea root, luego de la operación anterior, ejecutar el comando `sudo chown -R root:root data/` que dejará los permisos adecuadamente seteados en todo el proyecto.

> En caso de crearse nuevos proyectos/aplicaciones desde dentro de los contenedores de Docker, repetir las operaciones.

### Commands execution

Por la misma razon que los permisos, es conveniente ejecutar los comandos con el usuario `gotoiot` creado dentro del contendor. Para ello, cada vez que se tenga que ejecutar un comando dentro del contenedor, poner este prefijo `docker-compose run code-api su gotoiot -c 'python manage.py COMMAND'`.

