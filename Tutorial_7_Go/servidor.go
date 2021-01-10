    package main
    import (
      "fmt" // paquete de salida
      "net/http" // paquete para las peticiones HTTP 
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
