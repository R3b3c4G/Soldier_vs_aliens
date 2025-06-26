class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _game_title = "Soldados vs aliens"              # Título de la ventana.
    _screen_size = (1280, 720)                      # Resolución de la pantalla (ancho, alto).
    _fps = 30                                       # Número máximo de FPS del videojuego.
    """NUEVO."""
    _game_over_screen_time = 4                      # Tiempo que se detiene el juego al perder.

    # Configuraciones del soldado.
    _soldier_size = (142, 76)                       # Escala del soldado (ancho, alto).
    _soldier_frames_per_row = 4                     # Número de frames que contiene cada fila de la hoja de frames.
    _soldier_frames_per_column = 2                  # Número de filas de la hoja de frames.
    _soldier_frame_delay = 300                      # Tiempo de cada frame del personaje (en ms) para la animación del descanso.
    _soldier_shooting_frame_delay = 34              # Tiempo de cada frame del personaje (en ms) para la animación del disparo.
    _soldier_speed = 12.5                           # Velocidad (en píxeles) del personaje.

    # Configuraciones de los disparos.
    _shot_size = (32, 32)                           # Escala del disparo (ancho, alto).
    _shot_frames_per_row = 4                        # Número de frames que contiene cada fila de la hoja de frames.
    _shot_frame_delay = 100                         # Tiempo de cada frame del disparo (en ms).
    _shot_speed = 32.5                              # Velocidad (en píxeles) del disparo.
    """NUEVO."""
    _max_gunshots = 2                               # Número máximo de disparos.

    # Configuraciones de los aliens.
    _alien_size = (78, 76)                          # Escala del alien (ancho, alto).
    _alien_frames_per_row = 4                       # Número de frames que contiene cada fila de la hoja de frames.
    _alien_frame_delay = 180                        # Tiempo de cada frame del disparo (en ms).
    _alien_speed_x = 4.5                            # Velocidad en X (en píxeles) del alien.
    _alien_speed_y = 22.5                           # Velocidad en Y (en píxeles) del alien.
    _min_aliens = 10                                # Mínimo de enemigos que aparecen en la pantalla.

    # Rutas de las imágenes utilizadas.
    _background_image_path = "../Media/background_image.jpg"
    _soldier_sheet_path = "../Media/soldier-idle_shooting_sheet.png"
    _shot_sheet_path = "../Media/shot-sheet.png"
    _alien_sheets_path = ["../Media/alien1-Sheet.png", "../Media/alien2-Sheet.png",
                          "../Media/alien3-Sheet.png", "../Media/alien4-Sheet.png",
                          "../Media/alien5-Sheet.png"]
    _game_over_image_path = "../Media/game_over_image.jpg"

    #Rutas de sonidos
    _music_volume = 0.15
    _music_fadeout_time=_game_over_screen_time
    _music_path = "../Media/sound_fond.mp3"
    _start_sounds_path = "../Media/iniciosound.mp3"
    _game_over_sound_path = "../Media/intro_sound.mp3"
    _shoot_sound_path = "../Media/shot_laser.mp3"


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

    """NUEVO."""
    @classmethod
    def get_game_over_screen_time(cls) -> int:
        """
        Getter para _game_over_screen_time.
        """
        return cls._game_over_screen_time

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
    def get_max_gunshots(cls) -> int:
        """
        Getter para _max_gunshots.
        """
        return cls._max_gunshots

    @classmethod
    def get_alien_size(cls) -> tuple[int, int]:
        """
        Getter para _alien_size.
        """
        return cls._alien_size

    @classmethod
    def get_alien_frames_per_row(cls) -> int:
        """
        Getter para _alien_frames_per_row.
        """
        return cls._shot_frames_per_row

    @classmethod
    def get_alien_frame_delay(cls) -> int:
        """
        Getter para _alien_frame_delay.
        """
        return cls._alien_frame_delay

    @classmethod
    def get_alien_speed_x(cls) -> float:
        """
        Getter para _alien_speed_x.
        """
        return cls._alien_speed_x

    @classmethod
    def get_alien_speed_y(cls) -> float:
        """
        Getter para _alien_speed_y.
        """
        return cls._alien_speed_y

    @classmethod
    def get_min_aliens(cls) -> int:
        """
        Getter para _min_aliens.
        """
        return cls._min_aliens

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

    @classmethod
    def get_alien_sheets_path(cls) -> list:
        """
        Getter para _alien_sheets_path.
        """
        return cls._alien_sheets_path

    @classmethod
    def get_game_over_image_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._game_over_image_path

    @classmethod
    def get_music_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._music_path

    @classmethod
    def get_start_sounds_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._start_sounds_path

    @classmethod
    def get_game_over_sound_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._game_over_sound_path

    @classmethod
    def get_shoot_sound_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._shoot_sound_path

    @classmethod
    def get_music_volume (cls) -> float:
        """
        Getter para _background_image_path.
        """
        return cls._music_volume
    @classmethod
    def get_music_fadeout_time (cls):
        return cls._music_fadeout_time



