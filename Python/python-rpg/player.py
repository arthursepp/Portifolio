import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('Python/python-rpg/graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
        self.hitbox = self.rect.inflate(0, -26)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        
        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
            
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1            
        else:
            self.direction.x = 0
    
    def move(self, speed):
        # Normaliza o vetor de direção
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        # self.rect.center += self.direction * speed        
        
        self.hitbox.x += self.direction.x * speed
        
        self.collision('horizontal')
        
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        
        self.rect.center = self.hitbox.center
        
    
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):  # Corrigido aqui
                    if self.direction.x > 0: # Movendo para a direita (com colisões):
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # Movendo para a esquerda (com colisões):
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):  # Corrigido aqui
                    if self.direction.y > 0: # Movendo para baixo (com colisões):
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # Movendo para cima (com colisões):
                        self.hitbox.top = sprite.hitbox.bottom
        
    def update(self):
        self.input()
        self.move(self.speed)
