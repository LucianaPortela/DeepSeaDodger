#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.health = None
        self.name = name
        self.index = 0
        self.animation_list = []

        if 'Level' in self.name:
            self.surf = pygame.image.load(f'./asset/{self.name}.png').convert_alpha()
        else:
            for i in range(6):
                image_path = f'./asset/{self.name}Bg{i}.png'
                try:
                    image = pygame.image.load(image_path).convert_alpha()
                    if self.name == 'Player1':
                        image = pygame.transform.scale(image, (30, 30))
                    elif 'Enemy1' in self.name:
                        image = pygame.transform.scale(image, (60, 40))
                    elif 'Enemy2' in self.name:
                        image = pygame.transform.scale(image, (100, 70))
                    elif 'Enemy3' in self.name:
                        image = pygame.transform.scale(image, (50, 70))
                    elif 'Enemy4' in self.name:
                        image = pygame.transform.scale(image, (60, 40))
                    elif 'Enemy5' in self.name:
                        image = pygame.transform.scale(image, (20, 10))

                    self.animation_list.append(image)
                except pygame.error:
                    break
            if self.animation_list:
                self.surf = self.animation_list[0]


        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]

    def animation(self) -> None:
        if self.animation_list:
            self.index += 0.2
            if self.index >= len(self.animation_list):
                self.index = 0
            self.surf = self.animation_list[int(self.index)]

    @abstractmethod
    def move(self) -> None:
        pass