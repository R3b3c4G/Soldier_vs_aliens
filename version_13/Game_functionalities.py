import pygame
from Configurations import Configurations
from Media import Background, GameOverImage,Scoreboard, Audio
from Soldier import Soldier
from Shot import Shot
from Alien import Alien
import time
from random import randint

"""CAMBIO. Ahora se considera un segundo soldado y sus disparos"""
def game_events(soldier: Soldier, gunshots: pygame.sprite.Group, soldier2: Soldier, gunshots2: pygame.sprite.Group, audio:Audio) -> bool:
    """
    Función que administra los eventos del juego.
    :param soldier: Objeto con el soldado (personaje del primer jugador).
    :param gunshots: Grupo que almacena los disparos del primer soldado.
    :param soldier2: Objeto con el soldado (personaje del segundo jugador).
    :param gunshots2: Grupo que almacena los disparos del segundo soldado.
    :return: La bandera de fin del juego.
    """
    # Se declara la bandera de fin del juego que se retorna.
    game_over = False

    # Se verifican los eventos (teclado y ratón) del juego.
    for event in pygame.event.get():
        # El evento es un clic para cerrar el juego.
        if event.type == pygame.QUIT:
            game_over = True

        # Se verifica el evento de presionar una tecla.
        if event.type == pygame.KEYDOWN:
            # Se verifica las flechas para el movimiento.
            if event.key == pygame.K_UP:
                soldier.is_moving_up = True

            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = True

            """CAMBIO. Ahora también se incluye la verificación de la cantidad de disparos."""
            # Si se presionó el espacio y la cantidad de disparos es menor al máximo posible, entonces se
            # crea un nuevo disparo y se agrega al grupo. Además, indica que el soldado está dis  parando.
            if event.key == pygame.K_SPACE and len(gunshots) < Configurations.get_max_gunshots():
                new_shot = Shot(soldier)
                gunshots.add(new_shot)
                soldier.shoots()
                audio.play_shoot_sound()


            """CAMBIO. Ahora se considera un segundo soldado."""
            # Controles para es segundo soldado.
            if event.key == pygame.K_q:
                soldier2.is_moving_up = True
            if event.key == pygame.K_a:
                soldier2.is_moving_down = True
            if event.key == pygame.K_d and len(gunshots2) < Configurations.get_max_gunshots():
                new_shot = Shot(soldier2)
                gunshots2.add(new_shot)
                soldier2.shoots()
                audio.play_shoot_sound()

        # Se verifica el evento de soltar una tecla.
        if event.type == pygame.KEYUP:
            # Se verifica las flechas para dejar de moverse.
            if event.key == pygame.K_UP:
                soldier.is_moving_up = False
            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = False

            """CAMBIO. Ahora se considera un segundo soldado."""
            if event.key == pygame.K_q:
                soldier2.is_moving_up = False
            if event.key == pygame.K_a:
                soldier2.is_moving_down = False

    # Se regresa la bandera.
    return game_over

"""CAMBIO. Ahora se considera un segundo soldado y sus disparos."""
def handle_movement(screen: pygame.surface.Surface,
                    soldier: Soldier, gunshots: pygame.sprite.Group,soldier2: Soldier,
                    gunshots2: pygame.sprite.Group, aliens: pygame.sprite.Group) -> None:
    """
    Función que administra los movimientos.
    :param screen: Objeto con la pantalla.
    :param soldier: Objeto con el soldado (personaje del primer jugador).
    :param gunshots: Grupo que almacena los disparos del primer soldado.
    :param soldier2: Objeto con el soldado (personaje del segundo jugador).
    :param gunshots2: Grupo que almacena los disparos del segundo soldado.
    :param aliens: Grupo que almacena los aliens.
    """
    # Se actualiza la posición del soldado.
    soldier.update_position(screen)
    # Se actualizan las posiciones de los disparos del soldado.
    for shot in gunshots.sprites():
        shot.update_position()

    """CAMBIO. Ahora se considera un segundo soldado."""
    soldier2.update_position(screen)
    for shot in gunshots2.sprites():
        shot.update_position()

    # Se actualizan las posiciones de los aliens.
    for alien in aliens.sprites():
        alien.update_position(screen)


