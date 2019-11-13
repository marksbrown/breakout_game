import pyxel
from objects import Paddle, Ball


class Background:
    def __init__(self, screen_size, margin=10, colour=1):
        self.sx, self.sy = screen_size
        self.margin = margin
        self.colour = colour

    def draw_border(self):
        """
        Draw border between four corners
        """
        top_left = (self.margin, self.margin)
        top_right = (self.sx - self.margin, self.margin)
        bottom_right = (self.sx - self.margin, self.sy - self.margin)
        bottom_left = (self.margin, self.sy - self.margin)
        pyxel.line(*top_left, *top_right, self.colour)
        pyxel.line(*top_right, *bottom_right, self.colour)
        pyxel.line(*bottom_right, *bottom_left, self.colour)
        pyxel.line(*bottom_left, *top_left, self.colour)

    def draw(self):
        pyxel.cls(0)
        self.draw_border()

    def update(self):
        pass


class App:
    screen_size = (160, 120)
    margin = 10

    @property
    def objects(self):
        yield self.paddle
        yield self.ball

    def __init__(self):
        pyxel.init(*App.screen_size)
        self.background = Background(App.screen_size, App.margin)
        self.ball = Ball(App.screen_size, App.margin)
        self.paddle = Paddle(App.screen_size, App.margin)
        
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        for obj in self.objects:
            obj.update()

    def draw(self):
        self.background.draw()
        for obj in self.objects:
            obj.draw()


if __name__ == "__main__":
    App()
