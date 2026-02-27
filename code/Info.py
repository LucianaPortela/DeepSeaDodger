#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN
from pygame.font import Font
from code.Const import C_WHITE, C_ORANGE, WIN_WIDTH, WIN_HEIGHT, ENTITY_DAMAGE, C_GREEN, C_RED


class Info:
    def __init__(self, window: Surface):
        self.window = window
        self.e1 = pygame.transform.scale(pygame.image.load('./asset/Enemy1Bg0.png').convert_alpha(), (60, 40))
        self.e2 = pygame.transform.scale(pygame.image.load('./asset/Enemy2Bg0.png').convert_alpha(), (120, 65))
        self.e3 = pygame.transform.scale(pygame.image.load('./asset/Enemy3Bg0.png').convert_alpha(), (50, 40))
        self.e4 = pygame.transform.scale(pygame.image.load('./asset/Enemy4Bg0.png').convert_alpha(), (60, 50))
        self.e5 = pygame.transform.scale(pygame.image.load('./asset/Enemy5Bg0.png').convert_alpha(), (60, 20))
        self.bg = pygame.image.load('./asset/Level2Bg0.png').convert_alpha()

    def info_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('./asset/BALOOBHAIJAAN-REGULAR.TTF', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        while True:
            self.window.blit(self.bg, (0, 0))
            self.info_text(25, "Faça pontos comendo minhocas", C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT - 295))
            self.info_text(25, "e fuja dos inimigos!", C_WHITE,(WIN_WIDTH / 2, WIN_HEIGHT - 265))
            self.window.blit(self.e1, (WIN_WIDTH * 0.30, 95))
            self.info_text(22, f"Dano: -{ENTITY_DAMAGE['Enemy1']}", C_RED, (WIN_WIDTH * 0.20, 110))
            self.window.blit(self.e2, (WIN_WIDTH * 0.37 - 40, 145))
            self.info_text(22, f"Dano: -{ENTITY_DAMAGE['Enemy2']}", C_RED, (WIN_WIDTH * 0.20, 180))
            self.window.blit(self.e3, (WIN_WIDTH * 0.76, 155))
            self.info_text(22, f"Dano: -{ENTITY_DAMAGE['Enemy3']}", C_RED, (WIN_WIDTH * 0.65, 180))
            self.window.blit(self.e4, (WIN_WIDTH * 0.76, 85))
            self.info_text(22, f"Dano: -{ENTITY_DAMAGE['Enemy4']}", C_RED, (WIN_WIDTH * 0.65, 110))
            self.window.blit(self.e5, (WIN_WIDTH / 2 + 10, 235))
            self.info_text(22, f"Vida: +{-ENTITY_DAMAGE['Enemy5']}", C_GREEN, (WIN_WIDTH / 2 - 50, 245))
            self.info_text(25, "aperte ENTER para iniciar!", C_WHITE, (WIN_WIDTH / 2 - 10, WIN_HEIGHT - 30))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        return
            pygame.display.flip()