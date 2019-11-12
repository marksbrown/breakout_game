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

    def __init__(self, x, y, width, height, sx, sy, colour, **kwargs):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sx = sx
        self.sy = sy
        self.colour = colour
        self.debug = kwargs.get('debug', True)
        self.verbose = kwargs.get('verbose', False)

    def draw(self):
        pyxel.rect(self.left, self.top, self.width, self.height, self.colour)

    @abstractmethod
    def update(self):
        pass


class Ball(Rectangle):
    colour = 2
    radius = 2
    margin = 2  # shift if we get stuck
    max_speed = 5

    def __init__(self, screen_size):
        sx, sy = screen_size
        super().__init__(sx // 2, sy // 2,
                         Paddle.width, Paddle.height,
                         sx, sy, Paddle.colour)
        self.vx = 1
        self.vy = 2
    
    def draw(self):
        pyxel.circb(self.left, self.top, Ball.radius, Ball.colour)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        if self.left < 0:
            self.x = self.margin + self.radius
            self.vx *= -1
        if self.right > self.sx:
            self.x = self.sx - self.margin - self.radius
            self.vx *= -1
        if self.top < 0:
            self.y = self.margin + self.radius
            self.vy *= -1
        if self.bottom >= self.sy:
            # TODO implement game over criteria
            if self.debug:
                self.y = self.sy - self.margin - self.radius
                self.vy *= -1
            else:
                pyxel.quit()  # GAME OVER!


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
