Para este tutorial, segui la instrucciones de los tutoriales:
- En la Seccion, del consumer y publisher, al utilizar Docker-compose build y Docker-compose up Simplemente esperamos tener un mensaje,
el cual se responde automaticamente despues de ser recibido y luego se finaliza el proceso de RabbitMQ.

Punto a tener BASTANTE en cuenta.

Es que en todos los Docker-compose.yml, se tuvo que modificar los ports de rabbitmq pasando de '15672:15672' -> 15672 Y '5672:5672' -> 5672
de alguna manera solucionaba el problema de utilizar Docker-compose up, ya que si no se hacia el cambio el rabbitmq se porteaba DOS veces provocando un error
haciendo imposible seguir.

Por otra parte, para que funcionara las traducciones y busquedas de wikipedia en el bot de slack simplemente segui los pasos del tutorial implementado por el profesor aunque con algunos cambios:

- Las secciones que fueron modificadas para que YO pueda utilizarlo, fueron las de los TOKEN_SLACK Y TOKEN_SINGING_TICKET principalmente para que mi bot se conectara con el docker
- el ngrok tenia que ser ejecutado antes que cualquier otra cosa, usar docker-compose up, para que se conectara a docker, sin embargo, tenia que finalizar el proceso, o almenos
estar muy cerca de hacerlo para que esten conectados, y de esta manera poder conectar el ngrok con el bot slack. Luego de todo tenia que reiniciar el proceso de docker y al reiniciarlo
esta apto para realizar las busquedas y traducciones que funcionaban completamente.
