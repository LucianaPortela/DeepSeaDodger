import sys
import pygame
from datetime import datetime
from pygame import Surface, Rect, KEYDOWN, K_RETURN
from pygame.constants import K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from code.Const import C_YELLOW, SCORE_POS, MENU_OPTION, C_WHITE, C_ORANGE


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)


    def save(self, game_mode: str, player_score: list[int]):
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(30, 'Parabéns! seu peixinho retornou para casa.', C_WHITE, SCORE_POS['Title'])
            text = 'Digite o nome do seu peixinho:'
            score = player_score[0]
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 10:
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 10:
                            name += event.unicode
            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(40, '10 MELHORES PEIXINHOS', C_ORANGE, SCORE_POS['Title'])
        self.score_text(20, 'PEIXINHO     MINHOCAS           DATA      ', C_ORANGE, SCORE_POS['Label'])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('./asset/BALOOBHAIJAAN-REGULAR.TTF', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def get_formatted_date():
        current_datetime = datetime.now()
        current_time = current_datetime.strftime("%H:%M")
        current_date = current_datetime.strftime("%d/%m/%y")
        return f"{current_time} - {current_date}"