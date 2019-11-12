import pyxel
from paddle import Paddle


class App:
    screen_size = (160, 120)

    @property
    def objects(self):
        yield self.paddle

    def __init__(self):
        pyxel.init(*App.screen_size)
        self.paddle = Paddle(App.screen_size)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        for obj in self.objects:
            obj.update()

    def draw(self):
        pyxel.cls(0)
        for obj in self.objects:
            obj.draw()
        


if __name__ == "__main__":
    App()