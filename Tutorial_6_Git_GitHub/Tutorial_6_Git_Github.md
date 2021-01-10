# Tutorial_6_Git_Github

# ¿Que es Git y Github?

Git es un software de control de versiones pensando en la eficiencia, la confiabilidad y compatibilidad del mantenimiento de versiones de aplicaciones cuando éstas tienen un gran número de archivos de
codigo fuente.
Github es un plataforma de desarrollo colaborativo en la cual la gente puede guardas sus proyectos utilizando el sistema de controles de versiones de Git. De esta manera la gente puede realizar codigos en conjunto, dado que los proyectos estan almacenados publicamente naturalmente.

# ¿Como utilizo Github?

Hay que recordar que lo que queremos para trabajar, es tener los proyectos unidos a un mismo lugar de tal manera que todas las personas que entren al repositorio puedan utilizar los archivos de la manera mas simple posible, por lo que lo mas importante es organizar bien el repositorio.

Para tener un mejor manejo en la utilizacion de Github, lo unico que necesitaremos es conocer los comandos mas importantes y utiles.

`git rm -r --cached` = Borra el caché de los archivos seguidos por **git add**, para actualizar el funcionamiento del archivo **.gitignore**

`git init` = Inicia localmente un repositorio Git, creando un subdirectorio .git que llevará registro de los metadatos necesarios para el funcionamiento.

`git clone url` = Crea una copia del repositorio especificado a través de su url en GitHub. Por detrás, realiza un **git init**, y copia los respectivos archivos dentro. Si se reemplaza la url por una dirección local de archivos, también crea una copia.

`git add .` = Agrega a seguimiento todos los archivos dentro del repositorio. Se utiliza generalmente con ayuda del archivo **.gitignore**, para así evitar seguir archivos que no son útiles de compartir, como librerías instaladas o archivos caché. Se puede reemplazar el punto por algún o algunos archivos específicos.

`git commit -am "mensaje"` = Prepara todos los archivos de trabajo para una entrega, que eventualmente puede ser subida al repositorio GitHub. La flag 'a' incluye los nuevos archivos añadidos con **git add**, y la flag 'm' permite entregar un mensaje relacionado al *commit*.

`git push <origin> <master>` = Envía finalmente un nuevo **commit** local al repositorio remoto en GitHub. **origin** y **master** pueden ser obviados, o reemplazados, siendo **origin** el destino, y **master** algun branch del repositorio.

`git push --all origin` = Sube todos los branch al repositorio remoto.

`git status` = Lista los archivos modificados, y los que no fueron incluídos por **add** o **commit**.

`git remote -v` = Lista los repositorios remotos configurados dentro del directorio de llamada.

`git remote add origin <server>` = Agrega un repositorio iniciado localmente al servidor especificado.

`git checkout -b <branch_name>` = Crea un nuevo branch, y lo selecciona como actual.

`git switch <branch_name>` = Selecciona el branch especificado como el actual.

`git branch` = Lista los branch disponibles, y muestra la actual.

`git branch -d <branch_name>` = Elimina el branch especificado.

`git push origin :<branch_name>` = Elimina el branch especificado del repositorio remoto.

`git pull` = Descarga (fetch) y combina (merge) cambios del repositorio remoto con el local.

`git merge <branch_name>` = Combina el branch especificado con el actual.

`git diff` = Permite ver todos los conflictos de combinación

`git diff --base <filename>` = Permite ver los conflictos respecto al archivo base.

`git diff <source> <target>` = Permite ver los conflictos entre la branch source y la target (destino).

`git checkout -- <filename>` = Permite revertir cambios respecto a los últimos archivos confirmados con **git add**.

`git fetch origin && git reset --hard origin/master` = Revierte todos los cambios efectuados, y se alínea con los archivos del repositorio remoto.

Con esto dicho, tenemos todos los comandos para poder establecer bien nuestro repositorio.
