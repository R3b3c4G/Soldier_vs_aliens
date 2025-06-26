import pygame
from Configurations import Configurations

class Background:
    """
    Clase que contiene el fondo de pantalla.
    Sus atributos son: image (apariencia) y rect (posición y tamaño).
    Sus métodos son: blit() (dibujar).
    """
    def __init__(self):
        # Se carga la imagen del fondo de pantalla.
        image_path = Configurations.get_background_image_path()
        self.image = pygame.image.load(image_path)

        # Se escala la imagen al tamaño de la pantalla.
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el fondo de pantalla en la pantalla.
        :param screen: Pantalla en donde se dibuja el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)


class Scoreboard:
    def __init__(self):
        self._points= 0
        self._typeface = "kilmono"
        self._font_size = 40
        self._font_color = (60, 90, 255)

        #Se agrega la imagen con el score
        self._font = pygame.font.SysFont(self._typeface, self._font_size)
        self.image = self._font.render("Mata a los Aliens MUUUAJAJAJA", True, self._font_color)

        self.rect = self.image.get_rect()
        #Se ajusta la posicion del marcador
        self.rect.x = Configurations.get_screen_size()[0]*0.05
        self.rect.y = Configurations.get_screen_size()[1]*0.05

    def update(self, new_score: int)->None:
        text = "Aliens Exterminados: " + str(new_score)
        self.image = self._font.render(text, True, self._font_color)
    def blit(self, screen: pygame.surface.Surface ):
        screen.blit(self.image, self.rect)


    @property
    def points (self)->int:
        return self._points
    @points.setter
    def points (self, points):
        self._points = points


class GameOverImage:
    def __init__(self):
        game_over_image_path = Configurations.get_game_over_image_path()
        self.image = pygame.image.load(game_over_image_path)

        # Se escala la imagen al tamaño de la pantalla.
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface) -> None:

        # Dibujar la imagen en pantalla
        screen.blit(self.image, self.rect)