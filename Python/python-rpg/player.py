import pygame  # Importa a biblioteca pygame
from settings import *  # Importa todas as configurações do arquivo settings.py,
from support import *  # Importa funções de suporte

class Player(pygame.sprite.Sprite):  # Define a classe Player que herda de pygame.sprite.Sprite
    def __init__(self, pos, groups, obstacle_sprites, create_attack, destroy_attack, create_magic):
        super().__init__(groups)  # Inicializa a classe base com os grupos de sprites
        self.image = pygame.image.load('Python/python-rpg/graphics/test/player.png').convert_alpha()  # Carrega a imagem do jogador
        self.rect = self.image.get_rect(topleft=pos)  # Define o retângulo do jogador
        
        # Cria a hitbox do jogador
        self.hitbox = self.rect.inflate(0, -26)  # Reduz a altura da hitbox
        
        # Importa as animações do jogador
        self.import_player_assets()
        
        self.status = 'down'  # Define o status inicial do jogador
        self.frame_index = 0  # Índice do quadro de animação
        self.animation_speed = 0.15  # Velocidade da animação

        # Movimento do jogador
        self.direction = pygame.math.Vector2()  # Vetor de direção do jogador
        self.attacking = False  # Estado de ataque do jogador
        self.attack_cooldown = 400  # Tempo de recarga do ataque
        self.attack_time = None  # Tempo do último ataque
        
        self.create_attack = create_attack  # Função para criar ataque
        self.destroy_attack = destroy_attack  # Função para destruir ataque
        self.weapon_index = 0  # Índice da arma atual
        self.weapon = list(weapon_data.keys())[self.weapon_index]  # Nome da arma atual
        self.can_switch_weapon = True  # Estado de troca de arma
        self.weapon_switch_time = None  # Tempo da última troca de arma
        self.switch_duration_cooldown = 200  # Tempo de recarga da troca de arma
        
        #Mágica
        self.create_magic = create_magic  # Função para criar mágica
        self.magic_index = 0 # Índice da mágica atual
        self.magic = list(magic_data.keys())[self.magic_index]  # Nome da arma atual
        self.can_switch_magic = True  # Estado de troca de mágica
        self.magic_switch_time = None  # Tempo da última troca de mágica        
        
        self.obstacle_sprites = obstacle_sprites  # Sprites de obstáculos
        
        # Status
        self.stats = {'health': 100, 'energy': 60, 'attack': 10, 'magic': 4, 'speed': 5}  # Atributos do jogador
        self.health = self.stats['health']  # Vida do jogador
        self.energy = self.stats['energy']  # Energia do jogador
        self.exp = 123  # Experiência do jogador
        self.speed = self.stats['speed']  # Velocidade do jogador
        
    def import_player_assets(self):
        character_path = 'Python/python-rpg/graphics/player/'  # Caminho das animações do jogador
        
        self.animations = {
            'up': [], 'down': [], 'left': [], 'right': [],
            'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
            'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack': [],
        }  # Dicionário de animações
        
        for animation in self.animations.keys():
            full_path = character_path + animation  # Caminho completo da animação
            self.animations[animation] = import_folder(full_path)  # Importa a animação
        
    def input(self):
        if not self.attacking:
            keys = pygame.key.get_pressed()  # Obtém as teclas pressionadas
            
            # Movimento do jogador
            if keys[pygame.K_UP]:
                self.direction.y = -1  # Move para cima
                self.status = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1  # Move para baixo
                self.status = 'down'
            else:
                self.direction.y = 0  # Para de mover verticalmente
                
            if keys[pygame.K_LEFT]:
                self.direction.x = -1  # Move para a esquerda
                self.status = 'left'
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1  # Move para a direita
                self.status = 'right'
            else:
                self.direction.x = 0  # Para de mover horizontalmente
                
            # Ataque do jogador
            if keys[pygame.K_SPACE]:
                self.attacking = True  # Inicia o ataque
                self.attack_time = pygame.time.get_ticks()  # Registra o tempo do ataque
                self.create_attack()  # Cria o ataque
            
            # Mágica do jogador
            if keys[pygame.K_LCTRL]:
                self.attacking = True  # Inicia a mágica
                self.attack_time = pygame.time.get_ticks()  # Registra o tempo da mágica
                
                style = list(magic_data.keys())[self.magic_index]  # Obtém o estilo da mágica
                strength = list(magic_data.values())[self.magic_index]['strength']  + self.stats['magic'] # Obtém a força
                cost = list(magic_data.values())[self.magic_index]['cost'] # Obtém o custo                
                self.create_magic(style,strength,cost) # Cria a mágica
        
            if keys[pygame.K_q] and self.can_switch_weapon:
                self.can_switch_weapon = False  # Desabilita a troca de arma
                self.weapon_switch_time = pygame.time.get_ticks()  # Registra o tempo da troca
                
                if self.weapon_index < len(list(weapon_data.keys())) - 1:
                    self.weapon_index += 1  # Troca para a próxima arma
                else:
                    self.weapon_index = 0  # Volta para a primeira arma
                    
                self.weapon = list(weapon_data.keys())[self.weapon_index]  # Atualiza a arma atual
                
            if keys[pygame.K_e] and self.can_switch_magic:
                self.can_switch_magic = False  # Desabilita a troca de mágica
                self.magic_switch_time = pygame.time.get_ticks()  # Registra o tempo da troca
                
                if self.magic_index < len(list(magic_data.keys())) - 1:
                    self.magic_index += 1  # Troca para a próxima mágica
                else:
                    self.magic_index = 0  # Volta para a primeira mágica
                    
                self.magic = list(magic_data.keys())[self.magic_index]  # Atualiza a mágica atual
                print('magic')
        
    def get_status(self):
        # Atualiza o status do jogador
        if self.direction.x == 0 and self.direction.y == 0:
            if 'idle' not in self.status and 'attack' not in self.status:
                self.status = self.status + '_idle'  # Define o status como idle
                
        if self.attacking:
            self.direction.x = 0  # Para de mover horizontalmente
            self.direction.y = 0  # Para de mover verticalmente
            
            if 'attack' not in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')  # Troca idle por attack
                else:
                    self.status = self.status + '_attack'  # Adiciona attack ao status
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')  # Remove attack do status
    
    def move(self, speed):
        # Normaliza o vetor de direção
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()  # Normaliza a direção
        
        # Move o jogador horizontalmente
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')  # Verifica colisões horizontais
        
        # Move o jogador verticalmente
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')  # Verifica colisões verticais
        
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
        current_time = pygame.time.get_ticks()  # Obtém o tempo atual
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False  # Termina o ataque
                self.destroy_attack()  # Destroi o ataque
        
        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True  # Permite trocar de arma novamente
                
        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_switch_magic = True  # Permite trocar de arma novamente
                
    def animate(self):
        # Anima o jogador
        animation = self.animations[self.status]  # Obtém a animação atual
        self.frame_index += self.animation_speed  # Atualiza o índice do quadro
        if self.frame_index >= len(animation):
            self.frame_index = 0  # Reinicia o índice do quadro
        self.image = animation[int(self.frame_index)]  # Atualiza a imagem do jogador
        self.rect = self.image.get_rect(center=self.hitbox.center)  # Atualiza o retângulo do jogador
                
    def update(self):
        # Atualiza o jogador
        self.input()  # Lê a entrada do jogador
        self.cooldowns()  # Verifica os cooldowns
        self.get_status()  # Atualiza o status do jogador
        self.animate()  # Anima o jogador
        self.move(self.speed)  # Move o jogador