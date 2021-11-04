<a href="https://www.correlation-one.com/">
    <img src="doc/correlation-one-logo.png" alt="logo" title="Correlation One" align="right" width="60" height="60" />
</a>

[Read doc in English](README.md)

Code API
========

Este proyecto es una API para realizar challenges de codigo para puestos de trabajo en Data Science, inspirada en la [API de Correlation One](https://quiz.correlation-one.com/test/data-scientist).

La API está desarrollada en Python con [Django REST Framework](https://www.django-rest-framework.org/) (DRF) que permite crear RESTful APIs de manera consistente y escalable. Así mismo se ejecuta sobre un contenedor de Docker que permite correr la aplicación de igual manera en múltiples entornos. La base de datos utilizada para guardar la información de los assesments, takers, y preguntas, es PostgreSQL, también corriendo sobre un contenedor de Docker. 

La API tiene una funcionalidad integrada llamada "Browsable API", que te permite explorar toda la API desde un navegador web, y en esta imagen podés ver la vista principal de la API de assesments.

![screenshot-browsable-api](doc/screenshot-browsable-api.png)

## Comenzando 🚀

Esta sección es una guía con los pasos escenciales para que puedas poner en marcha la aplicación.

<details><summary><b>Mira los pasos necesarios</b></summary><br>

### Instalar las dependencias

Para correr este proyecto es necesario que instales `Docker` y `Docker Compose`. 

En [este artículo](https://www.gotoiot.com/pages/articles/docker_installation_linux/) (en español) están los detalles para instalar Docker y Docker Compose en una máquina Linux. En caso que quieras instalar las herramientas en otra plataforma o tengas algún incoveniente, podes leer la documentación oficial de [Docker](https://docs.docker.com/get-docker/) y también la de [Docker Compose](https://docs.docker.com/compose/install/).

Continua con la descarga del código cuando tengas las dependencias instaladas y funcionando.

### Descargar el código

Para descargar el codigo, lo más conveniente es realizar un `fork` de este proyecto a tu cuenta personal haciendo click en [este link](https://github.com/agustinBassi/django-rest-api/fork). Una vez que ya tengas el fork a tu cuenta, descargalo desde la terminal con este comando (acordate de poner tu usuario en el link):

```
git clone https://github.com/USER/django-rest-api.git
```

> En caso que no tengas una cuenta en Github, o no quieras realizar un fork, podés clonar directamente este repo con el comando `git clone https://github.com/agustinBassi/django-rest-api.git` .

### Configuración inicial del proyecto

Para ejecutar la aplicación, primero es necesario descargar la imagen de la base de datos con el comando `docker-compose pull db`. A continuación, es necesario que compiles el servicio de la REST API con el comando `docker-compose build django-rest-api` (puede demorar unos minutos). 

Cuando los procesos anteriores finalicen, iniciá el servicio de base de datos con el comando `docker-compose up -d db` desde la raíz del proyecto. Con la base de datos corriendo, es necesario crear las tablas que necesita la aplicación para funcionar con los siguientes comandos:

```
docker-compose run django-rest-api python manage.py migrate
```

En este proyecto hay incluídos unos datos de ejemplo para que puedas poner a funcionar la aplicación con información precargada. Es recomendable que importes estos datos para probar la aplicación de manera rápida sin que tengas que cargar los datos de prueba manualmente. Para cargar los datos pre-cargados, ejecuta el siguiente comando:

```
docker-compose run django-rest-api python manage.py loaddata .fixtures/db.json
```

### Ejecutar la aplicación

Con las configuraciones iniciales realizadas, es momento de ejecutar el servicio de la API con el comando `docker-compose up -d django-rest-api` (si querés correr el servicio de manera interactiva, podes quitar el flag -d en la ejecución). Cuando el servicio inicie, podés acceder al `API Browser` desde el navegador ingresando la URL [http://localhost:8000/v1/assesments](http://localhost:8000/v1/assesments) en el navegador. 

Si pudiste acceder al `API browser` significa que la aplicación se encuentra corriendo correctamente.

</details>

Continuá explorando el proyecto una vez que lo tengas funcionando.

## Información principal 🔍

En esta sección vas a encontrar la información para entender y configurar el proyecto.

<details><summary><b>Mira los detalles</b></summary>

### Características principales

A continuación podés ver las características principales del proyecto:

* RESTful API totalmente explorable mediante la "Browsable API"
* Exploración de la API mediante HyperLinks
* Navegación asistida para todos los flujos de la aplicación
* Recuperación de instancias de assesments
* Panel de administración de la aplicación
* Documentación de uso de cada endpoint en la "Browsable API"
* Paginación en todos los endpoints
* Representación de la información en diferentes formatos
* Cálculo de score autmático
* Obtención del tiempo restante de assesment en cada nueva question
* Personalización de API
* Prevención que un taker tenga más de un assesment activo
* Prevención de envío de questions y options incorrectas
* Prevención de re-comenzar una instancia activa o finalizada
* Prevención de obtención de questions de una instancia no activada
* Prevención de envío de respuestas en una instancia no activada
* Amplia documentación de uso
* Versionado de la API de assesments

### Configuración de Django

En el archivo `djangorestapi/settings.py` se encuentra la configuración general del proyecto Django. Dentro de este archivo se pueden realizar todo tipo de configuraciones de Django en la que se destacan las siguientes:

* Selección y configuración del motor de base de datos.
* Aplicaciones instaladas dentro del proyecto.
* Configuración de zona horaria.
* Configuración de debug del proyect.
* Configuración específica de Django REST Framework.
* Configuración de templates.
* Configuración de directorio para archivos estáticos.

Para mayor información sobre toda la posibilidad de configuraciones, podés acceder a la documentación oficial en [este link](https://docs.djangoproject.com/en/3.2/topics/settings/).

### Browsable API

Django REST Framework tiene una funcionalidad nativa que permite hacer navegable la REST API. Esta característica es realmente una funcionalidad excelente, ya que habilita a explorar, navegar y descubrir la API sin tener que abrir ningún programa dedicado (como Postman u otros clientes).

Desde la Browsable API es posible crear instancias de assesments y realizar todos los pasos necesarios para completar el flujo de un assesment (create, test, start, get questions, send answers, end test, get result).

### Cómo usar la API

El punto inicial para comenzar a utilizar la Browsable API es acceder a la URL [http://localhost:8000/v1/assesments](http://localhost:8000/v1/assesments) en el navegador. La aplicación viene con algunos datos cargados para que puedas utilizarla de manera plug & play (es necesario que hayas ejecutado el comando loaddata detallado el apartado de configuración inicial).

Para realizar un `Assesment`, comenzá creando una `Instance` accediento a la URL de un assesment en particular, por ejemplo [http://localhost:8000/v1/assesments/assesments/1/create](http://localhost:8000/v1/assesments/assesments/1/create) con un POST, ingresando los campos `first_name, last_name, email`, como JSON en el body del request. 

Una vez que se crea el assesments, simplemente segui el link `next` provisto en el body del response, que te asistirá en la navegación de todo el flujo del assesment hasta que la finalice.

La respuesta del endpoint devuelve el id y la URL de la instancia creada. Con ese id podés acceder a los siguientes endpoints:

* `instances/<uuid:pk>/`: para obtener los detalles de la instancia.
* `instances/<uuid:pk>/test`: para chequear que la instancia esté disponible para realizarse.
* `instances/<uuid:pk>/start`: para iniciar una instancia, setear el start_time, el end_time y el flag active.
* `instances/<uuid:pk>/questions/<int:q_id>`: en el endpoint para obtener los detalles de la instancia, en el campo `assesment->question_count` se puede obtener la cantidad de preguntas del assesment. Luego, podés acceder a cada una de ellas, desde 1 hasta question_count. Cualquier valor fuera de estos valores devolverá un código 405 Not Allowed.
* `instances/<uuid:pk>/answer`: para enviar la respuesta sobre un assesment. Recibe un question_id y option_id en el body del request. 
* `instances/<uuid:pk>/end`, para finalizar una instancia, setear el end_time, poner el flag active en False y calcular el score automáticamente.
* `instances/<uuid:pk>/result`: para obtener el resultado de una instancia en particular.
* `instances/restore`: para recuperar una instancia (en caso que haya una activa) de un taker en particular.

### Crear Assesments, Questions, Options y sus asociaciones

El servicio de la API tiene integrado un panel de administración que te permite realizar operaciones CRUD sobre cada uno de los modelos (tablas) de la aplicación. En esta imagen podés ver cómo se ve el panel de aministración.

![screenshot-admin-panel](doc/screenshot-admin-panel.png)

Para crear distintos assesments, asignarle questions y options, es necesario ingresar al panel de administrador de la aplicación. Si ejecutaste el comando `python manage.py loaddata .fixtures/db.json` detallado el apartado de configuración inicial, se crea automáticamente un superusuario con el nombre `admin` y pass `admin` (podes cambiar la contraseña para tener una mayor seguridad).

Para ingresar al panel de administrador de la aplicación ingresa en la URL [http://localhost:8000/admin](http://localhost:8000/admin), y loggeate con el usuario y contraseña de superusuario indicado previamente.

Desde el panel izquierdo podrás crear todas las entidades que consideres necesarias y las relaciones entre ellas.

> En caso de no haber ejecutado el comando `python manage.py loaddata .fixtures/db.json`, podés crear un super usuario con el comando `docker-compose run django-rest-api python manage.py createsuperuser`, y luego loggearte en el panel de admin con el usuario creado.

### Variables de entorno

En el archivo `env` están definidas algunas variables de entorno que utiliza el servicio de base de datos, como así también el servicio de la API. Se pueden agregar/quitar las variables necesarias. En caso de borrar accidentalmente los valores o el archivo env, a continuación podés encontrar unos valores que funcionan correctamente con la aplicación.

```
DJANGO_SECRET_KEY=sup3rs3cr3tk3y
DJANGO_DEBUG=True
DATABASE_NAME=codedb
DATABASE_USER=postgres
DATABASE_PASS=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
```

Es **ALTAMENTE RECOMENDABLE** que cambies estas variables si querés utilizar esta aplicación con fines productivos.

### Manipulación de base de datos

Django provee una excelente manipulación de la base de datos sin que sea necesario usar ninguna herramienta externa para realizar las operaciones necesarias.

Si se quiere realizar un backup simple de la base de datos, ejecutar el siguiente comando:

```
docker-compose run django-rest-api \
python manage.py dumpdata --indent 2 > .fixtures/db.json
```

Si se quiere realizar un backup de la base de datos que pueda ser utilizado en una fresh database, ejecutar el siguiente comando:

```
docker-compose run django-rest-api \
python manage.py dumpdata --indent 2 \
--exclude auth.permission --exclude contenttypes --exclude admin.logentry > .fixtures/db.json
```

Para cargar los datos de la aplicación en una fresh database, ejecutar el siguiente comando para crear las tablas necesarias:

```
docker-compose run django-rest-api python manage.py migrate
```

Y luego cargar datos dentro de las tablas:

```
docker-compose run django-rest-api python manage.py loaddata .fixtures/db.json
```

</details>

## Información complementaria 📚

En esta sección vas a encontrar información que te va a servir para tener un mayor contexto.

<details><summary><b>Lee esta info</b></summary>

### ERD (Entity-Relation Desing)

Para el diseño de las entidades y sus relaciones, se utilizó la herramienta online [EDR Plus](https://erdplus.com/standalone), que permite crear entidades, atributos y relaciones de manera muy sencilla. En la siguiente figura podes ver el diagrama de entidad-relacion del sistema.

![architecture](doc/entity-relation-diagram.png)

Un `Assesment` se define una única vez, y además de sus atributos, tiene asociado una o varias `Questions`. A su vez, cada `Questions` tiene asociada una o más `Options`.

Para poder realizar un `Assesment` es necesario que un `Taker` se registre con sus datos, y que cree una `Instance` de un `Assesment`. Cada `Instance` tiene, además de sus atributos, un UUID como identificador. Esto permite que, desde otro navegador se pueda recuperar la instancia en función de los datos del Taker. 

### Endpoints

A continuación se lista cada uno de los endpoints, con su descripción y métodos disponibles.

* `assesments/` - Muestra una lista con todos los recursos disponibles de la aplicación (GET)
* `assesments/assesments` - Muestra una lista con todos los assesments disponibles (GET)
* `assesments/assesments/<id>` - Muestra la HOME de un test específico (GET)
* `assesments/assesments/<id>/status` - Chequea el estado de un assesment y devuelve su status (GET)
* `assesments/assesments/<id>/create` - Crea una nueva instancia de un assesment y devuelve el UUID de la instancia (POST)
* `assesments/instances` - Muestra una lista con todas las instancias disponibles (GET)
* `assesments/instances/<id>` - Muestra el detalle de la instancia (GET)
* `assesments/instances/<id>/test` - Chequea que la instancia este activa (GET)
* `assesments/instances/<id>/start` - Inicia el test y empieza el countdown (POST)
* `assesments/instances/<id>/questions/<id>` - Muestra el detalle con la pregunta de una instancia (GET)
* `assesments/instances/<id>/answer` - Envía el resultado de una respuesta (PUT)
* `assesments/instances/<id>/end` - Finaliza una instancia (POST)
* `assesments/instances/<id>/result` - Muestra el resultado de una instancia (GET)
* `assesments/instances/restore` - Permite recuperar una instancia en función de los datos de un usuario (POST)
* `assesments/takers` - Muestra una lista con todos los tests takers que realizaron assesments (GET)
* `assesments/takers/<id>` - Muestra el detalle de un taker específico (GET)
* `assesments/questions` - Muestra una lista con todos las questions disponibles (GET)
* `assesments/questions/<id>` - Muestra el detalle de una question específico (GET)
* `assesments/options` - Muestra una lista con todos las options disponibles (GET)
* `assesments/options/<id>` - Muestra el detalle de una option específico (GET)

Si bien en la lista anterior se encuentra la información de cada endpoint, es mucho mejor navegar mediante la `Browsable API` que permite acceder a mayor información sobre cada uno de los endpoints.

### Estructura de directorios

```sh
├── .fixtures                       # dir to save DB fixtures to export/import using Django manage.py
├── assesments (important files)    # main assesments app dir
│   ├── migrations                  # dir to track DB modifications
│   ├── admin.py                    # register assesments model into admin interface
│   ├── models.py                   # assesments models declaration
│   ├── serializers.py              # classes for serialize/deserialize models instances
│   ├── urls.py                     # configuration of app routes
│   └── views.py                    # bussiness logic function and classes
├── djangorestapi                         # main Django project
│   ├── asgi.py                     # utility to load Django app into ASGI servers
│   ├── settings.py                 # main Django project settings
│   ├── urls.py                     # main Django project URLs configuration
│   └── wsgi.py                     # utility to load Django app into WSGI servers
├── doc                             # dir to save documentation
│   └── ...
├── tests                           # dir to save test files and assets (no unit tests)
│   └── ...
├── .gitignore                      # exclude files from versions control
├── .dockerignore                   # exclude files when build a docker image
├── Contribuitors.md                # project contribuitors
├── Dockerfile                      # Dockerfile for Django project
├── LICENSE                         # licencia del proyecto
├── README.md                       # este archivo
├── docker-compose.yml              # configuración de los contenedores de Docker centralizada
├── env                             # variables de entorno utilizadas en el proyecto
├── manage.py                       # archivo con utilidades nativas de Django
└── requirements.txt                # dependencias de Python del proyecto
```

### Correlation-One Requests/Responses

Para entender de mejor manera la funcionalidad de la API de Correlation One, podés realizar el flujo de un assesment ingresando en [este link](https://quiz.correlation-one.com/test/data-scientist). Así mismo, revisando el tráfico de red desde la ventana de development del navegador, analizando y entendiendo la información enviada y recibida en cada request, podrás tener un mejor contexto sobre la funcionalidad necesaria.

Para facilitar el acceso a la información de los endpoints, podés acceder al archivo `doc/api-requests-responses.md`, donde se encuentran guardados los requests/responses realizados contra la API de Correlation One.

Gran parte de la funcionalidad está inspirada en los mensajes de la API, aunque con algunas diferencias.

</details>


## TODOs 📝

En esta sección podés ver las funcionalidades pendientes del proyecto y una posible forma de implementarlas.

<details><summary><b>Mira la lista completa de pendientes</b></summary><br>

* **Armar los requests con Postman**: Si bien el challenge requiere armar los requests con Postman, resulta más valioso utilizar la Browsable API y la navegación automatizada de sus flujos que utilizar Postman.
* **Ejecutar la aplicación con un servidor web productivo.**: Para el desarrollo y demostración de la aplicación se utiliza el servidor web de desarrollo de Django. Si se quisiera implementar un servidor productivo, en [este link](https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/uwsgi/), por ejemplo, hay información para configurar uWSGI.
* **Comprimir responses**: Si se utilizara un servidor web productivo, se podría realizar la compresión de las respuestas. En [este link](https://rtcamp.com/tutorials/nginx/enable-gzip/) hay un tutorial para habilitar Gzip en un servidor Nginx.
* **Autenticación de usuarios**: Actualmente la API permite que cualquier usuario pueda ver los endpoints de la aplicación, y crear nuevas instancias. Se podría realizar autenticación de usuarios utilizando JWT o bien OAuth. Django provee mecanismos built-in para el manejo de autenticación y autorización de usuarios, pero para mantener el proyecto lo más conciso posible, se decició no incluir esta característica.
* **Encriptación por SSL**: Este proyecto tiene fines demostrativos, y además utiliza el web server de desarrollo provisto por Django. Si se quisiera llevar este proyecto a un entorno productivo, se debería implementar SSL en el webserver utilizado. Por ejemplo en [este link](https://www.youtube.com/watch?v=NhidVhNHfeU) se encuentra información sobre cómo configurar los certificados en Nginx. Así mismo, en [este link](https://timonweb.com/django/https-django-development-server-ssl-certificate/) hay un tutorial sobre cómo habilitar HTTPS utilizando el Django development server.
* **Soportar otros formatos mas que texto**: Si bien el challenge requería que se puedan manejar más de un formato para las questions y options, en esta API solo tienen un formato (CharField). En ese campo de texto se puede guardar tanto texto plano como HTML. Si se quisiera guardar una imagen, se podría alojar en un bucket de S3 y en el campo sólo guardar la URL.
* **Testing automatizado.**: Si bien tener testing automatizado es una característica totalmente necesaria, para este proyecto no se implementó. Aunque implementar unit testing no resulta demasiado complejo. Si se quisiera implementar, en [este link](https://docs.djangoproject.com/en/3.2/topics/testing/overview/) se encuentra toda la información necesaria.

</details>

## Tecnologías utilizadas 🛠️

En esta sección podés ver las tecnologías más importantes utilizadas.

<details><summary><b>Mira la lista completa de tecnologías</b></summary><br>

* [Docker](https://www.docker.com/) - Ecosistema que permite la ejecución de contenedores de software.
* [Docker Compose](https://docs.docker.com/compose/) - Herramienta que permite administrar múltiples contenedores de Docker.
* [Python](https://www.python.org/) - Lenguaje en el que están realizados los servicios.
* [Django](https://www.djangoproject.com/) - Popular framework en Python para desarrollo de aplicaciones web.
* [Django REST Framework](https://www.django-rest-framework.org/) - Framwork basado en Django para el diseño de REST APIs.
* [PostgreSQL](https://www.postgresql.org/) - Base de datos para consultar y almacenar datos.
* [Visual Studio Code](https://code.visualstudio.com/) - Popular IDE de desarrollo para múltiples plataformas.

</details>

## Contribuir 🖇️

Si estás interesado en el proyecto y te gustaría sumar fuerzas para que siga creciendo y mejorando, podés abrir un hilo de discusión para charlar tus propuestas en [este link](https://github.com/agustinBassi/django-rest-api/issues/new). Así mismo podés leer el archivo [Contribuir.md](https://github.com/gotoiot/gotoiot-doc/wiki/Contribuir) donde están bien explicados los pasos para que puedas enviar pull requests.

## Muestas de agradecimiento 🎁

Si te gustó este proyecto y quisieras apoyarlo, cualquiera de estas acciones estaría más que bien para mí:

* Apoyar este proyecto con una ⭐ en Github para llegar a más personas.
* Compartir este proyecto con otras personas.

## Autores 👥

Las colaboraciones principales fueron realizadas por:

* **[Agustin Bassi](https://github.com/agustinBassi)**: Ideación, puesta en marcha y mantenimiento del proyecto.

También podés mirar todas las personas que han participado en la [lista completa de contribuyentes](https://github.com/agustinBassi/django-rest-api/contributors).

## Licencia 📄

Este proyecto está bajo Licencia ([MIT](https://choosealicense.com/licenses/mit/)). Podés ver el archivo [LICENSE.md](LICENSE.md) para más detalles sobre el uso de este material.
