import pyxel
from abc import ABC, abstractmethod


class Rectangle(ABC):
    """
    Draw rectangle at x,y with width and height
    sx, sy : screen width and height
    """
    @property
    def left(self):
        return self.x - self.width // 2

    @property
    def right(self):
        return self.x + self.width // 2

    @property
    def top(self):
        return self.y - self.height // 2

    @property
    def bottom(self):
        return self.y + self.height // 2

    def __init__(self, x, y, width, height, sx, sy, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sx = sx
        self.sy = sy
        self.colour = colour

    def draw(self):
        pyxel.rect(self.left, self.top, self.width, self.height, self.colour)

    @abstractmethod
    def update(self):
        pass


class Paddle(Rectangle):
    colour = 1
    width = 20
    height = 4
    margin = 1  # shift if we get stuck
    keys = {pyxel.KEY_A: -2,
            pyxel.KEY_D: 2}

    def __init__(self, screen_size):
        sx, sy = screen_size
        super().__init__(sx // 2, int(sy*0.9), 
                         Paddle.width, Paddle.height, 
                         sx, sy, Paddle.colour)
        self.vx = 0

    def update(self):
        for key in Paddle.keys:
            if pyxel.btnp(key):
                self.vx = Paddle.keys[key]
            if pyxel.btnr(key):
                self.vx = 0
        self.x += self.vx

        if self.left <= 0:
            self.x = self.width // 2 + Paddle.margin
        elif self.right >= self.sx:
            self.x = self.sx - self.width // 2 - Paddle.margin
