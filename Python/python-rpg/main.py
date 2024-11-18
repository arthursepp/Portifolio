import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        # Configura a janela do jogo
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('RPG Genérico')
        self.clock = pygame.time.Clock()
        
        # Cria o nível do jogo
        self.level = Level()

    def run(self):
        while True:
            # Lida com eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            # Preenche a tela com preto
            self.screen.fill('black')
            # Executa o nível do jogo
            self.level.run()
            # Atualiza a tela
            pygame.display.update()
            # Controla a taxa de frames
            self.clock.tick(FPS)
            
if __name__ == '__main__':
    game = Game()
    game.run()