import pygame

# C
C_ORANGE = (237, 159, 43)
C_WHITE = (255, 255, 255)
C_BLUE = (11, 63, 184)
C_GREEN = (0, 255, 0)
C_RED = (150, 0, 10)

# D

DAMAGE_DELAY = 1000
DAMAGE_SPRITE_DELAY = 200

# E
EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 3,
    'Level2Bg0': 1,
    'Level2Bg1': 1,
    'Level2Bg2': 0,
    'Level2Bg3': 1,
    'Level2Bg4': 2,
    'Level3Bg0': 1,
    'Level3Bg1': 0,
    'Level3Bg2': 2,
    'Level3Bg3': 1,
    'Level3Bg4': 1,
    'Player1': 4,
    'Enemy1': 2,
    'Enemy2': 4,
    'Enemy3': 7,
    'Enemy4': 5,
    'Enemy5': 2,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level3Bg0': 999,
    'Level3Bg1': 999,
    'Level3Bg2': 999,
    'Level3Bg3': 999,
    'Level3Bg4': 999,
    'Player1': 100,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
    'Enemy4': 1,
    'Enemy5': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Player1': 1,
    'Enemy1': 30,
    'Enemy2': 60,
    'Enemy3': 70,
    'Enemy4': 40,
    'Enemy5': -10,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Player1': 0,
    'Enemy1': 0,
    'Enemy2': 0,
    'Enemy3': 0,
    'Enemy4': 0,
    'Enemy5': 1,
}

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_d}

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 30000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SPAWN_TIME = {
    'Level1': 2000,
    'Level2': 1000,
    'Level3': 500,
}

SCORE_POS = {'Title': (WIN_WIDTH / 2, 35),
             'Subtitle': (WIN_WIDTH / 2, 90),
             'EnterName': (WIN_WIDTH / 2, 120),
             'Label': (WIN_WIDTH / 2, 80),
             'Name': (WIN_WIDTH / 2, 160),
             'PlayerName': (WIN_WIDTH * 0.25),
             'PlayerScore': (WIN_WIDTH * 0.50),
             'PlayerDate': (WIN_WIDTH * 0.75),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }
