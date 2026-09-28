# Examen

## Alumna: Michelle Cámara González

---

### 1. Explica dos diferencias entre una API REST y un servidor GraphQL.

| API REST                                        | GraphQL                                                |
| ----------------------------------------------- | ------------------------------------------------------ |
| 1. Usa varios métodos HTTP para cada recurso.   | 1. Utiliza una solo endpoint para todas las peticiones |
| 2. Tiende a sufrir overfetching u underfetching | 2. Permite pedir múltiples recursos en un solo método  |

### 2. Indica una situación en la que conviene usar REST y otra en la que conviene usar GraphQL

1. _REST_: Cuando quieres realizar un CRUD sencillo con recursos definidos como con el de las laptops. Y también para APIs públicas.

2. _GraphQL_: Cuando necesitas realizar consultas complejas con múltiples recursos y evitar el overfetching, como en aplicaciones móviles.

### 3. ¿Qué diferencia hay entre una imagen y un contenedor? ¿Qué papel cumple el Dockerfile en esa relación?

1. _Imagen_: Es una plantilla con el sistema base, Python las dependencias y el código. No se ejecuta por si misma.

2. _Contenedor_: Es la instancia de esa imagen. De una sola se pueden crear varios contenedores.

3. _Dockerfile_: Es la receta para construir la imagen, su relación es que el dockerfile se construye y da una imagen que se ejecuta y da un contenedor.

### 4. . ¿Para qué sirve Docker Compose? En el mapeo 8000:8000, ¿qué representa el primer 8000 y qué representa el segundo?

_Compose_ sirve para definir y levantar varios contenedores juntos desde un solo archivo. Configura sus variables, puertos, volúmenes y la red que comparten. Gracias a esa red, la API puede encontrar a MySQL.

_8000:8000_ es host:contenedor. El primer puerto es el de mi máquina y el segundo es dentro del contenedor donde escucha uvicorn.

### 5. ¿Por qué las laptops del ejercicio 1 se guardan en MySQL y no en una lista de Python? ¿Qué identifica la llave primaria id?

Se guardan en MySQL y no en una lista de Python porque una lista se pierde cuando se apaga el contenedor, mientras que en MySQL los datos se guardan en el disco. La llave primaria id identifica de manera única a cada laptop.
