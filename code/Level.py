#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import pygame
from pygame import Rect
from pygame.font import Font
from pygame.surface import Surface
from code.Const import MENU_OPTION, C_ORANGE, TIMEOUT_LEVEL, TIMEOUT_STEP, EVENT_TIMEOUT, EVENT_ENEMY, C_WHITE, \
    WIN_HEIGHT, SPAWN_TIME, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player


class Level:
    def __init__(self,window: Surface, name: str, game_mode: str):
        self.window = window
        self.timeout = TIMEOUT_LEVEL
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name))
        player = EntityFactory.get_entity('Player1')
        self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)


    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                ent.animation()
                if ent.name == 'Player1':
                    self.level_text(20, f'VIDA: {ent.health} | MINHOCAS: ', C_ORANGE, (10, 30))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False
            self.level_text(20, f'TEMPO: {self.timeout / 1000:.1f}s', C_ORANGE, (10, 10))
            self.level_text(20, f'fps: {clock.get_fps():.0f}', C_WHITE, (WIN_WIDTH - 70, WIN_HEIGHT - 30))
            self.level_text(20, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 30))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font('./asset/BALOOBHAIJAAN-REGULAR.TTF', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

