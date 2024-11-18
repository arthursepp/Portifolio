import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        
        # Grupos de sprites visíveis e de obstáculos
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        # Cria o mapa do jogo
        self.create_map()
        
    def create_map(self):
        # Importa o layout do mapa a partir de arquivos CSV
        layout = {
            'boundary': import_csv_layout('Python/python-rpg/map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('Python/python-rpg/map/map_Grass.csv'),
            'object': import_csv_layout('Python/python-rpg/map/map_Objects.csv'),
        }
        
        # Importa as imagens dos tiles
        graphics = {
            'grass': import_folder('Python/python-rpg/graphics/Grass'),            
            'object': import_folder('Python/python-rpg/graphics/Objects'),
        }        
        
        # Cria os tiles com base no layout importado
        for style, layout in layout.items():        
            for row_index, row in enumerate(layout):            
                for col_index, col in enumerate(row):                    
                    if col != '-1':                    
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            # Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'grass', random_grass_image)
                            Tile((x, y), [self.visible_sprites], 'grass', random_grass_image)
                            
                        if style == 'object':
                            surf = graphics['object'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)

        # Cria o jogador
        self.player = Player((2000, 1430), [self.visible_sprites], self.obstacle_sprites)
        
    def run(self):
        # Desenha e atualiza os sprites visíveis
        self.visible_sprites.custom_draw(self.player)       
        self.visible_sprites.update()
        # Mostra o status do jogador no debug
        debug(self.player.status)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
        # Carrega a imagem do chão
        self.floor_surf = pygame.image.load('Python/python-rpg/graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))
        
    def custom_draw(self, player):
        # Calcula o offset da câmera
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        # Desenha o chão
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
                 
        # Desenha os sprites ordenados pela posição y
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)