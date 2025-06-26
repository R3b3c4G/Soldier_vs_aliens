import pygame
from Configurations import Configurations
from Media import Background
from Soldier import Soldier
from Shot import Shot
"""NUEVO."""
from Alien import Alien
import time
from random import randint

def game_events(soldier: Soldier, gunshots: pygame.sprite.Group) -> bool:
    """
    Función que administra los eventos del juego.
    :param soldier: Objeto con el soldado (personaje principal).
    :param gunshots: Grupo que almacena los disparos del soldado.
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

        # Se verifica el evento de soltar una tecla.
        if event.type == pygame.KEYUP:
            # Se verifica las flechas para dejar de moverse.
            if event.key == pygame.K_UP:
                soldier.is_moving_up = False

            if event.key == pygame.K_DOWN:
                soldier.is_moving_down = False

    # Se regresa la bandera.
    return game_over


"""REVISAR."""
def handle_movement(screen: pygame.surface.Surface,
                    soldier: Soldier, gunshots: pygame.sprite.Group, aliens: pygame.sprite.Group) -> None:
    """
    Función que administra los movimientos.
    :param screen: Objeto con la pantalla.
    :param soldier: Objeto con el soldado (personaje principal).
    :param gunshots: Grupo que almacena los disparos del soldado.
    :param aliens: Grupo que almacena los aliens.
    """
    # Se actualiza la posición del soldado.
    soldier.update_position(screen)

    # Se actualizan las posiciones de los disparos del soldado.
    for shot in gunshots.sprites():
        shot.update_position()

    # Se actualizan las posiciones de los aliens.
    for alien in aliens.sprites():
        alien.update_position(screen)


"""NUEVO."""
def check_collisions(screen: pygame.surface.Surface,
                    soldier: Soldier, gunshots: pygame.sprite.Group, aliens: pygame.sprite.Group) -> bool:
    """
    Función que revisa las colisiones en el juego: disparos del soldado - aliens, disparos del soldado - borde
    izquierdo de la pantalla, aliens - borde derecho de la pantalla, aliens - soldado.
    :param screen: Objeto con la pantalla.
    :param soldier: Objeto con el soldado (personaje principal).
    :param gunshots: Grupo que almacena los disparos del soldado.
    :param aliens: Grupo que almacena los aliens.
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

    # Se obtienen las colisiones entre los disparos del soldado - aliens.
    gunshots_aliens_collisions = pygame.sprite.groupcollide(gunshots, aliens, True, True)
    if len(gunshots_aliens_collisions) > 0:
        print("Alien eliminado 💣👽!!!")

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


def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock,
                   background: Background,
                   soldier: Soldier,
                   gunshots: pygame.sprite.Group,
                   aliens: pygame.sprite.Group) -> None:
    """
    Función que administra los elementos de la pantalla.
    :param screen: Objeto con la pantalla.
    :param clock: Objeto con el reloj del videojuego.
    :param background: Objeto con el fondo de pantalla.
    :param soldier: Objeto con el soldado (personaje principal).
    :param gunshots: Grupo que almacena los disparos del soldado.
    :param aliens: Grupo que almacena los aliens.
    """
    # Se dibuja el fondo de la pantalla.
    background.blit(screen)

    # Se anima y se dibuja el soldado en la pantalla.
    soldier.update_animation()
    soldier.blit(screen)

    # Se animan y se dibujan los disparos del soldado.
    for shot in gunshots.sprites():
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


"""NUEVO."""
def game_over_screen() -> None:
    """
    Función con la pantalla del fin del juego.
    """
    # Se agrega una pausa para que el usuario se dé cuenta de que ha perdido.
    time.sleep(Configurations.get_game_over_screen_time())
