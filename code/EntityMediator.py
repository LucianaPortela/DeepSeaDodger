from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:
    @staticmethod
    def __check_screen_limits(ent: Entity):
        # Remove enemies once they are off the screen
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __check_hitbox(e1: Entity, e2: Entity):
        # Only process collisions between a Player, Enemies or Worms
        player = None
        enemy = None

        if isinstance(e1, Player) and isinstance(e2, Enemy):
            player, enemy = e1, e2
        elif isinstance(e1, Enemy) and isinstance(e2, Player):
            player, enemy = e2, e1

        # All sides collision detection
        if player and enemy:
            if player.rect.colliderect(enemy.rect):
                # Apply interaction of damage or heal
                player.apply_damage(enemy.damage)

                # If the enemy is a Worm, it must be removed after the collision
                if enemy.damage < 0:
                    enemy.health = 0
                    player.score += 1  # Count Worms

    @staticmethod
    def check_collision(entity_list: list[Entity]):
        # Iterate through the list to check screen limits
        for i in range(len(entity_list)):
            ent1 = entity_list[i]
            EntityMediator.__check_screen_limits(ent1)
            for j in range(i + 1, len(entity_list)):
                ent2 = entity_list[j]
                EntityMediator.__check_hitbox(ent1, ent2)

    @staticmethod
    def check_health(entity_list: list[Entity]):
        # Remove dead entities
        for ent in entity_list[:]:
            if ent.health <= 0:
                entity_list.remove(ent)
