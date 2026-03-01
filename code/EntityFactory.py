import random
from code.Background import Background
from code.Const import DISPLAY_WIDTH, DISPLAY_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1':  # Create background loop
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (DISPLAY_WIDTH, 0)))  # Continue the loop
                return list_bg
            case 'Level2':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (DISPLAY_WIDTH, 0)))
                return list_bg
            case 'Level3':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level3Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level3Bg{i}', (DISPLAY_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (10, DISPLAY_HEIGHT / 2))

            case 'Turtle':  # Randomizes enemy spawn height to prevent players from hiding in the edges
                return Enemy('Turtle', (DISPLAY_WIDTH + 5, random.randint(5, DISPLAY_HEIGHT - 35)))

            case 'Shark':
                return Enemy('Shark', (DISPLAY_WIDTH + 5, random.randint(5, DISPLAY_HEIGHT - 70)))

            case 'Anglerfish':
                return Enemy('Anglerfish', (DISPLAY_WIDTH + 5, random.randint(5, DISPLAY_HEIGHT - 35)))

            case 'Octopus':
                return Enemy('Octopus', (DISPLAY_WIDTH + 5, random.randint(5, DISPLAY_HEIGHT - 35)))

            case 'Worm':
                return Enemy('Worm', (DISPLAY_WIDTH + 5, random.randint(5, DISPLAY_HEIGHT - 35)))
