
import pygame

from Soldier import Soldier
from  Media import  Background

def game_events ( ) -> bool:
    """
    Funcion que administra los eventos del juego
    :return: La bandera del fin del juego

    """

    game_over = False
    # Verificacion de eventos (tecleado, clic y raton) del juego.
    for event in pygame.event.get():
        # Un clic en cerrar juego:
        if event.type == pygame.QUIT:
            game_over = True
     # Retorna bandera
    return  game_over

def screen_refresh(screen: pygame.surface.Surface, background: Background, soldier: Soldier)->None:
    """
    Funcion que administra los elementos visuales.
    :return:
    """
    # Se dibujam elementos graficos en pantalla:
    # Se rellena el objeto pantalla
    #screen.fill(Configurations.get_background())
    background.blit(screen)

    soldier.blit(screen)


    # Actualizar pantalla
    pygame.display.flip()