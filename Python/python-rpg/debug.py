import pygame
pygame.init()

# Define a fonte para o texto de debug
font = pygame.font.Font(None, 30)

def debug(info, y=10, x=10):
    # Obtém a superfície de exibição atual
    display_surface = pygame.display.get_surface()
    # Renderiza o texto de debug
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    # Desenha um retângulo preto atrás do texto
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    # Desenha o texto na tela
    display_surface.blit(debug_surf, debug_rect)