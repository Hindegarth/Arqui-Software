# Generamos datos de ejemplo 
# Se crean 500 datos aleatorios
x <- rnorm(500)
y <- x + rnorm(500)
plot(x,y)
plot(x, y, main = "Gráfico de dispersión")