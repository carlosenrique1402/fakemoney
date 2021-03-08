
Para iniciar a trabajar con el repositorio, hay que hacer un fork con github, clonar su repositorio y solicitar un pull request cuando terminen de realizar sus cambios.
  - ¿Qué es un **Fork**? En el ámbito del desarrollo de software, es la creación de un proyecto en una dirección distinta de la principal u oficial tomando el código fuente del proyecto ya existente.
  - ¿Cómo trabajar con **Fork**? En la parte superior derecha del repositorio principal se encuentra un botón **Fork** que hay que presionar.
  - Para poder continúar, debemos estar autenticados en la plataforma **GitHub**.
  - Una vez que se creo el **Fork**, nos dirijimos a **Mis repositorios** ubicados en perfil y damos click en el repositorio.
  - A continuación hay un botón en la parte superior derecha de color verde, hacemos click para que muestre las opciones y copiamos el link para crear el repositorio con **HTTPS**.
  - Dentro de una terminal de **git-bash** ejecutaremos la siguiente línea de comando para clonar el repositorio:
  - `git clone {URL}`


**NOTA**:
!Es importante estar dentro del repositorio fakemoney para correr los comandos o rutas!

Para mantener sus _branch_ al día con el proyecto principal es útil ejecutar las siguientes líneas en la terminal de git. 

Esta línea les permitirá observar los cambios que se realicen en el branch principal.
```
git remote add profe https://github.com/ekiim/fakemoney.git
```

Después lo que deberán hacer para obtener los cambios mas recientes en la rama principal.

```
git pull profe main
```

---

Cuando tengas listos los cambios, y desees actualizar tu sitio de github, realizar un `push`

```
git push
```

Asi sus cambios se veran reflejados en su pagina de github, `https://github.com/{nombre de usuario}/fakemoney`

```
git status
```
El comando git status muestra el estado del directorio de trabajo y del área del entorno de ensayo. Permite ver los cambios que se han preparado, los que no y los archivos en los que Git no va a realizar el seguimiento.

### Clonacion del proyecto

Para poder copiar el proyecto fakemoney, primetamente debemos:

  - En la pagina de GitHub `https://github.com/ekiim/fakemoney` debos clickear el cuadro pequeño llamado **Fork**
(El proyecto se fakemoney se ha copiado a nuestro repositorio)

  - Ubicandonos en nuestro repositorio debemos entrar al del proyecto **ejem**`https://github.com/NombreDeUsuario/fakemoney`
En el boton **Code** nos mostrara nuestro link **ejem** `https://github.com/NombreDeUsuario/fakemoney.git`

En Git bash accederemos a la ruta de documentos para clonar ahi nuestra copia del proyecto
```
cd Documents/
```
Dentro de la ruta clonaremos el proyecto, utilizando nuestro propio link
```
git clone https://github.com/NombreDeUsuario/fakemoney.git
```
Para veficar estos pasos entraremos a la ruta del proyeto y mostraremos los documentos dentro de el
```
cd fakemoney/
ls
```
### COMO ACTUALIZAR TU REPOSITORIO
Para actualizar los cambios recientes del proyecyo
Entrar a la ruta de documentos o donde se haya descargado el proyecto
````
cd Documents/
````
Despues entraremos a la ruta del proyecto
```
cd fakemoney/
```
Ahora podremos actualizar el **REPOSITORIO** Aqui se descargaran las actualizaciones del proyecto
```
git pull profe main
```
Ahora se deben agregar esas actualizaciones a tu repositorio
```
git push
```
### Cambiar de editor de texto a NANO.

Nano es un editor de texto visual para la terminal.

Si deseas cambiar de editor de texto para los mensajes de `commit`, y utilizar NANO como editor de texto principal (para git).

Uno puede ejecutar la siguiente linea.

```
git config --global core.editor "nano"
```

### Evitar conflictos contra la rama principal.

Si presento confictos con la rama principal una manera de resolverlos es hacer un `git rebase`.

Para configurar que los `git pull` por default se comporten como un `rebase`, hay que ejecutar la siguiente linea.

```
git config --global pull.rebase true
```

De aqui en adelante uno puede ejecutar 

```
git pull profe main
```

Para traer a su rama actual los cambios que se presentan en la rama principal `ekiim:main`.

Cuando se tenga un conflicto entrarán en modo `rebase`, donde tendrán que editar los archivos para conciliar los cambios, y borraran lo no deseado.

Una vez concluida la fase de conciliación de cambios ejecutamos `git add` para informarle a `git` de esto, y ejecutamos un `git rebase --continue`.



