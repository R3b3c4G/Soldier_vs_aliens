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
    no_id=1
    def __init__(self):
        self.id = Scoreboard.no_id
        Scoreboard.no_id += 1
        self._points = 0
        self._typeface = "kilmono"
        self._font_size = 40
        self._font_color = (242, 68, 17 )
        self._text = " J1. Mata a los Aliens MUUUAJAJAJA"
        if self.id == 2:
            self._text = "J2. Ganale al J1 no te dejes!!!!!"
            self._font_color = (255, 227, 89)

        #Se agrega la imagen con el score
        self._font = pygame.font.SysFont(self._typeface, self._font_size)
        self.image = self._font.render(self._text, True, self._font_color)

        self.rect = self.image.get_rect()
        #Se ajusta la posicion del marcador
        self.rect.x = Configurations.get_screen_size()[0]*0.05
        self.rect.y = Configurations.get_screen_size()[1]*0.05

    def update(self, new_score: int)->None:
        text = "J1 Aliens Exterminados: " + str(new_score)

        if self.id > 1:
            text = "J2 Aliens Asesinados: " + str(new_score)

        self.image = self._font.render(text, True, self._font_color)
    def blit(self, screen: pygame.surface.Surface ):
        screen.blit(self.image, self.rect)

    """Acceso a atributos"""
    @property
    def points (self)->int:
        return self._points
    @points.setter
    def points (self, points):
        self._points = points

    @property
    def position_x (self):
        return self.rect.x
    @position_x.setter
    def position_x (self, position):
        self.rect.x = position

    @property
    def position_y (self):
        return self.rect.y
    @position_y.setter
    def position_y (self, position):
        self.rect.y = position

    @property
    def text (self):
        return self._text
    @text.setter
    def text (self, text:str):
        self._text = text



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


class Audio:
    def __init__(self):
        # Se carga la música del juego.
        pygame.mixer.music.load(Configurations.get_music_path())

        # Se cargan los sonidos.
        self._start_sound = pygame.mixer.Sound(Configurations.get_start_sounds_path())
        self._shoot_sound_path = pygame.mixer.Sound(Configurations.get_shoot_sound_path())
        self._game_over_sound = pygame.mixer.Sound(Configurations.get_game_over_sound_path())

    @classmethod
    def play_music(cls, volume)->None:
        """
        Se utiliza para realizar un desvanecimiento de la musica del juego hasta parar
        :param volume: tiempo de desvanecimiento en ms
        :return:
        """
        pygame.mixer.music.play(loops= -1) #El -1 indica que se reproduce en bucle
        pygame.mixer.music.set_volume(volume)


    @classmethod
    def music_fadeout(cls, time):
        """
        Se utiliza para realizar el desvanecimiento de la musica del juego
        :param time:
        :return:
        """
        pygame.mixer.music.fadeout(time)
    def play_start_sound(self)->None:
        """
        Se utiliza para reproduci el sonido cuando epieza el juego
        :return:
        """
        self._start_sound.play()
    def play_shoot_sound(self)->None:
        """
        Reproduce sonidos cuando la serpiente come una manzana
        :return:
        """
        self._shoot_sound_path.play()
    def play_game_over(self)->None:
        """Reproduce el sonido cuando pierde el jugador"""
        self._game_over_sound.play()