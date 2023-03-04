from turtle import Turtle
INITIAL_Y_POS = -250


class Spaceship(Turtle):

    def __init__(self, lives=3):
        super().__init__()
        self.projectiles = []
        self.color('white')
        self.lives = lives
        self.penup()
        self.shapesize(2)
        self.settiltangle(90)
        self.goto(0, INITIAL_Y_POS)
        self.fillcolor('white')
        self.speed(0)

    def move_right(self):
        if self.xcor() <= 270:
            self.setx(self.xcor() + 20)

    def move_left(self):
        if self.xcor() >= -270:
            self.setx(self.xcor() - 20)

    def advance_projectiles(self):
        # Advance projectiles
        for projectile in self.projectiles:
            projectile.forward(3)

    def remove_projectile(self):
        self.projectiles[0].clear()
        self.projectiles[0].ht()
        self.projectiles.remove(self.projectiles[0])

    def create_projectile(self):
        # Create projectile object
            projectile = Turtle()
            projectile.penup()
            projectile.color('blue')
            projectile.shape('square')
            projectile.shapesize(0.5)
            projectile.seth(90)
            projectile.shapesize(stretch_len=1, stretch_wid=0.1)
            projectile.setx(self.xcor())
            projectile.sety(self.ycor())
            self.projectiles.append(projectile)

    def check_projectiles(self):
        if not self.projectiles:
            self.create_projectile()
        elif self.projectiles[-1].ycor() > 0:
            self.create_projectile()

    def decrease_lives(self):
        self.lives -= 1

    def flicker(self, elapsed_time):
        if elapsed_time < 0.2:
            self.ht()
        elif elapsed_time < 0.4:
            self.st()
        elif elapsed_time < 0.8:
            self.ht()
        elif elapsed_time < 1:
            self.st()

