import pygame

# C
C_ORANGE = (237, 159, 43)
C_WHITE = (255, 255, 255)
C_BLUE = (11, 63, 184)
C_GREEN = (0, 255, 0)
C_RED = (150, 0, 10)

# D
DISPLAY_WIDTH = 576
DISPLAY_HEIGHT = 324

DAMAGE_DELAY = 1000
DAMAGE_SPRITE_DELAY = 200

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# H
HIT_DAMAGE = {
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
    'Player': 1,
    'Turtle': 30,
    'Shark': 60,
    'Anglerfish': 70,
    'Octopus': 40,
    'Worm': -15,
}

# M
MAX_HP = {
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
    'Player': 50,
    'Turtle': 1,
    'Shark': 1,
    'Anglerfish': 1,
    'Octopus': 1,
    'Worm': 1,
}

MENU_SELECTION = ('PLAY',
                  'SCORE',
                  'EXIT')

MOVEMENT_SPEED = {
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
    'Player': 4,
    'Turtle': 2,
    'Shark': 4,
    'Anglerfish': 7,
    'Octopus': 5,
    'Worm': 2,
}

# P
PLAYER_KEY_UP = {'Player': pygame.K_w}
PLAYER_KEY_DOWN = {'Player': pygame.K_s}
PLAYER_KEY_LEFT = {'Player': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player': pygame.K_d}

# R
RANKING_POSITION = {'Title': (DISPLAY_WIDTH / 2, 35),
                    'Subtitle': (DISPLAY_WIDTH / 2, 90),
                    'EnterName': (DISPLAY_WIDTH / 2, 120),
                    'Label': (DISPLAY_WIDTH / 2, 80),
                    'Name': (DISPLAY_WIDTH / 2, 160),
                    'PlayerName': (DISPLAY_WIDTH * 0.25),
                    'PlayerScore': (DISPLAY_WIDTH * 0.50),
                    'PlayerDate': (DISPLAY_WIDTH * 0.75),
                    0: (DISPLAY_WIDTH / 2, 105),
                    1: (DISPLAY_WIDTH / 2, 130),
                    2: (DISPLAY_WIDTH / 2, 155),
                    3: (DISPLAY_WIDTH / 2, 180),
                    4: (DISPLAY_WIDTH / 2, 205),
                    5: (DISPLAY_WIDTH / 2, 230),
                    6: (DISPLAY_WIDTH / 2, 255),
                    }

# S
SPAWN_TIME = {
    'Level1': 2000,
    'Level2': 1000,
    'Level3': 500,
}

SCORE_WORMS = {
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
    'Player': 0,
    'Turtle': 0,
    'Shark': 0,
    'Anglerfish': 0,
    'Octopus': 0,
    'Worm': 1,
}

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 30000
