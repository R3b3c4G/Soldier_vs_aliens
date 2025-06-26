"""
Nombre:      Héctor Jesús Méndez
Fecha:       21/05/2025
Descripcion: -Se crea el sistema de control principal del juego
             -Se crean la pantalla de inicioo
             -Se configura titulo
Version 0.1:
"""

#Importar modulos para videojuego
import pygame

def run_game() -> None:
    """
    Funcion principal del videojuego.
    :return:
    """
    #Inicializar modulo o recursos
    pygame.init()

    #Iniciarlizar pantalla

    screen_size = (1280, 720)       #Resolucion pantalla (ancho, alto)
    screen = pygame.display.set_mode(screen_size)

    #Configurar titulo de juego.
    game_title = "Alien Game de Me'Sant"
    pygame.display.set_caption(game_title)

    #Ciclo principal de juego:
    game_over = False
    while not game_over:
        #Verificacion de eventos (tecleado, clic y raton) del juego.
        for event in pygame.event.get():
            #Un clic en cerrar juego:
            if event.type == pygame.QUIT:
                game_over = True

        # Se dibujam elementos graficos en pantalla:
        background = (28, 30, 50)   #Fondo de pantalla en rgb de 0 a 255
        #Se rellena el objeto pantalla
        screen.fill(background)

        #Actualizar pantalla
        pygame.display.flip()
    #Cerrar recursos.
    pygame.quit()

if __name__ == '__main__':
    run_game()