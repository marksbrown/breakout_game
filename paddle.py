import pyxel

class Rectangle:
    """
    Draw rectangle at x,y with width and height
    """


class Paddle:
    colour = 1
    width = 50
    height = 10

    def __init__(self, screen_size):
        self.sx, self.sy = screen_size
        self.x = self.sx // 2