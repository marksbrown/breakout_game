import pyxel
   

class Rectangle:
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

    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, self.colour)


class Ball:
    colour = 2
    radius = 2
    max_speed = 5

    @property
    def left(self):
        return self.x - Ball.radius

    @property
    def right(self):
        return self.x + Ball.radius

    @property
    def top(self):
        return self.y - Ball.radius

    @property
    def bottom(self):
        return self.y + Ball.radius

    def reset(self):
        """
        Put ball back into starting position
        """
        self.x = self.sx // 2
        self.y = self.sy // 2
        self.vx = 0
        self.vy = 2

    def __init__(self, screen_size, margin):
        self.sx, self.sy = screen_size
        self.margin = margin
        self.reset()

    def draw(self):
        pyxel.circb(self.x, self.y, Ball.radius, Ball.colour)

    def update(self):
        
        if self.left < self.margin or self.right > self.sx - self.margin:
            self.vx *= -1
        if self.top < self.margin or self.bottom > self.sy - self.margin:
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy


class Paddle(Rectangle):
    colour = 1
    width = 20
    height = 4
    margin = 1  # shift if we get stuck
    keys = {pyxel.KEY_A: -2,
            pyxel.KEY_D: 2}

    def reset(self):
        self.x = self.sx // 2
        self.y = int(self.sy * 0.9)
        self.vx = 0

    def __init__(self, screen_size, screen_margin):
        self.sx, self.sy = screen_size
        self.screen_margin = screen_margin
        super().__init__(0, 0, 
                         Paddle.width, Paddle.height, 
                         Paddle.colour)
        self.reset()

    def update(self):
        for key in Paddle.keys:
            if pyxel.btnp(key):
                self.vx = Paddle.keys[key]
            if pyxel.btnr(key):
                self.vx = 0
        self.x += self.vx

        if self.left <= self.screen_margin:
            self.x = self.width // 2 + Paddle.margin
        elif self.right >= self.sx - self.screen_margin:
            self.x = self.sx - self.width // 2 - Paddle.margin
