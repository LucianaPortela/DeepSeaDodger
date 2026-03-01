from code.Entity import Entity
from code.Const import DISPLAY_WIDTH, MOVEMENT_SPEED


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    # Scrolls the background and make a parallax effect
    def move(self):
        self.rect.centerx -= MOVEMENT_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = DISPLAY_WIDTH
