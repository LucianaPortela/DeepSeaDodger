import pygame
from code.Entity import Entity
from code.Const import DISPLAY_HEIGHT, DISPLAY_WIDTH, MOVEMENT_SPEED, PLAYER_KEY_RIGHT, PLAYER_KEY_LEFT, \
    PLAYER_KEY_DOWN, PLAYER_KEY_UP


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.sound_eat = pygame.mixer.Sound('./asset/Point.wav')
        self.sound_eat.set_volume(0.3)
        self.sound_damage = pygame.mixer.Sound('./asset/Attack.wav')
        self.sound_damage.set_volume(0.3)

    def move(self):
        # Update player position based on key inputs respecting screen limits
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= MOVEMENT_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < DISPLAY_HEIGHT:
            self.rect.centery += MOVEMENT_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= MOVEMENT_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < DISPLAY_WIDTH:
            self.rect.centerx += MOVEMENT_SPEED[self.name]
        pass

    def apply_damage(self, damage):
        if damage < 0:
            self.health -= damage  # Restore health from worm
            self.sound_eat.play()  # Play score point sound effect
            return True
        elif damage > 0:
            # Apply damage only if the invincibility cooldown has passed
            current_time = pygame.time.get_ticks()
            if current_time - self.last_hit > self.damage_delay:
                self.health -= damage
                self.last_hit = current_time
                self.sound_damage.play()  # Play the damage sound effect
                return True
        return False
