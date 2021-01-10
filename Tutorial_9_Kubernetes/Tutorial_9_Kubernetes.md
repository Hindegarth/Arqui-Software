# Tutorial_9_Kubernetes

# ¿Que es Kubernetes?

Kubernetes es una plataforma de código abierto para automatizar la implementación, el escalado y la administración de aplicaciones en contenedores, usualmente en Docker.

En Kubernetes se utiliza la api API de Kubernetes para describir el estado deseado del clúster: qué aplicaciones u otras cargas de trabajo se quieren ejecutar, qué imagenes de contenedores usan, el número de replicas,etc.

Una vez que se especifica el estado deseado, el Plano de Control de Kubernetes realizará las acciones necesarias para que el estado actual del clúster coincida con el estado deseado. Para ello, Kubernetes realiza diferentes tareas de forma automática, como pueden ser: parar o arrancar contenedores, escalar el número de réplicas de una aplicación dada, etc.

# Instalacion de Kubernetes

Para poder instalar Kubernetes primero descagaremos desde su pagina
```
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
```
Habilitaremos los permisos de ejecución del binario kubectl
```
    chmod +x ./kubectl
```

Moveremos el kubectl dentro de del PATH.
```
    sudo mv ./kubectl /usr/local/bin/kubectl
```

Ahora hay que Instalar mediante gestor de paquetes en el siguiente orden:
```
    sudo apt-get update && sudo apt-get install -y apt-transport-https gnupg2 curl
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
    sudo apt-get update
    sudo apt-get install -y kubectl
```
Por ultimo ahora Instalaremos el minikube para manejar los cluster de forma local
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
# Realizar los Minekube

Ahora realizaremos un cluster, para empezar necesitamos activar el cluester local con el siguiente comando
```
minikube start
```
Los Deployments son la manera recomendada de manejar la creación y escalación.
Para crear un Deployment necesitamos saber que un pod es un conjunto de uno o mas contenedores, y que al hacer un deployment verifica el estado del pod y reinicia el contendor si es que este fuera eliminado

Al ejecutar el comando **kubectl create** para crear un Deployment que maneje un Pod. El Pod ejecuta un contenedor basado en la imagen proveida por Docker
```
kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4
```
Ahora obtendremos el Deployment, pod y los eventos de clúster, respectivamente.
```
kubectl get deployments
kubectl get pods
kubectl get events
```

Por ultimo crearemos el service, el Pod es accedido por su dirección IP interna dentro del clúster de Kubernetes, para hacer que el contenedor hello-node sea accesible desde afuera de la red virtual Kubernetes, se debe exponer el Pod como un Service de Kubernetes.

Expondremos el Pod a la red de internter con **kubectl expose**, luego obtendremos el service que creamos para poder ejecutarlo.

```
kubectl expose deployment hello-node --type=LoadBalancer --port=8080
kubectl get services
```
Ejecucion:
```
minikube service hello-node
```

Para poder eliminar los recursos creados en el clúster, utilizaremos lo siguiente, en el orden respectivo.
```
#para elminiar los servicios creados
kubectl delete service hello-node

#para eliminar los deployments creados
kubectl delete deployment hello-node

#denener la maquna virtual que se creo al principio
minikube stop

#eliminar la maquina virtual
minikube delete

```

