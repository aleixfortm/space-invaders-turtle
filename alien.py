from turtle import Turtle
import random


class Alien(Turtle):

    def __init__(self, positions, shoot_flag=True):
        super().__init__()
        self.y_positions = positions
        self.shoot_projectiles = shoot_flag
        self.projectiles = []
        self.color('white')
        self.seth(270)
        self.shapesize(3)
        self.penup()

    def spawn(self):
        y = random.choice(self.y_positions)
        self.y_positions.remove(y)
        x = random.randint(-270, 270)
        self.setpos(x, y)
        return self.y_positions

    def try_projectile(self):
        if self.shoot_projectiles:
            chance = random.randint(1, 60)
            if chance == 1 and not self.projectiles:
                self.create_projectile()
            if chance == 1 and self.projectiles[-1].ycor() <= self.ycor() - 100:
                self.create_projectile()
        self.advance_projectile()

    def advance_projectile(self):
        if self.projectiles:
            # Advance projectiles
            for projectile in self.projectiles:
                projectile.forward(2)

    def create_projectile(self):
        projectile = Turtle()
        projectile.penup()
        projectile.color('white')
        projectile.shape('square')
        projectile.shapesize(0.5)
        projectile.seth(270)
        projectile.shapesize(stretch_len=1, stretch_wid=0.1)
        projectile.setx(self.xcor())
        projectile.sety(self.ycor())
        self.projectiles.append(projectile)

    def stop_shooting(self):
        self.ht()
        self.shoot_projectiles = False

    def remove_projectile(self, proj_object):
        i = self.projectiles.index(proj_object)
        self.projectiles[i].clear()
        self.projectiles[i].ht()
        self.projectiles.remove(proj_object)


