<a href="https://www.gotoiot.com/">
    <img src="doc/gotoiot-logo.png" alt="logo" title="Goto IoT" align="right" width="60" height="60" />
</a>

Code API
========

Este proyecto es una API para realizar challenges de codigo para puestos de trabajo en Data Science. Está inspirada en la [API de Correlation One](https://quiz.correlation-one.com/test/data-scientist).

El proyecto está desarrollado en Python con Django REST Framework (DRF) que permite crear RESTful APIs escalables. Así mismo se ejecuta sobre un contenedor de Docker que permite correr el proyecto de igual manera en múltiples plataformas. Para la comunicación con la base de datos se utiliza PostgreSQL corriendo también sobre un contendor de Docker. Ambos servicios se ejecutan utilizando la herramienta Docker Compose, que permite ejecutar ambos servicios desde un mismo archivo, de manera centralizada y humanamente entendible.

En esta imagen se puede ver un diagrama de la arquitectura del proyecto.

![architecture](doc/architecture.png)

## Comenzando 🚀

Esta sección es una guía con los pasos escenciales para que puedas poner en marcha la aplicación.

<details><summary><b>Mira los pasos necesarios</b></summary><br>

### Instalar las dependencias

Para correr este proyecto es necesario que instales `Docker` y `Docker Compose`. 

En [este artículo](https://www.gotoiot.com/pages/articles/docker_installation_linux/) están los detalles para instalar Docker y Docker Compose en una máquina Linux. En caso que quieras instalar las herramientas en otra plataforma o tengas algún incoveniente, podes leer la documentación oficial de [Docker](https://docs.docker.com/get-docker/) y también la de [Docker Compose](https://docs.docker.com/compose/install/).

Continua con la descarga del código cuando tengas las dependencias instaladas y funcionando.

### Descargar el código

Para descargar el codigo, lo más conveniente es realizar un `fork` de este proyecto a tu cuenta personal haciendo click en [este link](https://github.com/agustinBassi/code-api/fork). Una vez que ya tengas el fork a tu cuenta, descargalo desde la terminal con este comando (acordate de poner tu usuario en el link):

```
git clone https://github.com/USER/connection-mqtt.git
```

> En caso que no tengas una cuenta en Github, o no quieras realizar un fork, podés clonar directamente este repo con el comando `git clone https://github.com/agustinBassi/code-api.git` .

### Ejecutar la aplicación

Para ejecutar la aplicación tenes que correr el comando `docker-compose up -d db` desde la raíz del proyecto. Este comando va a descargar la imagen de la base de datos y la va a poner a correr. Una vez ejecutado el comando anterior, es necesario que compiles el servicio de la REST API con el comando `docker-compose build code-api` (puede demorar unos minutos). 

Una vez que compile el servicio, podés ejecutarlo de manera interactiva en la terminal con el comando `docker-compose up code-api` (si querés correr el servicio en segundo plano, podés agregar el flag -d en la ejecución). Cuando el servicio inicie, podés acceder al `API Browser` desde el navegador ingresando la URL [http://localhost:8000/](http://localhost:8000/) en el navegador.

Si pudiste acceder al `API browser` significa que la aplicación se encuentra corriendo bien.

</details>

Continuá explorando el proyecto una vez que lo tengas funcionando.

## Información principal 🔍

En esta sección vas a encontrar la información para entender y configurar el proyecto.

<details><summary><b>Mira los detalles</b></summary>


</details>

## Información complementaria 📚

En esta sección vas a encontrar información que te va a servir para tener un mayor contexto.

<details><summary><b>Lee esta info</b></summary>

### Permissions

Cuando se ejecutan los comandos desde dentro del contenedor de docker, se ejecutan con el usuario root. Esto impide luego editar la estructura de directorios adecuadamente. Una vez que se crean el proyecto y/o las aplicaciones de Django, es conveniente ejecutar el comando `sudo chown -R $USER:$USER .` para dar permisos al usuario:grupo sobre todo el proyecto.

Así mismo, y debido a que la carpeta de `data` que contiene la base de datos es necesario que el owner sea root, luego de la operación anterior, ejecutar el comando `sudo chown -R root:root data/` que dejará los permisos adecuadamente seteados en todo el proyecto.

> En caso de crearse nuevos proyectos/aplicaciones desde dentro de los contenedores de Docker, repetir las operaciones.

### Commands execution

Por la misma razon que los permisos, es conveniente ejecutar los comandos con el usuario `gotoiot` creado dentro del contendor. Para ello, cada vez que se tenga que ejecutar un comando dentro del contenedor, poner este prefijo `docker-compose run code-api su gotoiot -c 'python manage.py COMMAND'`.

### Sobre Django

En estos slides hay una buena y simple info sobre lo que puede hacer Django REST Framework. Sobre todo agrega la parte de filtrado, ordering, y busqueda que estan muy buenas.

### Ejecución de servicios

Los servicios de la aplicación se ejecutan sobre contenedores de Docker, así se pueden desplegar de igual manera en diferentes plataformas. Los detalles sobre cómo funcionan los servicios los podés ver directamente en el archivo **docker-compose.yml** y complementar la información con el README de cada parte de la app.

</details>

## Tecnologías utilizadas 🛠️

En esta sección podés ver las tecnologías más importantes utilizadas.

<details><summary><b>Mira la lista completa de tecnologías</b></summary><br>

* [Docker](https://www.docker.com/) - Ecosistema que permite la ejecución de contenedores de software.
* [Docker Compose](https://docs.docker.com/compose/) - Herramienta que permite administrar múltiples contenedores de Docker.
* COMPLETAR PYTHON
* COMPLETAR DJANGO
* COMPLETAR DJANGO REST FRAMEWORK

</details>

## Contribuir 🖇️

Si estás interesado en el proyecto y te gustaría sumar fuerzas para que siga creciendo y mejorando, podés abrir un hilo de discusión para charlar tus propuestas en [este link](https://github.com/gotoiot/connection-mqtt/issues/new). Así mismo podés leer el archivo [Contribuir.md](https://github.com/gotoiot/gotoiot-doc/wiki/Contribuir) donde están bien explicados los pasos para que puedas enviar pull requests.

## Muestas de agradecimiento 🎁

Si te gustó este proyecto y quisieras apoyarlo, cualquiera de estas acciones estaría más que bien para mí:

* Apoyar este proyecto con una ⭐ en Github para llegar a más personas.
* Compartir este proyecto con otras personas.

## Autores 👥

Las colaboraciones principales fueron realizadas por:

* **[Agustin Bassi](https://github.com/agustinBassi)**: Ideación, puesta en marcha y mantenimiento del proyecto.

También podés mirar todas las personas que han participado en la [lista completa de contribuyentes](https://github.com/connection-mqtt/contributors).

## Licencia 📄

Este proyecto está bajo Licencia ([MIT](https://choosealicense.com/licenses/mit/)). Podés ver el archivo [LICENSE.md](LICENSE.md) para más detalles sobre el uso de este material.

# TODOs

* Armar los requests con Postman
* Not permitir que un taker tome mas de un test al mismo tiempo
