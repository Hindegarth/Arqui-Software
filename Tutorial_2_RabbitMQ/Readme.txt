Lo que se hizo en el tutorial fue seguir las instrucciones de como se comportan las cosas en rabbitmq

Para resumir las cosas de la utilizacion de los ejemplos de rabbitmq, es que existe un servidor en el terminal que espera recibir un mensaje
por otro lado existe un mensajero que da el mensaje al servidor, para realizar una accion.

Cada uno tiene su utilidad:
	hello-world simplemente, recibe un mensaje en blanco y el servidor muestra hello world

	rpc, el recibe un mensaje en blanco y retorna fibonnacci de 30

	work-queue, por su parte este codigo nos permite tener varios servidores y cada vez que llevemos un mensaje tendran un trabajo establecido y un tiempo dependiendo de este mismo
		ademas de que al haber varios cada trabajo se distribuye equitativamente, si se modificara algunos aspectos podriamos realizar que los trabajos se distribuyan por
		el tiempo que lleva trabajando el trabajador

	publish-subscribe, es igual que la mayoria de los demas pero se centra en ver el tema de las colas

Por ultimo nos queda la tarea, tiene una estructura muy parecida a la de los work-queue, sin embargo, wiki.py se le importo wikipedia donde al recibir el argumento del mensajero realizara
una busqueda en wikipedia del resumen del tema en particular, hay que tener en claro que el idioma que se busca en la wikipedia es español
por otra parte, tenemos video que al recibir el argumento del mensajero te da las caracteristicas del canal de youtube
	