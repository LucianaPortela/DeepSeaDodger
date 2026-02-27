#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import pygame
from pygame import Rect
from pygame.font import Font
from pygame.surface import Surface
from code.Const import C_ORANGE, TIMEOUT_LEVEL, TIMEOUT_STEP, EVENT_TIMEOUT, EVENT_ENEMY, C_WHITE, \
    WIN_HEIGHT, SPAWN_TIME, WIN_WIDTH, ENTITY_HEALTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int], player_position: list, player_health: list[int]):
        self.window = window
        self.timeout = TIMEOUT_LEVEL
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name))
        self.spawn_time = SPAWN_TIME.get(self.name)
        self.player_health = player_health
        pygame.time.set_timer(EVENT_ENEMY, self.spawn_time)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        player.rect.left = player_position[0]
        player.rect.top = player_position[1]
        player.health = player_health[0]
        self.entity_list.append(player)
        self.player_position = player_position

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font('./asset/BALOOBHAIJAAN-REGULAR.TTF', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)


    def run(self, player_score: list[int]):
        clock = pygame.time.Clock()
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(-1)
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                ent.animation()
                if ent.name == 'Player1':
                    self.level_text(20, f'VIDA: {ent.health}', C_ORANGE, (10, 30))
                    self.level_text(20, f'MINHOCAS: {ent.score}', C_ORANGE, (10, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    if self.name == 'Level1':
                        choice = random.choice(('Enemy1', 'Enemy5'))
                    elif self.name == 'Level2':
                        choice = random.choice(('Enemy2', 'Enemy4', 'Enemy5'))
                    elif self.name == 'Level3':
                        choice = random.choice(('Enemy2', 'Enemy3', 'Enemy3', 'Enemy3', 'Enemy3', 'Enemy3', 'Enemy5'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.spawn_time > 500:
                        self.spawn_time -= 50
                        pygame.time.set_timer(EVENT_ENEMY, self.spawn_time)

                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                                self.player_position[0] = ent.rect.left
                                self.player_position[1] = ent.rect.top
                                self.player_health[0] = ent.health
                        return True

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

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)


