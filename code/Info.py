import sys
import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN
from pygame.font import Font
from code.Const import C_WHITE, DISPLAY_WIDTH, DISPLAY_HEIGHT, HIT_DAMAGE, C_GREEN, C_RED


class Info:
    def __init__(self, window: Surface):
        self.window = window
        # Preload and scale enemies sprites
        self.e1 = pygame.transform.scale(pygame.image.load('./asset/TurtleBg0.png').convert_alpha(), (60, 40))
        self.e2 = pygame.transform.scale(pygame.image.load('./asset/SharkBg0.png').convert_alpha(), (120, 65))
        self.e3 = pygame.transform.scale(pygame.image.load('./asset/AnglerfishBg0.png').convert_alpha(), (50, 40))
        self.e4 = pygame.transform.scale(pygame.image.load('./asset/OctopusBg0.png').convert_alpha(), (60, 50))
        self.e5 = pygame.transform.scale(pygame.image.load('./asset/WormBg0.png').convert_alpha(), (60, 20))
        self.bg = pygame.image.load('./asset/Level2Bg0.png').convert_alpha()

    def info_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('./asset/Ithaca.ttf', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        # Show all enemies and worm values before the level start
        pygame.mixer_music.stop()  # Stop the menu music before start
        while True:
            self.window.blit(self.bg, (0, 0))
            self.info_text(40, "Faça pontos comendo minhocas", C_WHITE, (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT - 295))
            self.info_text(40, "e fuja dos inimigos!", C_WHITE, (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT - 260))
            self.window.blit(self.e1, (DISPLAY_WIDTH * 0.30, 95))
            self.info_text(30, f"Dano: -{HIT_DAMAGE['Turtle']}", C_RED, (DISPLAY_WIDTH * 0.20, 110))
            self.window.blit(self.e2, (DISPLAY_WIDTH * 0.37 - 40, 145))
            self.info_text(30, f"Dano: -{HIT_DAMAGE['Shark']}", C_RED, (DISPLAY_WIDTH * 0.20, 180))
            self.window.blit(self.e3, (DISPLAY_WIDTH * 0.76, 155))
            self.info_text(30, f"Dano: -{HIT_DAMAGE['Anglerfish']}", C_RED, (DISPLAY_WIDTH * 0.65, 180))
            self.window.blit(self.e4, (DISPLAY_WIDTH * 0.76, 85))
            self.info_text(30, f"Dano: -{HIT_DAMAGE['Octopus']}", C_RED, (DISPLAY_WIDTH * 0.65, 110))
            self.window.blit(self.e5, (DISPLAY_WIDTH / 2 + 10, 235))
            self.info_text(30, f"Vida: +{-HIT_DAMAGE['Worm']}", C_GREEN, (DISPLAY_WIDTH / 2 - 50, 245))
            self.info_text(35, "aperte ENTER para iniciar!", C_WHITE, (DISPLAY_WIDTH / 2 - 10, DISPLAY_HEIGHT - 30))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    # Wait the player confirmation to start
                    if event.key == K_RETURN:
                        return
            pygame.display.flip()
