En Pytest, al seguir las sesiones de las clases, entendi que en resumen sirve para la comprobacion del resultado deseado de un codigo
por lo que nos permite probar funciones tanto en sus mejores y peores casos.

al seguir el tutorial, hay una amplia cantidad de ejercicios para aprender como funciona el pytest, el cual solo ejecuta los test_...py y ..._test.py, las demas funciones
se usan para importaciones.

Por otro lado tambien existen Practicas las cuales se realizaron dos, la de fizzbuzz y los numeros romanos, los demas eran simples ejercicios que no aportaban mucho mas.

Y por ultimo la tarea:



1.- A partir la correción N°2 del Bot Néstor, agregar pruebas unitarias a los distintos componentes de la arquitectura. ¿Qué ejemplos de pruebas proponen?

	Dado que no tengo alguna idea de como implementar las pruebas unitarias en docker no pude agregarlas, pero si puedo dar ideas de que podrian hacer las cuales serian:

	- En los casos de que alguien quiera buscar en wikipedia algo, Si el mensaje que se le dio al bot es diferente al titular de su resumen deberia anularlo, esto lo digo
	debido a que cuando no se identifica bien el idioma ó se esta hablando de algo ambiguo, las respuestas pueden ser erroneas, por lo que deberia ser checkeado antes de lanzar el mensaje
	- En el proceso de traducir es algo bastante parecido pero identificando que las palabras que fueron buscadas esten en el idioma ingles, logrando una mejor traduccion


2.- ¿Cómo se podría combinar las pruebas unitarias con Docker?
	
	se podrian combinar en los procesos que realizan resultados constantes, de esta manera aseguramos que las respuestas siempre esten correctas
	algunos ejemplos son como los dichos en la pregunta 1.