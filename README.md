# Examen-I

Trabajo grupal 1
--Guia para conocer de Git Hub--

Comandos básicos de GIT

git config
Uno de los comandos más usados en git es git config, que puede ser usado para establecer una configuración específica de usuario, como sería el caso del email, un algoritmo preferido para diff, nombre de usuario y tipo de formato, etc… Por ejemplo, el siguiente comando se usa para establecer un email:
git config --global user.email sam@google.com

git init
Este comando se usa para crear un nuevo repertorio GIT:
git init

git add
Este comando puede ser usado para agregar archivos al index. Por ejemplo, el siguiente comando agrega un nombre de archivo temp.txt en el directorio local del index:
git add temp.txt

git clone
Este comando se usa con el propósito de revisar repertorios. Si el repertorio está en un servidor remoto se tiene que usar el siguiente comando:
git clone alex@93.188.160.58:/path/to/repository
Pero si estás por crear una copia local funcional del repertorio, usa el comando:

     git clone /path/to/repository

git commit
El comando commit es usado para cambiar a la cabecera. Ten en cuenta que cualquier cambio comprometido no afectara al repertorio remoto. Usa el comando:
git commit –m “Message to go with the commit here”

git status
Este comando muestra la lista de los archivos que se han cambiado junto con los archivos que están por ser añadidos o comprometidos.
git status

git push
Este es uno de los comandos más básicos. Un simple push envía los cambios que se han hecho en la rama principal de los repertorios remotos que están asociados con el directorio que está trabajando. Por ejemplo:
git push  origin master

git checkout
El comando checkout se puede usar para crear ramas o cambiar entre ellas. Por ejemplo, el siguiente comando crea una nueva y se cambia a ella:
command git checkout -b <banch-name>
Para cambiar de una rama a otra solo usa:

git checkout <branch-name>
git remote
El comando git se usa para conectar a un repositorio remoto. El siguiente comando muestra los repositorios remotos que están configurados actualmente:
git remote -v
Este comando te permite conectar al usuario con el repositorio local a un servidor remoto:

git remote add origin <93.188.160.58>

git branch
Este comando se usa para listar, crear o borrar ramas. Para listar todas las ramas se usa:
git branch

para borrar la rama:

git branch -d <branch-name>

git pull
Para poder fusionar todos los cambios que se han hecho en el repositorio local trabajando, el comando que se usa es:
git pull

git merge
Este comando se usa para fusionar una rama con otra rama activa:
git merge <branch-name>
