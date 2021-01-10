# Tutorial_8_R-Studio

# ¿Que es R y R-Studio?

R es un entorno y lenguaje de programación con un enfoque al análisis estadístico.
Este lenguaje es unos de los mas utilizados en la investigacion cientifica, gracias a su gran cantidad de bibliotecas que aportan mayor facilidad a resolucion de problemas ya que con sus diferentes bibliotecas puedes solucionar diferentes problemas estadisticos, matematicos, cientificos, etc.
R-Studio por su parte es un entorno de desarrollo integrado por el lenguaje de programación R, centrado a la computación estadística y gráficos, eso permite analisis y desarrollos para cualquier tipo de dato que presente R.


# La instalacion de R-Studio (Windows)


Para la instalacion del programa R :

Entraremos a la pagina https://www.r-project.org, en esta parte iremos a CRAN, donde encontraremos una variedad grande de redes de archivos de diferentes paises, por nuestra condicion de vivir en chile se elige Departamento de Ciencias de la Computación de la Universidad de Chile.

Clickeamos Windows y luego install

Al tener instalado R, descargaremos R-Studio desde la pagina https://rstudio.com/products/rstudio/download/#download

Al descargar R-studio ejecutamos el instalador y seguiremos los pasos hasta terminar, luego de esto se puede utilizar R Studio.


## Utilizando R-Sutdio Muestra de Graficos (Comando plot)


¿Como realizar una Muestra de Graficos (Comando plot)?

La función plot en R permite crear un gráfico pasando dos vectores con la misma longitud, un data frame, una matriz o incluso otros objetos, con esto dicho decimos que los graficos dependen de su clase o tipo de los datos de entrada.

Algunos ejemplos son del uso del comando plot son:

plot(x, y): Diagrama de dispersión de los vectores numéricos x e y
plot(factor): Gráfico de barras del factor
plot(factor, y): Diagrama de caja del vector numérico y los niveles del factor
plot(serie_temporal): Gráfico de una serie de tiempo (clase ts)
plot(data_frame): Gráfico de correlación de todas las columnas del data frame (más de dos columnas)
plot(fecha, y): Traza un vector basado en fechas
plot(función, inferior, superior):Traza la función entre el valor inferior y máximo especificado

Por ejemplo simularemos dos variables normales aleatorias llamadas x e y de la manera (Trabajo en consola):

	# Generamos datos de ejemplo 
	# Se crean 500 datos aleatorios
	x <- rnorm(500)
	y <- x + rnorm(500)

Al utilizar el comando plot de la forma plot(x,y) se generara un grafico con el diagrama de dispersión de los vectores numéricos x e y
al utilizar plot(x, y, main = "Gráfico de dispersión") se nos generara el mismo grafico pero con el titulo Grafico de dispersión.

Tambien el comando plot te permite cambiar el color de las variables , el nombre de los factores x e y , entre otras opciones para una presentacion del grafico mas ordenada(Esto aplica para todos lo graficos).
