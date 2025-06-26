

class Configurations:
    """
    Clase que contiene todas las configuraciones
    del juego.
    Encapsulamiento: solo getter
    """

    # Configuraciones de pantalla.
    _screen_size = (1280, 720)               # Resolucion pantalla (ancho, alto)
    _game_title = "Alien Game de Me'Sant"
    #_background = (12, 55, 65)               # Fondo de pantalla en rgb de 0 a 255
    _soldier_size = (142, 76)
    #Tamaño de disparo:
    _shot_size = (32,32)


    _frames_per_row = 4                             # Número de frames que contiene cada fila de la hoja de frames.
    _soldier_frame_delay = 300                      # Tiempo de cada frame del personaje (en ms).
    _soldier_speed = 12.5                           # Velocidad (en píxeles) del personaje.

    #Fps para correr juego:
    _fps = 60

    #Imagenes de juego
    # Rutas de las imágenes utilizadas.
    _background_image_path = "../Media/background_image.jpg"
    _soldier_sheet_path = "../Media/soldier-idle-sheet.png"
    _shot_sheet_path = "../Media/shot-sheet.png"

    @classmethod
    def get_screen_size (cls) ->tuple[int, int]:
        """
        getter para screen_size: Tamaño de pantalla
        :return:
        """
        return cls._screen_size

    @classmethod
    def get_game_title(cls)->str:
        """
        getter para game_title
        :return:
        """
        return cls._game_title

    @classmethod
    def get_soldier_size(cls) ->tuple[int, int]:
        return cls._soldier_size

    @classmethod
    def get_fps(cls):
        return cls._fps

    """NUEVO."""

    @classmethod
    def get_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._frames_per_row

    """NUEVO."""

    @classmethod
    def get_soldier_frame_delay(cls) -> int:
        """
        Getter para _soldier_frame_delay.
        """
        return cls._soldier_frame_delay

    """NUEVO."""

    @classmethod
    def get_soldier_speed(cls) -> float:
        """
        Getter para _soldier_speed.
        """
        return cls._soldier_speed

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._background_image_path

    """CAMBIO. El método de acceso cambió de acuerdo al cambio del parámetro utilizado."""

    @classmethod
    def get_soldier_sheet_path(cls) -> str:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._soldier_sheet_path

    @classmethod
    def get_shot_sheet_path(cls) -> str:
        """Getter para la hoja de imagenes de disparo"""
        return cls._shot_sheet_path

    @classmethod
    def get_shot_size(cls):
        """Retorna tamaño de la imagen de disparo"""
        return cls._shot_size