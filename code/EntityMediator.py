#!/usr/bin/python
# -*- coding: utf-8 -*-
from pstats import Stats

from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_collision = False
        if isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_collision = True
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_collision = True

        if valid_collision:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):

                if isinstance(ent1, Player):
                    ent1.apply_damage(ent2.damage)
                    if ent2.damage < 0:
                        ent2.health = 0
                        ent1.score += 1

                elif isinstance(ent2, Player):
                    ent2.apply_damage(ent1.damage)
                    if ent1.damage < 0:
                        ent1.health = 0
                        ent2.score += 1

                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range (len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_hit == 'Player1':
            ent.score += enemy.score