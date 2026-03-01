import sys
import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN
from pygame.font import Font
from code.Const import C_WHITE, DISPLAY_WIDTH, DISPLAY_HEIGHT, C_ORANGE


class GameOver:
    def __init__(self, window: Surface):
        self.window = window
        self.bg = pygame.image.load('./asset/GameOverBg.png').convert_alpha()
        self.bg = pygame.transform.scale(self.bg, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

    def text_gameover(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, font_name: str,
                      surface: Surface):
        text_font: Font = pygame.font.Font(f'./asset/{font_name}', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        surface.blit(source=text_surf, dest=text_rect)

    def run(self):
        fade_surface = Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        fade_surface.blit(self.bg, (0, 0))
        pygame.mixer_music.load(f'./asset/GameOver.mp3')
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(-1)  # Play the music over and over
        self.text_gameover(100, "GAME OVER", C_ORANGE, (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2 - 100), 'Ithaca.ttf',
                           fade_surface)
        self.text_gameover(40, "Poxa, seu peixinho morreu..", C_WHITE, (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2 - 30),
                           'Ithaca.ttf', fade_surface)
        self.text_gameover(20, "aperte Enter para voltar ao menu", C_WHITE,
                           (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2 + 140),
                           'Ithaca.ttf', fade_surface)

        for alpha in range(0, 255, 5):
            # Create a fadein and fadeout for a Game Over sad vibe
            fade_surface.set_alpha(alpha)
            self.window.blit(fade_surface, (0, 0))
            pygame.display.flip()
            pygame.time.delay(30)  # Controls the transition speed of the fade-in

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    # Wait for player to press enter to return to the main menu
                    if event.key == K_RETURN:
                        return
