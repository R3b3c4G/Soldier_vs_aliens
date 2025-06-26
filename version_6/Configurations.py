
class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _game_title = "Soldados vs aliens"              # Título de la ventana.
    _screen_size = (1280, 720)                      # Resolución de la pantalla (ancho, alto).
    _fps = 30                                       # Número máximo de FPS del videojuego.

    # Configuraciones del soldado.
    _soldier_size = (142, 76)                       # Escala del soldado (ancho, alto).
    _soldier_frames_per_row = 4                     # Número de frames que contiene cada fila de la hoja de frames.
    """NUEVO."""
    _soldier_frames_per_column = 2                  # Número de filas de la hoja de frames.
    _soldier_frame_delay = 300                      # Tiempo de cada frame del personaje (en ms) para la animación del descanso.
    """NUEVO."""
    _soldier_shooting_frame_delay = 34              # Tiempo de cada frame del personaje (en ms) para la animación del disparo.
    _soldier_speed = 12.5                           # Velocidad (en píxeles) del personaje.

    # Configuraciones de los disparos.
    _shot_size = (32, 32)                           # Escala del disparo (ancho, alto).
    _shot_frames_per_row = 4                        # Número de frames que contiene cada fila de la hoja de frames.
    _shot_frame_delay = 100                         # Tiempo de cada frame del disparo (en ms).
    _shot_speed = 32.5                              # Velocidad (en píxeles) del disparo.

    """CAMBIO. Se modificó la imagen que se carga para la hoja de sprites del soldado."""
    # Rutas de las imágenes utilizadas.
    _background_image_path = "../media/background_image.jpg"
    _soldier_sheet_path = "../media/soldier_and_shoot_path.png"
    _shot_sheet_path = "../media/shot-sheet.png"


    """ %%%%%%%     MÉTODOS DE ACCESO.    %%%%%%%%%%%%%%%%%%%%% """
    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para _game_title.
        """
        return cls._game_title

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para _screen_size.
        """
        return cls._screen_size

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps.
        """
        return cls._fps

    @classmethod
    def get_soldier_size(cls) -> tuple[int, int]:
        """
        Getter para _soldier_size.
        """
        return cls._soldier_size

    @classmethod
    def get_soldier_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._soldier_frames_per_row

    """NUEVO."""
    @classmethod
    def get_soldier_frames_per_column(cls) -> int:
        """
        Getter para _soldier_frames_per_column.
        """
        return cls._soldier_frames_per_column

    @classmethod
    def get_soldier_frame_delay(cls) -> int:
        """
        Getter para _soldier_frame_delay.
        """
        return cls._soldier_frame_delay

    """NUEVO."""
    @classmethod
    def get_soldier_shooting_frame_delay(cls) -> int:
        """
        Getter para _soldier_shooting_frame_delay.
        """
        return cls._soldier_shooting_frame_delay

    @classmethod
    def get_soldier_speed(cls) -> float:
        """
        Getter para _soldier_speed.
        """
        return cls._soldier_speed

    @classmethod
    def get_shot_size(cls) -> tuple[int, int]:
        """
        Getter para _shot_size.
        """
        return cls._shot_size

    @classmethod
    def get_shot_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._shot_frames_per_row

    @classmethod
    def get_shot_frame_delay(cls) -> int:
        """
        Getter para _shot_frame_delay.
        """
        return cls._shot_frame_delay

    @classmethod
    def get_shot_speed(cls) -> float:
        """
        Getter para _soldier_speed.
        """
        return cls._shot_speed

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._background_image_path

    @classmethod
    def get_soldier_sheet_path(cls) -> str:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._soldier_sheet_path

    @classmethod
    def get_shot_sheet_path(cls) -> str:
        """
        Getter para _shot_sheet_path.
        """
        return cls._shot_sheet_path