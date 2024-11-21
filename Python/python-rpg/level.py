import pygame  # Importa a biblioteca pygame
from settings import *  # Importa todas as configurações do arquivo settings.py
from tile import Tile  # Importa a classe Tile do arquivo tile.py
from player import Player  # Importa a classe Player do arquivo player.py
from debug import debug  # Importa a função debug do arquivo debug.py
from support import *  # Importa funções de suporte do arquivo support.py
from random import choice  # Importa a função choice da biblioteca random
from weapon import Weapon  # Importa a classe Weapon do arquivo weapon.py
from ui import UI  # Importa a classe UI do arquivo ui.py

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()  # Obtém a superfície de exibição do jogo
        
        # Grupos de sprites visíveis e de obstáculos
        self.visible_sprites = YSortCameraGroup()  # Cria um grupo de sprites visíveis com ordenação por Y
        self.obstacle_sprites = pygame.sprite.Group()  # Cria um grupo de sprites de obstáculos
        
        self.current_attack = None  # Inicializa o ataque atual como None
        
        # Cria o mapa do jogo
        self.create_map()  # Chama o método para criar o mapa
        
        self.ui = UI()  # Inicializa a interface do usuário
    
    def create_map(self):
        # Importa o layout do mapa a partir de arquivos CSV
        layout = {
            'boundary': import_csv_layout('Python/python-rpg/map/map_FloorBlocks.csv'),  # Layout das bordas
            'grass': import_csv_layout('Python/python-rpg/map/map_Grass.csv'),  # Layout da grama
            'object': import_csv_layout('Python/python-rpg/map/map_Objects.csv'),  # Layout dos objetos
        }
        
        # Importa as imagens dos tiles
        graphics = {
            'grass': import_folder('Python/python-rpg/graphics/Grass'),  # Imagens da grama
            'object': import_folder('Python/python-rpg/graphics/Objects'),  # Imagens dos objetos
        }
        
        # Cria os tiles com base no layout importado
        for style, layout in layout.items():  # Itera sobre os diferentes estilos de layout
            for row_index, row in enumerate(layout):  # Itera sobre as linhas do layout
                for col_index, col in enumerate(row):  # Itera sobre as colunas do layout
                    if col != '-1':  # Verifica se a célula não está vazia
                        x = col_index * TILESIZE  # Calcula a posição x do tile
                        y = row_index * TILESIZE  # Calcula a posição y do tile
                        
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')  # Cria um tile invisível para as bordas
                        
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])  # Escolhe uma imagem aleatória de grama
                            Tile((x, y), [self.visible_sprites], 'grass', random_grass_image)  # Cria um tile de grama
                        
                        if style == 'object':
                            surf = graphics['object'][int(col)]  # Obtém a imagem do objeto
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)  # Cria um tile de objeto

        # Cria o jogador
        self.player = Player((2000, 1430), [self.visible_sprites], self.obstacle_sprites, self.create_attack, self.destroy_attack)  # Inicializa o jogador
    
    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites])  # Cria um ataque e o adiciona aos sprites visíveis
    
    def destroy_attack(self):
        if self.current_attack:  # Verifica se há um ataque atual
            self.current_attack.kill()  # Remove o ataque atual
        self.current_attack = None  # Define o ataque atual como None
    
    def run(self):
        # Desenha e atualiza os sprites visíveis
        self.visible_sprites.custom_draw(self.player)  # Desenha os sprites visíveis com a câmera
        self.visible_sprites.update()  # Atualiza os sprites visíveis
        self.ui.display(self.player)  # Atualiza a interface do usuário com as informações do jogador

        # Mostra o status do jogador no debug
        # debug(self.player.status)  # Comenta a linha de debug do status do jogador

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()  # Inicializa a classe base pygame.sprite.Group
        self.display_surface = pygame.display.get_surface()  # Obtém a superfície de exibição do jogo
        self.half_width = self.display_surface.get_size()[0] // 2  # Calcula a metade da largura da tela
        self.half_height = self.display_surface.get_size()[1] // 2  # Calcula a metade da altura da tela
        self.offset = pygame.math.Vector2()  # Inicializa o vetor de offset da câmera
        
        # Carrega a imagem do chão
        self.floor_surf = pygame.image.load('Python/python-rpg/graphics/tilemap/ground.png').convert()  # Carrega a imagem do chão
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))  # Obtém o retângulo da imagem do chão
    
    def custom_draw(self, player):
        # Calcula o offset da câmera
        self.offset.x = player.rect.centerx - self.half_width  # Calcula o offset x da câmera
        self.offset.y = player.rect.centery - self.half_height  # Calcula o offset y da câmera
        
        # Desenha o chão
        floor_offset_pos = self.floor_rect.topleft - self.offset  # Calcula a posição do chão com o offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)  # Desenha o chão na tela
        
        # Desenha os sprites ordenados pela posição y
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):  # Ordena os sprites pela posição y
            offset_pos = sprite.rect.topleft - self.offset  # Calcula a posição do sprite com o offset
            self.display_surface.blit(sprite.image, offset_pos)  # Desenha o sprite na tela