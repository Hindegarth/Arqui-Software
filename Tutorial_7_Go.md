# Tutorial_7_Programacion_en_GO

# ¿Que es GO?

Go es un Lenguaje de programacion creado por Google, tiene reconocimiento por ser eficiente y sencillo de programar
Go es bastante versatil, sin embargo, la mayoria de proyectos se centran especialmente en los programas de redes y sistemas distribuidos
por lo que se le asocia como el lenguaje de la nube.



# La instalacion de programacion en Go 

Vamos a obtener una URL de tarball que se extrae de la pagina oficial
- $ curl -O https://dl.google.com/go/go1.12.1.linux-amd64.tar.gz

Luego con sha256sum verificamos el tarball
- $ sha256sum go1.12.1.linux-amd64.tar.gz

El cual nos dara un Output similar a este, pero con el detalle que el hash es el mismo
2a3fdabf665496a0db5f41ec6af7a9b15a49fbe71a85a50ca38b1f13a103aeec  **go1.12.1.linux-amd64.tar.gz**

Ahora extraeremos el archivo y lo instalamos en alguna direccion deseada, **/usr/local** tiende a ser la recomendada:
- $ sudo tar -xvf go1.12.1.linux-amd64.tar.gz -C **/usr/local**

Ahora protegeremos a Go, para que solo se pueda acceder con Root
sudo chown -R root:root /usr/local/go


## Creación del espacio de trabajo para Go

El espacio de trabajo de Go se dividen en dos secciones :
-  src: donde estan los archivos de origen de go que es escrito por el mismo Go, el cual el Go utiliza para el proceso de compilacion, aparte de esto puede contener repositorios de control de versiones, permitiendo tener los paquetes completos.

- bin: donde se ubican los ejecutables creados e instalados por Go

Para crear el espacio de trabajo utilizamos el siguiente comando donde tendremos las dos secciones principal creadas
- $ mkdir -p $HOME/go/{bin,src}

Con los siguientes comandos, estableceremos una variable de entorno local GOPATH esto sirve para indicarle al compilador, el codigo de fuente local que hemos hecho, aunque no es necesario en varios sitios se recomienda hacerlo de todas maneras.

- $ nano ~/.profile
- $ export GOPATH=$HOME/go
- $ export PATH=$PATH:$GOPATH/bin
- $ export PATH=$PATH:$GOPATH/bin:/usr/local/go/bin
- $ . ~/.profile   (Para actualizar)
- $ echo $PATH (Verificamos la actualizacion, si se inicia con root veremos, root/go/bin)

## Hello-World

Para crear un programa (en el directorio que usted quiera), crearemos un archivo **hello.go** donde escribiremos lo siguiente:


    package main
    
    import "fmt"
    
    func main() {
        fmt.Println("Hello, World!")
    }

ahora en la consola lo ejecutamos con:
- $ go run hello.go

## Usar Go web con peticiones http


Crearemos un servidor http, para esto tenemos que importar los paquetes escenciales y crear dos funciones donde una mostrara un mensaje en el servidor de HTTP y la otra lo bloqueara para que siga existiendo hasta que se finalice.

    package main
    import (
      "fmt"  // paquete de salida
      "net/http"   // paquete para las peticiones HTTP 
    )
    // Se encargara en manejar peticiones y da a una respuesta al servidor
    func manejador(w http.ResponseWriter, r *http.Request){  
      fmt.Fprintf(w,"Hola, %s, ¡este es el servidor!", r.URL.Path)
    }
    // el HandleFunc se encarga de las peticiones de la funcion manjeador
    // y el http.ListenAndServe, dejara el programa bloqueado 
    func main(){
      http.HandleFunc("/", manejador)
      fmt.Println("El servidor se encuentra en ejecución")
      http.ListenAndServe(":8080", nil)
    }

