import sys
import pygame
from datetime import datetime
from pygame import Surface, KEYDOWN, K_RETURN
from pygame.constants import K_BACKSPACE, K_ESCAPE
from code.Const import RANKING_POSITION, C_WHITE, C_ORANGE
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.font_title = pygame.font.Font('./asset/Ithaca.ttf', 60)
        self.font_main = pygame.font.Font('./asset/Ithaca.ttf', 35)
        self.font_data = pygame.font.Font('./asset/Ithaca.ttf', 27)

    def save_score(self, game_mode: str, player_score: list[int]):
        # Collect player name and save the final score to the database
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(self.surf, self.rect)
            self.score_text(self.font_title, 'Parabéns!', C_WHITE, RANKING_POSITION['Title'])
            self.score_text(self.font_data, 'Seu peixinho conseguiu retornar para casa!', C_WHITE,
                            RANKING_POSITION['Subtitle'])
            score = player_score[0]
            self.score_text(self.font_main, 'Digite o nome do seu peixinho:', C_WHITE,
                            RANKING_POSITION['EnterName'])
            self.score_text(self.font_main, name, C_ORANGE, RANKING_POSITION['Name'])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) >= 1:
                        # Save to database and proceed to ranking
                        db_proxy.save({'name': name,
                                       'score': score,
                                       'date': get_formatted_date()})
                        db_proxy.close()
                        self.show_ranking()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    elif len(name) < 8:
                        name += event.unicode
            pygame.display.flip()
            pass

    def show_ranking(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.ranking()
        db_proxy.close()

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(self.font_title, '7 MELHORES PEIXINHOS', C_ORANGE, RANKING_POSITION['Title'])
            self.score_text(self.font_main, 'PEIXINHO', C_WHITE,
                            (RANKING_POSITION['PlayerName'], RANKING_POSITION['Label'][1]))
            self.score_text(self.font_main, 'MINHOCAS', C_WHITE,
                            (RANKING_POSITION['PlayerScore'], RANKING_POSITION['Label'][1]))
            self.score_text(self.font_main, 'DATA', C_WHITE,
                            (RANKING_POSITION['PlayerDate'], RANKING_POSITION['Label'][1]))
            # Iterate through the high scores list to display each players rank
            for index, player_score in enumerate(list_score):
                id_, name, score, date = player_score
                # Vertical position from const.py
                y_pos = RANKING_POSITION[index][1]
                self.score_text(self.font_data, f'{name}', C_ORANGE, (RANKING_POSITION['PlayerName'], y_pos))
                self.score_text(self.font_data, f'{int(score):03d}', C_ORANGE, (RANKING_POSITION['PlayerScore'], y_pos))
                self.score_text(self.font_data, f'{date}', C_ORANGE, (RANKING_POSITION['PlayerDate'], y_pos))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE or event.key == K_RETURN:
                        return
            pygame.display.flip()

    def score_text(self, font_obj, text, color, center_pos):
        text_surf = font_obj.render(str(text), True, color).convert_alpha()
        text_rect = text_surf.get_rect(center=center_pos)
        self.window.blit(text_surf, text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_date}"
