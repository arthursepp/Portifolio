import pygame  # Importa a biblioteca pygame
from settings import *  # Importa todas as configurações do arquivo settings.py

class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()  # Obtém a superfície de exibição
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)  # Define a fonte da UI
        
        # Inicializa o texto de vida
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)  # Define a barra de vida
        self.energy_bar_rect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)  # Define a barra de energia
        
        # Convertendo dicionário de armas:
        self.weapon_graphics = []  # Lista para armazenar gráficos das armas
        
        for weapon in weapon_data.values():
            path = weapon['graphic']  # Obtém o caminho do gráfico da arma
            weapon = pygame.image.load(path).convert_alpha()  # Carrega a imagem da arma
            self.weapon_graphics.append(weapon)  # Adiciona a imagem à lista
            
        # Convertendo dicionário de magias:
        self.magic_graphics = []  # Lista para armazenar gráficos das magias
        
        for magic in magic_data.values(): # Itera sobre as magias
            magic = pygame.image.load(magic['graphic']).convert_alpha() # Carrega a imagem da magia
            self.magic_graphics.append(magic) # Adiciona a imagem à lista
    
    def show_bar(self, current, max_amount, bg_rect, color):
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)  # Desenha o fundo da barra
        
        # Convertendo stats para pixels
        ratio = current / max_amount  # Calcula a proporção atual
        current_width = bg_rect.width * ratio  # Calcula a largura atual da barra
        current_rect = bg_rect.copy()  # Copia o retângulo de fundo
        current_rect.width = current_width  # Define a largura do retângulo atual
        
        # Desenhando a barra de vida
        pygame.draw.rect(self.display_surface, color, current_rect)  # Desenha a barra atual
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)  # Desenha a borda da barra
    
    def show_exp(self, exp):
        text_surf = self.font.render(str(int(exp)), False, TEXT_COLOR)  # Renderiza o texto da experiência
        x = self.display_surface.get_size()[0] - 20  # Define a posição x do texto
        y = self.display_surface.get_size()[1] - 20  # Define a posição y do texto
        text_rect = text_surf.get_rect(bottomright=(x, y))  # Obtém o retângulo do texto
        
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 20))  # Desenha o fundo do texto
        self.display_surface.blit(text_surf, text_rect)  # Desenha o texto
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 20), 3)  # Desenha a borda do texto
    
    def selection_box(self, left, top, has_switched):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)  # Define o retângulo da caixa de seleção
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)  # Desenha o fundo da caixa
        
        if has_switched:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)  # Desenha a borda ativa
        else:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)  # Desenha a borda inativa
        
        return bg_rect  # Retorna o retângulo da caixa
        
    def weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.selection_box(10, 630, has_switched)  # Obtém o retângulo da caixa de seleção
        weapon_surf = self.weapon_graphics[weapon_index]  # Obtém a imagem da arma
        weapon_rect = weapon_surf.get_rect(center=bg_rect.center)  # Obtém o retângulo da arma
        
        self.display_surface.blit(weapon_surf, weapon_rect)  # Desenha a arma na tela
        
    def magic_overlay(self, magic_index, has_switched):
        bg_rect = self.selection_box(80, 635, has_switched)  # Obtém o retângulo da caixa de seleção
        magic_surf = self.magic_graphics[magic_index]  # Obtém a imagem da arma
        magic_rect = magic_surf.get_rect(center=bg_rect.center)  # Obtém o retângulo da arma
        
        self.display_surface.blit(magic_surf, magic_rect)  # Desenha a arma na tela
        
    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)  # Mostra a barra de vida
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)  # Mostra a barra de energia
        
        self.show_exp(player.exp)  # Mostra a experiência do jogador
        self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)  # Mostra a arma do jogador
        self.magic_overlay(player.magic_index, not player.can_switch_magic)