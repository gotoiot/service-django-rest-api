# Entity Relation Design

En la siguiente figura podes ver el diagrama de entidad-relacion.

![architecture](doc/erd.png)

Segun el entendimiento, un Assesment se define una única vez, y además de un título, y descripción tiene asociadas, una o varias preguntas. A su vez, cada pregunta tiene asociada dos o más opciones.

Desde el lado del AssesmentTaker, en el momento que está listo para tomar un assesment, se crea una instancia, que tiene asociada una duración, una fecha de inicio y fin, un UUID y el progreso del Assesment. Esto permite que, desde otro navegador se pueda recuperar el UUID de la instancia en función de los datos del TestTaker. 

# Endpoints design

* `/` - Muestra una lista con los recursos disponibles (GET)
* `/assesments` - Muestra una lista con todos los tests disponibles (GET)
* `/assesments/<id>` - Muestra la HOME de un test específico (GET)
* `/assesments/<id>/create` - Crea una nueva instancia de un assesment y devuelve el UUID de la instancia (POST)
* `/instances/<id>` - Muestra el detalle de la instancia (GET)
* `/instances/<id>/test` - Chequea que la instancia este activa (GET)
* `/instances/<id>/start` - Inicia el test y empieza el countdown (POST)
* `/instances/<id>/end` - Finaliza una instancia (POST)
* `/instances/<id>/result` - Muestra el resultado de una instancia (GET)
* `/assesments/<id>/questions` - Muestra una lista con las preguntas de una instancia (GET)
* `/assesments/<id>/questions/<id>` - Muestra el detalle con la pregunta de una instancia (GET). Envia el resultado de una respuesta (POST).
* `/takers` - Muestra una lista con todos los tests takers que realizaron assesments (GET)
* `/takers/<id>` - Muestra el detalle de un taker específico (GET)
* `/status?id=xx` - Recibe como query argument el id de la instancia (GET)

# Correlation One API Request/responses
