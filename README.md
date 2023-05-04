# Paso 1:
Debes comprender la estructura de las carpetas: 
1. Folder "in": En está carpeta encontras la data del modelo. 
2. Folder out: El resultado del modelo (gráficas, predicción, etc)
3. Folder models: El modelo mismo (mejores modelos)

# Paso 2:
Crear un entorno virtual para MacOs. En caso de tenr linux o windows. Podrás agregar los pasos a este README.md
1. python3 -m venv venv
2. source venv/bin/activate

# Paso 3:
Crear las carpetas (in, out and models), con los comandos:
mkdir "nombre_folder"

# Paso 4:
Crear un archivo .gitignore
Y agrega los archivos que tu consideres que no debes de compartir por tu seguridad.

# Paso 5: 
Entender el actuar de cada un archivo. ¿Por qué se hace esto? Buscamos que cada archivo (con apoyo del OOP) tenga el control del flujo y se haga cargo de 1 tarea en concreto. 

1. main.py: Este archivo se creará en la raíz de la carpeta. 
    a. Esté archivo será el método de ejecución principal.
    b. Flujo del modelo de principio a fin.

2. load.py: Carga de los elementos. 

3. utils.py: Todos los métodos a reutilizar en todo el proceso. ¿Por qué buscamos eso? Evitamos mezclar ese código con el de la ejecución. Y sobre todo si el modelo llegará a tener diferentes tipos de archivos (csv, json, base64) podríamos generar diferentes funciones que puedan leer este tipo de data, sin necesidad de cambiar o romper el código:
    a. Cargar y leer Data.
    b. Leer diferentes tipos de archivos (csv, json, etc)
    c. Conectarse a una BBDD de remota.
ejem: Leer archivo

4. models.py: En este archivo tendremos todo el código de ML