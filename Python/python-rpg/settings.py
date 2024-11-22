# Configurações do jogo
WIDTH = 1280  # Largura da janela do jogo
HEIGHT = 720  # Altura da janela do jogo
FPS = 60  # Frames por segundo
TILESIZE = 64  # Tamanho dos tiles

# UI:
BAR_HEIGHT = 20  # Altura das barras de status
HEALTH_BAR_WIDTH = 200  # Largura da barra de vida
ENERGY_BAR_WIDTH = 140  # Largura da barra de energia
ITEM_BOX_SIZE = 80  # Tamanho da caixa de itens
UI_FONT = 'Python/python-rpg/graphics/font/joystix.ttf'  # Fonte da UI
UI_FONT_SIZE = 18  # Tamanho da fonte da UI

WATER_COLOR = '#71DDEE'  # Cor da água
UI_BG_COLOR = '#222222'  # Cor de fundo da UI
UI_BORDER_COLOR = '#111111'  # Cor da borda da UI
TEXT_COLOR = '#EEEEEE'  # Cor do texto

HEALTH_COLOR = 'red'  # Cor da barra de vida
ENERGY_COLOR = 'blue'  # Cor da barra de energia
UI_BORDER_COLOR_ACTIVE = 'gold'  # Cor da borda ativa da UI

# Dados das armas
weapon_data = {
    'sword': { 'cooldown': 100, 'damage': 15, 'graphic': 'Python/python-rpg/graphics/weapons/sword/full.png' },
    'lance': { 'cooldown': 400, 'damage': 30, 'graphic': 'Python/python-rpg/graphics/weapons/lance/full.png' },
    'axe': { 'cooldown': 300, 'damage': 20, 'graphic': 'Python/python-rpg/graphics/weapons/axe/full.png' },
    'rapier': { 'cooldown': 50, 'damage': 8, 'graphic': 'Python/python-rpg/graphics/weapons/rapier/full.png' },
    'sai': { 'cooldown': 80, 'damage': 10, 'graphic': 'Python/python-rpg/graphics/weapons/sai/full.png' },
}

magic_data = {
    'flame': {'strength': 5, 'cost': 15, 'graphic': 'Python/python-rpg/graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 10, 'graphic': 'Python/python-rpg/graphics/particles/heal/heal.png'}
}
