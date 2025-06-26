# Se importan los módulos necesarios.
import pygame
from pygame.examples.music_drop_fade import volume

from Configurations import Configurations
from Game_functionalities import game_events, handle_movement, check_collisions, screen_refresh, game_over_screen     # CAMBIO.
from Media import Background, Scoreboard, Audio
from Soldier import Soldier
from pygame.sprite import Group
from Alien import Alien
from random import randint


def run_game() -> None:
    """
    Función principal del videojuego.
    """
    # Se inicializa el módulo de pygame y se realizan las configuraciones iniciales.
    pygame.init()
    screen_size = Configurations.get_screen_size()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()  # Se usa para controlar la velocidad de fotogramas (FPS).

    # Se configura el título de la ventana.
    game_title = Configurations.get_game_title()
    pygame.display.set_caption(game_title)

    # Se crea el objeto del fondo de pantalla.
    background = Background()

    # Se crea el objeto del soldado (personaje principal).
    soldier = Soldier(screen)

    # Se crea el grupo para almacenar los disparos del soldado.
    gunshots = Group()

    # Se crea el grupo para almacenar a los enemigos.
    aliens = Group()

    # Se crea el scoreboard
    scoreboard = Scoreboard()

    # Se reproduce la música y el sonido inicial.
    audio = Audio()
    audio.play_music(volume=Configurations.get_music_volume())
    audio.play_start_sound()



    # Se crea la flota inicial de enemigos.
    min_aliens = Configurations.get_min_aliens()
    aliens_to_spawn = min_aliens + randint(0, min_aliens)

    for _ in range(aliens_to_spawn):
        alien = Alien()
        aliens.add(alien)

    # Ciclo principal del videojuego.
    game_over = False
    while not game_over:
        # Función que administra los eventos del juego.
        game_over = game_events(soldier, gunshots, audio)

        """NUEVO."""
        # Si el usuario ha cerrado la ventana, entonces se termina el ciclo para cerrar los recursos de pygame.
        if game_over:
            break

        """REVISAR."""
        # Función que administra los movimientos.
        handle_movement(screen, soldier, gunshots, aliens)

        """NUEVO."""
        # Función que revisa las colisiones en el juego.
        game_over = check_collisions(screen, soldier, gunshots, aliens, scoreboard, audio)

        # Función que administra los elementos de la pantalla.
        screen_refresh(screen, clock, background, soldier, gunshots, aliens, scoreboard)

        """NUEVO."""
        # Si el usuario ha perdido la partida, entonces se llama a la función que muestra la pantalla
        # del fin del juego.
        if game_over:
            game_over_screen(screen, audio)

    # Cierra todos los recursos del módulo pygame.
    pygame.quit()



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    run_game()