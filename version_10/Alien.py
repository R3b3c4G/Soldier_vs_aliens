import pygame
from pygame.sprite import Sprite
from random import choice, uniform, randint
from Configurations import Configurations

class Alien(Sprite):
    """
    Clase que representa un alien.
    Hereda de la clase Sprite para utilizar grupos de sprites y detectar colisiones entre sprites.
    Sus atributos son: image (apariencia), rect (posición y tamaño). Además, tiene una lista con los frames
                       para el movimiento y la animación, así como los atributos requeridos para tal fin.
    Sus métodos son: blit() (dibujar), update_position (para el movimiento) y update_animation (para la animación).
    """


    def __init__(self):
        """
        Constructor del alien, en donde se llama al constructor padre de Sprite.
        """
        # Se llama al constructor de la clase padre.
        super().__init__()

        # Lista que almacena los frames del alien.
        self._frames = []

        # Se cargan las hojas que contienen los aliens, se selecciona aleatoriamente una de ellas
        # para cargar los frames del alien.
        sheets_path = Configurations.get_alien_sheets_path()
        sheet_path = choice(sheets_path)
        alien_sheet = pygame.image.load(sheet_path)

        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_alien_frames_per_row()
        sheet_width = alien_sheet.get_width()
        sheet_height = alien_sheet.get_height()
        alien_frame_width = sheet_width // sheet_frames_per_row
        alien_frame_height = sheet_height

        # Se obtiene el tamaño para escalar cada frame.
        alien_frame_size = Configurations.get_alien_size()

        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        for i in range(sheet_frames_per_row):
            x = i * alien_frame_width
            y = 0
            subsurface_rect = (x, y, alien_frame_width, alien_frame_height)
            frame = alien_sheet.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, alien_frame_size)

            self._frames.append(frame)

        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()    # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = randint(0,sheet_frames_per_row - 2)     # Índice inicial aleatorio de la lista.

        # Se selecciona la primera imagen a mostrar de manera aleatoria.
        self.image = self._frames[self._frame_index]
        self._frame_index+= 1

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        # Se actualiza la posición inicial aleatoriamente, considerando que no se vea en la pantalla.
        screen_height = Configurations.get_screen_size()[1]
        self.rect.y = alien_frame_height * randint(0, (screen_height // alien_frame_height - 1))
        self.rect.x = -alien_frame_width

        # Banderas de movimiento en Y. Se elige aleatoriamente la dirección inicial.
        self._is_moving_up = choice([True, False])
        self._is_moving_down = not self._is_moving_up

        # Se incluyen los atributos para el movimiento.
        self._rect_x = float(self.rect.x)
        self._speed_x = Configurations.get_alien_speed_x() * uniform(0.6, 1.4)
        self._rect_y = float(self.rect.y)
        self._speed_y = Configurations.get_alien_speed_y() * uniform(0.65,1.35)


    def update_position(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para actualizar la posición del alien de acuerdo a las banderas de movimiento.
        """
        # Se obtiene el rectángulo del borde de la pantalla.
        screen_rect = screen.get_rect()

        # Se actualiza la posición en X del valor flotante de la posición.
        self._rect_x += self._speed_x

        # Se verifican los estados de la bandera para modificar la posición en Y.
        if self._is_moving_up:
            self._rect_y -= self._speed_y

        elif self._is_moving_down:
            self._rect_y += self._speed_y

        # Se verifica que el alien no sobrepase los bordes de la pantalla.
        # En caso verdadero, se conmutan las banderas de movimiento.
        if self._rect_y < float(screen_rect.top):
            self._rect_y = float(screen_rect.y)
            self._is_moving_up = False
            self._is_moving_down = True

        elif self._rect_y > (screen_rect.bottom - self.image.get_height()):
            self._rect_y = float(screen_rect.bottom - self.image.get_height())
            self._is_moving_up = True
            self._is_moving_down = False

        # Se actualiza la posición del rectángulo.
        self.rect.x = int(self._rect_x)
        self.rect.y = int(self._rect_y)


    def update_animation(self) -> None:
        """
        Se utiliza para actualizar el frame visible del alien, dando la impresión de animación.
        """
        # Se verifica si el tiempo transcurrido es mayor o igual al tiempo establecido para actualizar el frame.
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_alien_frame_delay()
        needs_refresh = (current_time - self._last_update_time) >= frame_delay

        if needs_refresh:
            # En caso verdadero, se actualiza el frame por el siguiente en la lista.
            # Además, se actualizan los atributos para resetear el tiempo y actualizar el índice.
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            # Finalmente, se verica si el índice ha recorrido todos los frames para volver al inicio de la lista.
            if self._frame_index >= len(self._frames):
                self._frame_index = 0


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el alien en la pantalla.
        :param screen: Pantalla en donde se dibuja el alien.
        """
        # Se dibuja sobre la pantalla.
        screen.blit(self.image, self.rect)
