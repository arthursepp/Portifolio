# Configurações do jogo
WIDTH = 1280  # Largura da janela do jogo
HEIGHT = 720  # Altura da janela do jogo
FPS = 60  # Frames por segundo
TILESIZE = 64  # Tamanho dos tiles

#UI:

BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'Python/python-rpg/graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

WATER_COLOR = '#71DDEE'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

weapon_data = {
    'sword': { 'cooldown': 100, 'damage': 15, 'graphic': 'Python/python-rpg/graphics/weapons/sword/full.png' },
    'lance': { 'cooldown': 400, 'damage': 30, 'graphic': 'Python/python-rpg/graphics/weapons/lance/full.png' },
    'axe': { 'cooldown': 300, 'damage': 20, 'graphic': 'Python/python-rpg/graphics/weapons/axe/full.png' },
    'rapier': { 'cooldown': 50, 'damage': 8, 'graphic': 'Python/python-rpg/graphics/weapons/rapier/full.png' },
    'sai': { 'cooldown': 80, 'damage': 10, 'graphic': 'Python/python-rpg/graphics/weapons/sai/full.png' },
}
