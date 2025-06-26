import pygame
from pygame.sprite import Sprite
from Configurations import Configurations
from Soldier import  Soldier


class Shot(Sprite):
    def __init__(self, screen, soldier:Soldier):
        super().__init__()
        self._is_create_shot = False

        #Se genera lista para almacenar frames:
        self._frames = []
        #Aqui se carga la hoja de imagenes:
        shet_path = Configurations.get_shot_sheet_path()
        shot_sheet = pygame.image.load(shet_path)

        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_width = shot_sheet.get_width()
        sheet_height = shot_sheet.get_height()
        soldier_frame_width = sheet_width // sheet_frames_per_row
        soldier_frame_height = sheet_height

        # Se obtiene el tamaño para escalar cada frame.
        shot_frame_size = Configurations.get_shot_size()

        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        for i in range(sheet_frames_per_row):
            x = i * soldier_frame_width
            y = 0
            subsurface_rect = (x, y, soldier_frame_width, soldier_frame_height)
            frame = shot_sheet.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, shot_frame_size)

            self._frames.append(frame)


        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()  # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0  # Índice de la lista.


        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        #Posicion
        self.rect.right = soldier.soldier_rect.right-125    #Quitar codigo duro
        self.rect.centery = soldier.soldier_rect.centery -14


        # Se incluyen los atributos para el movimiento.
        self._rect_y = float(self.rect.x)
        self._speed = Configurations.get_soldier_speed()  #Cambiar valor independiente


    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza pra dibujar el fondo.
        :param screen:
        :return:
        """
        screen.blit(self.image, self.rect)

    def update_animation(self) -> None:
        """
        Se utiliza para actualizar el frame visible del soldado, dando la impresión de animación.
        """
        # Se verifica si el tiempo transcurrido es mayor o igual al tiempo establecido para actualizar el frame.
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_soldier_frame_delay()
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

    def update_position(self):
        """Metodo para actualizar posicion"""
        ###CHECAR

        if self._is_create_shot:
            self.rect.x -= self._speed

    @property
    def is_create_shot(self):
        return self._is_create_shot
    @is_create_shot.setter
    def is_create_shot(self, value):
        self._is_create_shot = value