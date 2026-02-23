#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.index = 0
        self.speed = 0
        self.damage = ENTITY_DAMAGE[self.name]
        self.health = ENTITY_HEALTH[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.animation_list = []
        self.last_hit = 0
        self.damage_delay = 1000
        self.sprite_damage_delay = 200

        if 'Level' in self.name:
            self.surf = pygame.image.load(f'./asset/{self.name}.png').convert_alpha()
        else:
            for i in range(6):
                image_path = f'./asset/{self.name}Bg{i}.png'
                try:
                    image = pygame.image.load(image_path).convert_alpha()
                    if self.name == 'Player1':
                        image = pygame.transform.scale(image, (40,30))
                    elif 'Enemy1' in self.name:
                        image = pygame.transform.scale(image, (80, 60))
                    elif 'Enemy2' in self.name:
                        image = pygame.transform.scale(image, (180, 100))
                    elif 'Enemy3' in self.name:
                        image = pygame.transform.scale(image, (70, 50))
                    elif 'Enemy4' in self.name:
                        image = pygame.transform.scale(image, (80, 70))
                    elif 'Enemy5' in self.name:
                        image = pygame.transform.scale(image, (35, 15))

                    self.animation_list.append(image)
                except pygame.error:
                    break
            if self.animation_list:
                self.surf = self.animation_list[0]


        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]

    def animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_hit < self.sprite_damage_delay:
            try:
                self.surf = pygame.image.load('./asset/Player1hurt.png').convert_alpha()
                self.surf = pygame.transform.scale(self.surf, (30, 30))
            except:
                pass
        else:
            if self.animation_list:
                self.index += 0.1
                if self.index >= len(self.animation_list):
                    self.index = 0
                self.surf = self.animation_list[int(self.index)]

    @abstractmethod
    def move(self) -> None:
        pass