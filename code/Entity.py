import pygame
from abc import ABC, abstractmethod
from code.Const import HIT_DAMAGE, SCORE_WORMS, DAMAGE_DELAY, DAMAGE_SPRITE_DELAY, MAX_HP


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.index = 0
        self.speed = 0
        self.damage = HIT_DAMAGE[self.name]
        self.health = MAX_HP[self.name]
        self.score = SCORE_WORMS[self.name]
        self.animation_list = []
        self.last_hit = 0
        self.damage_delay = DAMAGE_DELAY
        self.damage_sprite_delay = DAMAGE_SPRITE_DELAY
        self.hurt_surf = pygame.image.load('./asset/Playerhurt.png').convert_alpha()
        self.hurt_surf = pygame.transform.scale(self.hurt_surf, (40, 30))

        if 'Level' in self.name:
            # Load level background
            self.surf = pygame.image.load(f'./asset/{self.name}.png').convert_alpha()
        else:
            # Load and scales sprites for enemies and player
            for i in range(6):
                image_path = f'./asset/{self.name}Bg{i}.png'
                try:
                    image = pygame.image.load(image_path).convert_alpha()
                    if self.name == 'Player':
                        image = pygame.transform.scale(image, (40, 30))
                    elif 'Turtle' in self.name:
                        image = pygame.transform.scale(image, (80, 60))
                    elif 'Shark' in self.name:
                        image = pygame.transform.scale(image, (180, 100))
                    elif 'Anglerfish' in self.name:
                        image = pygame.transform.scale(image, (80, 60))
                    elif 'Octopus' in self.name:
                        image = pygame.transform.scale(image, (80, 70))
                    elif 'Worm' in self.name:
                        image = pygame.transform.scale(image, (35, 15))
                    self.animation_list.append(image)
                except pygame.error:
                    break

            if self.animation_list:
                self.surf = self.animation_list[0]

        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.health = MAX_HP[self.name]
        self.damage = HIT_DAMAGE[self.name]

    def animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_hit < self.damage_sprite_delay:  # Show a hurt sprite after a hit
            self.surf = self.hurt_surf
            self.surf = pygame.transform.scale(self.surf, (40, 30))
        else:
            if self.animation_list:
                self.index += 0.1  # Speed of frames animation
                if self.index >= len(self.animation_list):
                    self.index = 0
                self.surf = self.animation_list[int(self.index)]

    @abstractmethod
    def move(self) -> None:
        pass
