from turtle import Screen, Turtle


class Background:
    def __init__(self):
        self.screen = Screen()
        self.jack = Turtle()
        self.jack.hideturtle()
        self.screen.setup(width=1000, height=712)
        self.screen.title("World Cup Sweepstakes")
        # image = "images/worldmap_1000.png"
        self.screen.bgpic("images/worldmap_1000.png")
        # self.screen.addshape(image)
        # self.jack.shape(image)
