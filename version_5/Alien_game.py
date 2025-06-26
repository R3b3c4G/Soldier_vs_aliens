"""
Nombre:      Héctor Jesús Méndez
Fecha:       21/05/2025
Descripcion: Se agregan nuevos archivos en el proyecto para mejorar la organizacion de codigo.
             Se reemlaza codigo duro

Version 0.2:
"""
#Importar modulos para videojuego
import pygame
from pygame.sprite import Group

from Soldier import Soldier
from Media import Background
from game_funtionalities import game_events, screen_refresh
from Configurations import Configurations
from Shot import Shot



def run_game() -> None:
    """
    Funcion principal del videojuego.
    :return: No retorna nada
    """
    #Inicializar modulo o recursos
    pygame.init()
    #Se crea reloj
    clock = pygame.time.Clock()

    #Iniciarlizar pantalla
    screen_size =  Configurations.get_screen_size()    #Resolucion pantalla (ancho, alto)
    screen = pygame.display.set_mode(screen_size)

    #Configurar titulo de juego.
    game_title = Configurations.get_game_title()
    pygame.display.set_caption(game_title)

    #Se crea objeto Backgraund:
    background = Background()
    #Se crea objeto Soldado
    soldier = Soldier(screen)
    #Se crea disparo y grupo de disparos
    shots = Group()




    #Ciclo principal de juego:
    game_over = False
    while not game_over:
        #Verificacion de eventos (tecleado, clic y raton) del juego.
        game_over = game_events(soldier, shots, screen)
        # Se dibujan elementos graficos en pantalla:
        screen_refresh(screen, background, soldier, clock, shots)
    #Cerrar recursos.
    pygame.quit()

if __name__ == '__main__':
    run_game()