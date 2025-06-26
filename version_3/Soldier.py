import pygame
from pygame.sprite import Sprite

from Configurations import Configurations
class Soldier(Sprite):
    """Clase del personaje de un soldado"""
    def __init__(self, screen):
        super().__init__()
        soldier_image_path = Configurations.get_soldier_image_path()
        self.image = pygame.image.load(soldier_image_path)
        #Se escala la imagen al tamaño del soldado
        image_soldier_size = Configurations.get_soldier_size()
        self.image = pygame.transform.scale(self.image, image_soldier_size)
        screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.centery = screen_rect.centery
        self.rect.left = screen_rect.left  # Esto colocará el sprite en el borde derecho

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza pra dibujar el fondo.
        :param screen:
        :return:
        """
        screen.blit(self.image, self.rect)
