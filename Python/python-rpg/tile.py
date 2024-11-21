import pygame  # Importa a biblioteca pygame
from settings import *  # Importa todas as configurações do arquivo settings.py

class Tile(pygame.sprite.Sprite):  # Define a classe Tile que herda de pygame.sprite.Sprite
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)  # Inicializa a classe base com os grupos de sprites
        self.sprite_type = sprite_type  # Define o tipo de sprite
        self.image = surface  # Define a imagem do tile
        
        # Ajusta a posição do tile dependendo do tipo
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILESIZE))  # Ajusta a posição para objetos
        else:
            self.rect = self.image.get_rect(topleft=pos)  # Ajusta a posição para outros tipos
        
        # Cria uma hitbox para o tile
        self.hitbox = self.rect.inflate(0, -10)  # Reduz a altura da hitbox