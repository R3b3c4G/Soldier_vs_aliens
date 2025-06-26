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


class Audio:
    def __init__(self):
        # Se carga la música del juego.
        pygame.mixer.music.load(Configurations.get_music_path())

        # Se cargan los sonidos.
        self._start_sound = pygame.mixer.Sound(Configurations.get_start_sounds_path())
        self._shoot_sound_path = pygame.mixer.Sound(Configurations.get_shoot_sound_path())
        self._game_over_sound = pygame.mixer.Sound(Configurations.get_game_over_sound_path())
        self._impact_sound = pygame.mixer.Sound(Configurations.get_sound_impact())

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
        Reproduce sonidos cuando dispara
        :return:
        """
        self._shoot_sound_path.play()


    def play_game_over(self)->None:
        """Reproduce el sonido cuando pierde el jugador"""
        self._game_over_sound.play()

    def pla_impact_sound(self):
        self._impact_sound.play()