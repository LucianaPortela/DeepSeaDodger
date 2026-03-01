import sys
import random
import pygame
from pygame.surface import Surface
from code.Const import TIMEOUT_LEVEL, TIMEOUT_STEP, EVENT_TIMEOUT, EVENT_ENEMY, C_WHITE, \
    DISPLAY_HEIGHT, SPAWN_TIME, DISPLAY_WIDTH, C_RED
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.GameOver import GameOver
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int], player_position: list,
                 player_health: list[int]):
        self.window = window
        self.timeout = TIMEOUT_LEVEL
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name))
        self.spawn_time = SPAWN_TIME.get(self.name)
        self.player_health = player_health
        player = EntityFactory.get_entity('Player')
        player.score = player_score[0]
        player.rect.left = player_position[0]
        player.rect.top = player_position[1]
        player.health = player_health[0]
        pygame.time.set_timer(EVENT_ENEMY, self.spawn_time)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)
        self.entity_list.append(player)
        self.player_position = player_position
        self.font_main = pygame.font.Font('./asset/Ithaca.ttf', 30)
        self.font_small = pygame.font.Font('./asset/Ithaca.ttf', 15)
        # Load and prepare HUD icons for life, score, and timer display
        self.icon_time = pygame.image.load('./asset/Time.png').convert_alpha()
        self.icon_time = pygame.transform.scale(self.icon_time, (15, 20))
        self.icon_heart = pygame.image.load('./asset/Heart.png').convert_alpha()
        self.icon_heart = pygame.transform.scale(self.icon_heart, (20, 20))
        self.icon_worm = pygame.image.load('./asset/Worm.png').convert_alpha()
        self.icon_worm = pygame.transform.scale(self.icon_worm, (20, 20))

    def level_text(self, font, text: str, text_color: tuple, text_pos: tuple):
        text_surf = font.render(text, True, text_color).convert_alpha()
        self.window.blit(source=text_surf, dest=text_pos)

    def run(self, player_score: list[int]):
        clock = pygame.time.Clock()
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(-1)  # Music level loop
        while True:
            clock.tick(60)  # Limit the frame ratio in 60 FPS
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                ent.animation()  # Animate sprites
            for ent in self.entity_list:
                if ent.name == 'Player':
                    # Timer
                    self.window.blit(self.icon_time, (10, 10))
                    self.level_text(self.font_main, f'{self.timeout / 1000:.1f}s', C_RED, (35, 5))
                    # Life
                    self.window.blit(self.icon_heart, (10, 35))
                    self.level_text(self.font_main, f'{ent.health}', C_RED, (35, 30))
                    # Worms
                    self.window.blit(self.icon_worm, (10, 60))
                    self.level_text(self.font_main, f'{ent.score}', C_RED, (35, 55))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    if self.name == 'Level1':
                        choice = random.choice(('Turtle', 'Worm'))
                    elif self.name == 'Level2':
                        choice = random.choice(('Shark', 'Octopus', 'Worm'))
                    elif self.name == 'Level3':
                        # Randomly select enemies based on the current level difficulty
                        choice = random.choice(
                            ('Shark', 'Anglerfish', 'Anglerfish', 'Anglerfish', 'Anglerfish', 'Anglerfish', 'Worm'))
                    self.entity_list.append(EntityFactory.get_entity(choice))  # Randomly spawn selected enemies

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    # Decrease spawn delay as time runs out to increase enemy density making more difficult
                    if self.spawn_time > 500:
                        self.spawn_time -= 50
                        pygame.time.set_timer(EVENT_ENEMY, self.spawn_time)
                        # Create a 1 sec fadeout effect on music when the level is almost over
                    if self.timeout == 1000:
                        pygame.mixer_music.fadeout(1000)

                    if self.timeout == 0:
                        # Save the exact position, score and health of player to continue in the next level
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player':
                                player_score[0] = ent.score
                                self.player_position[0] = ent.rect.left
                                self.player_position[1] = ent.rect.top
                                self.player_health[0] = ent.health
                        return True

                alive = False
                # Check if the player still alive
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        alive = True
                # If its dead, show the GameOver screen
                if not alive:
                    game_over = GameOver(self.window)
                    game_over.run()
                    return False
            # Display FPS and entities
            self.level_text(self.font_small, f'fps: {clock.get_fps():.0f}', C_WHITE,
                            (DISPLAY_WIDTH - 60, DISPLAY_HEIGHT - 20))
            self.level_text(self.font_small, f'entidades: {len(self.entity_list)}', C_WHITE, (10, DISPLAY_HEIGHT - 20))
            pygame.display.flip()

            EntityMediator.check_collision(entity_list=self.entity_list)
            EntityMediator.check_health(entity_list=self.entity_list)
