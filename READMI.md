# Python: Pasos para crear un juego con ayuda de la libreira PyGame

#### Primero debemos realizar las importaciones de las diferentes librerias a utilizar

##### 1. pygame: podemos utilizas varios objetos, traer y mostrar imagenes, audios...

##### 2. random: tomar elementos aleatorios de un arreglo

##### 3. math: deja tener acceso a funciones matemáticas

##### 4. sys: accede a variables y funciones

##### 5. os: proporciona y expone los detalles y la funcionalidad del sistema operativo

#### Segundo iniciamos PyGame

#### Tercero con ayuda pygame/display.set_mode establecemos

##### Código a utilizar:` screen = pygame.display.set_mode((screen_width, screen_height))`

##### - el ancho (width)

##### - el alto (height)

##### - el formato de color (RGB) si deseamos en dado caso

##### - el tamaño de ventana (fullscreen=True o False)

##### Establecemos el título del juego con ayuda de:

##### Código a utilizar: `Código a utilizar: pygame.display.set_caption("Pygame - Fire Game")`

##### Es importante ccrear la función para rutear los archivos y poderlos cargar adecuadamente

##### Se cargar cada uno de los elementos a utilizar en el juego

##### - Fondo del juego

##### - sonido del juego

##### - Icono de la ventana

##### - Imagen del jugador

##### - Imagende la bala

##### - Imagen del enemigo

#### Cuarto definimos una variable que nos permita controlar el bucle principal del juego

#### Quinto creamos dos clases: Player y Enemy

##### Clase Player:

##### - Debe contener posicion x e y

##### - Debe contener velocidad x e y

##### - Debe ser capaz de moverse por pantalla

##### - Debe ser capaz de disparar balas

##### - Debe ser capaz de colisionarse con enemigos

##### Clase Enemy:

##### - Debe contener posicion x e y

##### - Debe contener velocidad x e y

##### - Debe ser capaz de moverse por pantalla

##### - Debe ser capaz de colisionarse con jugador

##### - Debe ser capaz de disparar balas

##### Se establece el score para que valla sumando el mostrando en pantalla los puntajes, nos apoyamos por medio de la siguiente función

`def show_score():`
`score_value = font.render("Score "+ str(score), True, (255, 255, 255))`
`screen.blit(score_value, (10, 10))`

##### Importante establecer la función que nos determina si el juego a acabo "Game over" para ello realizamos la función que nos ayuda a determinar esta situación

`def game_over(): large_text = font.render("Game Over", True, (255, 255, 255)) ...`

#### Función principal del juego

##### En esta función se inicia declarando las variables globales a utilizar dentro de ella

##### También se declara un While el cuál es el bucle principal de la función

##### Se comprueba si el jugador ha perdido o ganado el juego

##### Si no ha perdido ni ganado, se actualizan los valores de la posición del jugador y sus balas

##### Se dibujan todos los elementos en pantalla

##### Se establece los movimientos a partir del teclado

##### Se llama la variable y función de colisiones para que se haga efectivo este movimiento y se articule con el score

##### Se llama a la función show_score para mostrar el score en pantalla

##### y por último geneerar el reloj o tiempo de juego, posteriormente llamar la función princial

##### Función principal `gamepy()` cerramos con esta indicación, probar y corregir posibles errores
