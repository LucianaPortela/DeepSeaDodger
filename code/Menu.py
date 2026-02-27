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
        self.sound_select = pygame.mixer.Sound('./asset/MenuSelection.wav')
        self.sound_select.set_volume(0.2)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, font_name: str, ):
        text_font: Font = pygame.font.Font(f'./asset/{font_name}', text_size)
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
            self.menu_text(75, "Deep Sea", C_BLUE, ((WIN_WIDTH / 2), 60), 'BROTHERBOLD.OTF')
            self.menu_text(65, "Dodge", C_BLUE, ((WIN_WIDTH / 2), 120), 'BROTHERBOLD.OTF')
            self.menu_text(30, "Controles", C_WHITE, (90, 195), 'Ithaca.ttf')
            self.menu_text(27, "W", C_ORANGE, (90, 245), 'Ithaca.ttf')
            self.menu_text(20, "sobe", C_WHITE, (90, 225), 'Ithaca.ttf')
            self.menu_text(27, "A", C_ORANGE, (75, 260), 'Ithaca.ttf')
            self.menu_text(20, "recua", C_WHITE, (45, 260), 'Ithaca.ttf')
            self.menu_text(27, "D", C_ORANGE, (105, 260), 'Ithaca.ttf')
            self.menu_text(20, "avança", C_WHITE, (140, 260), 'Ithaca.ttf')
            self.menu_text(27, "S", C_ORANGE, (90, 275), 'Ithaca.ttf')
            self.menu_text(20, "desce", C_WHITE, (90, 295), 'Ithaca.ttf')
            self.menu_text(30, "Aperte ENTER", C_WHITE, (470, 220), 'Ithaca.ttf')
            self.menu_text(30, "para selecionar", C_WHITE, (470, 245), 'Ithaca.ttf')
            self.menu_text(15, "Desenvolvido por", C_ORANGE, (470, 280), 'Ithaca.ttf')
            self.menu_text(15, "Luciana Portela", C_ORANGE, (470, 295), 'Ithaca.ttf')
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    text_rect = self.menu_text(50, MENU_OPTION[i], C_ORANGE, ((WIN_WIDTH / 2), 200 + 40 * i),
                                               'Ithaca.ttf')
                    icon_rect = self.player_icon.get_rect()
                    icon_rect.right = text_rect.left - 10
                    icon_rect.centery = text_rect.centery - 5
                    self.window.blit(self.player_icon, icon_rect)
                else:
                    self.menu_text(40, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 40 * i), 'Ithaca.ttf')
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_w:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        self.sound_select.play()
                        return MENU_OPTION[menu_option]