def check_collisions(screen: pygame.surface.Surface,
                    soldier: Soldier, gunshots: pygame.sprite.Group, soldier2: Soldier, gunshots2: pygame.sprite.Group,
                     aliens: pygame.sprite.Group, scoreboard:Scoreboard, scoreboard2:Scoreboard ) -> bool:
    """
    Función que revisa las colisiones en el juego: disparos del soldado - aliens, disparos del soldado - borde
    izquierdo de la pantalla, aliens - borde derecho de la pantalla, aliens - soldado.
    :param screen: Objeto con la pantalla.
    :param soldier: Objeto con el soldado (personaje del primer jugador).
    :param gunshots: Grupo que almacena los disparos del primer soldado.
    :param soldier2: Objeto con el soldado (personaje del segundo jugador).
    :param gunshots2: Grupo que almacena los disparos del segundo soldado.
    :param aliens: Grupo que almacena los aliens.
    :param scoreboard: El marcador.
    :param scoreboard2: El marcador2.
    :return: La bandera de fin del juego.
    """
    # Se declaran variables que se utilizan en la función.
    game_over = False                   # Bandera de fin del juego que se retorna.
    screen_rect = screen.get_rect()     # Se obtiene el rectángulo de la pantalla.

    # Se obtienen las colisiones entre los alies - soldado.
    aliens_soldier_collisions = pygame.sprite.spritecollide(soldier, aliens, dokill=False)
    if len(aliens_soldier_collisions)  > 0:
        game_over = True
        return game_over

    """CAMBIO. Ahora se considera un segundo soldado."""
    # Se obtienen las colisiones entre los aliens y el segundo soldado.
    aliens_soldier2_collisions = pygame.sprite.spritecollide(soldier2, aliens, dokill=False)
    if len(aliens_soldier2_collisions) > 0:
        game_over = True
        return game_over

    # Se obtienen las colisiones entre los disparos del soldado - aliens.
    gunshots_aliens_collisions = pygame.sprite.groupcollide(gunshots, aliens, True, True)
    if len(gunshots_aliens_collisions) > 0:
        scoreboard.points = scoreboard.points+1
        scoreboard.update(scoreboard.points)
        print("Alien eliminado 💣👽!!!")

    """CAMBIO. Ahora se considera un segundo soldado."""
    gunshots2_aliens_collisions = pygame.sprite.groupcollide(gunshots2, aliens, True, True)
    if len(gunshots2_aliens_collisions) > 0:
        scoreboard2.points = scoreboard2.points+1
        scoreboard2.update(scoreboard2.points)
        print("Alien eliminado por el jugador 2 💥👽")

    # Se revisan las colisiones entre los disparos del soldado - borde izquierdo de la pantalla.
    for shot in gunshots.copy():
        if shot.rect.right < screen_rect.left:
            gunshots.remove(shot)

    # Se revisan las colisiones entre los aliens - borde derecho de la pantalla.
    for alien in aliens.copy():
        if alien.rect.left > screen_rect.right:
            aliens.remove(alien)

    # Se agregan más enemigos si hay menos de la cantidad mínima.
    min_aliens = Configurations.get_min_aliens()
    if len(aliens) <= min_aliens:
        aliens_to_spawn = randint(1, min_aliens)
        for _ in range(aliens_to_spawn):
            alien = Alien()
            aliens.add(alien)

    # Se regresa la bandera.
    return game_over

"""CAMBIO. Ahora se considera un segundo soldado y sus disparos."""
def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock,
                   background: Background,
                   soldier: Soldier,
                   gunshots: pygame.sprite.Group,
                    soldier2: Soldier,
                    gunshots2: pygame.sprite.Group,
                   aliens: pygame.sprite.Group,
                   scoreboard:Scoreboard,
                   scoreboard2:Scoreboard) -> None:
    """
    Función que administra los elementos de la pantalla.
    :param screen: Objeto con la pantalla.
    :param clock: Objeto con el reloj del videojuego.
    :param background: Objeto con el fondo de pantalla.
    :param soldier: Objeto con el soldado (personaje del primer jugador).
    :param gunshots: Grupo que almacena los disparos del primer soldado.
    :param soldier2: Objeto con el soldado (personaje del segundo jugador).
    :param gunshots2: Grupo que almacena los disparos del segundo soldado.
    :param aliens: Grupo que almacena los aliens.
    :param scoreboard: Objeto que gestiona la puntuación y su visualización.
    """
    # Se dibuja el fondo de la pantalla.
    background.blit(screen)

    # Se anima y se dibuja el soldado en la pantalla.
    soldier.update_animation()
    soldier.blit(screen)
    #Se dibuja scoreboard
    scoreboard.blit(screen)
    scoreboard2.text = "J2 Mata mas que el J1 !!!!!!!"
    scoreboard2.blit(screen)


    # Se animan y se dibujan los disparos del soldado.
    for shot in gunshots.sprites():
        shot.update_animation()
        shot.blit(screen)


    """CAMBIO. Ahora se considera un segundo soldado."""
    soldier2.update_animation()
    soldier2.blit(screen)

    for shot in gunshots2.sprites():
        shot.update_animation()
        shot.blit(screen)

    # Se animan y se dibujan los aliens.
    for alien in aliens.sprites():
        alien.update_animation()
        alien.blit(screen)

    # Se actualiza la pantalla, dando la impresión de movimiento.
    pygame.display.flip()

    # Se controla la velocidad de fotogramas (FPS) del videojuego.
    clock.tick(Configurations.get_fps())

"""CAMBIO."""
def game_over_screen(screen, audio:Audio, scoreboard: Scoreboard, scoreboard2: Scoreboard) -> None:
    """
    Función con la pantalla del fin del juego y el score final.

    """

    audio.music_fadeout(time = Configurations.get_music_fadeout_time())
    audio.play_game_over()

    game_over_image = GameOverImage()
    game_over_image.blit(screen)

    """NUEVO."""
    # Calcular el score total.
    total_score = scoreboard.points + scoreboard2.points
    final_score = f"Score final del equipo: {total_score} aliens eliminados"

    font = pygame.font.SysFont("kilmono", 45)
    text_color = (255, 255, 255)
    results = font.render(final_score, True, text_color)

    screen.blit(results, (10,10))

    # Se agrega una pausa para que el usuario se dé cuenta de que ha perdido.
    pygame.display.flip()
    time.sleep(Configurations.get_game_over_screen_time())
