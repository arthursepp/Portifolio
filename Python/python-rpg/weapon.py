import pygame  # Importa a biblioteca pygame

class Weapon(pygame.sprite.Sprite):  # Define a classe Weapon que herda de pygame.sprite.Sprite
    def __init__(self, player, groups):
        super().__init__(groups)  # Inicializa a classe base com os grupos de sprites
        
        direction = player.status.split('_')[0]  # Obtém a direção do jogador a partir do status
        
        full_path = f'Python/python-rpg/graphics/weapons/{player.weapon}/{direction}.png'  # Cria o caminho completo para a imagem da arma
        self.image = pygame.image.load(full_path).convert_alpha()  # Carrega a imagem da arma e converte para incluir transparência
        
        if direction == 'right':
            self.rect = self.image.get_rect(midleft=player.rect.midright + pygame.math.Vector2(0, 16))  # Define a posição da arma à direita do jogador
            
        elif direction == 'left':
            self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(0, 16))  # Define a posição da arma à esquerda do jogador
            
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(-10, 0))  # Define a posição da arma abaixo do jogador
            
        else:
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(-10, 0))  # Define a posição da arma acima do jogador