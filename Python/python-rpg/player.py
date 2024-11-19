import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, create_attack):
        super().__init__(groups)
        self.image = pygame.image.load('Python/python-rpg/graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        
        # Cria a hitbox do jogador
        self.hitbox = self.rect.inflate(0, -26)
        
        # Importa as animações do jogador
        self.import_player_assets()
        
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        # Movimento do jogador
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None       
        
        self.create_attack = create_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        print(self.weapon)
        
        self.obstacle_sprites = obstacle_sprites
        
    def import_player_assets(self):
        character_path = 'Python/python-rpg/graphics/player/'
        
        self.animations = {
            'up': [], 'down': [], 'left': [], 'right': [],
            'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
            'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack': [],
        }
        
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)      
        
    def input(self):
        if not self.attacking:
            keys = pygame.key.get_pressed()
            
            # Movimento do jogador
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0
                
            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1            
                self.status = 'right'
            else:
                self.direction.x = 0
                
            # Ataque do jogador
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()                
            
            # Mágica do jogador
            if keys[pygame.K_LCTRL]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                print('magic')
        
    def get_status(self):
        # Atualiza o status do jogador
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
                
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')
    
    def move(self, speed):
        # Normaliza o vetor de direção
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        # Move o jogador horizontalmente
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        
        # Move o jogador verticalmente
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        
        # Atualiza a posição do retângulo do jogador
        self.rect.center = self.hitbox.center
        
    def collision(self, direction):
        # Lida com colisões horizontais
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # Movendo para a direita
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # Movendo para a esquerda
                        self.hitbox.left = sprite.hitbox.right

        # Lida com colisões verticais
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # Movendo para baixo
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # Movendo para cima
                        self.hitbox.top = sprite.hitbox.bottom
        
    def cooldowns(self):
        # Lida com o cooldown dos ataques
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                
    def animate(self):
        # Anima o jogador
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)
                
    def update(self):
        # Atualiza o jogador
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)