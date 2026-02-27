#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import C_BLUE, MENU_OPTION, C_ORANGE, WIN_WIDTH, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.player_icon = pygame.image.load('./asset/Player1Bg0.png').convert_alpha()
        self.player_icon = pygame.transform.scale(self.player_icon, (25, 20))

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('./asset/BROTHERBOLD.OTF', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        return text_rect
    def button_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('./asset/BALOOBHAIJAAN-REGULAR.TTF', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        return text_rect

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(75, "Deep Sea", C_BLUE, ((WIN_WIDTH / 2), 60))
            self.menu_text(65, "Dodge", C_BLUE, ((WIN_WIDTH / 2), 120))
            self.button_text(20, "Controles", C_WHITE, (90, 205))
            self.button_text(22, "W", C_ORANGE, (90, 245))
            self.button_text(15, "sobe", C_WHITE, (90, 225))
            self.button_text(22, "A", C_ORANGE, (75, 260))
            self.button_text(15, "recua", C_WHITE, (45, 260))
            self.button_text(22, "D", C_ORANGE, (105, 260))
            self.button_text(15, "avança", C_WHITE, (140, 260))
            self.button_text(22, "S", C_ORANGE, (90, 275))
            self.button_text(15, "desce", C_WHITE, (90, 295))
            self.button_text(20, "Menu", C_WHITE, (480, 205))
            self.button_text(30, "▲", C_ORANGE, (480, 230))
            self.button_text(30, "▼", C_ORANGE, (480, 260))
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    text_rect = self.menu_text(35, MENU_OPTION[i], C_ORANGE, ((WIN_WIDTH / 2), 200 + 40 * i))
                    icon_rect = self.player_icon.get_rect()
                    icon_rect.right = text_rect.left - 10
                    icon_rect.centery = text_rect.centery - 5
                    self.window.blit(self.player_icon, icon_rect)
                else:
                    self.menu_text(25, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 40 * i))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]