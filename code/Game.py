import sys
import pygame
from code.Const import DISPLAY_WIDTH, DISPLAY_HEIGHT, MENU_SELECTION, MAX_HP
from code.Info import Info
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(DISPLAY_WIDTH, DISPLAY_HEIGHT))

    def run(self, ):
        while True:

            menu = Menu(self.window)
            score = Score(self.window)
            menu_return = menu.run()

            if menu_return == MENU_SELECTION[0]:  # Play
                info_screen = Info(self.window)  # Show bestiary before start a new game
                info_screen.run()
                player_score = [0]
                player_position = [10, DISPLAY_HEIGHT / 2]
                player_health = [MAX_HP['Player']]
                level = Level(self.window, 'Level1', menu_return, player_score, player_position, player_health)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score, player_position, player_health)
                    level_return = level.run(player_score)
                    if level_return:
                        level = Level(self.window, 'Level3', menu_return, player_score, player_position, player_health)
                        level_return = level.run(player_score)
                        if level_return:
                            # Save the score only if reach the final of Level 3 without dying
                            score.save_score(menu_return, player_score)

            elif menu_return == MENU_SELECTION[1]:  # Score
                score.show_ranking()

            elif menu_return == MENU_SELECTION[2]:  # Exit
                pygame.quit()
                quit()
            else:
                pygame.quit()
                sys.exit()
