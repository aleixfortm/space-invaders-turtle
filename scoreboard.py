from turtle import Turtle

N_LIVES = 3


class Lives(Turtle):

    def __init__(self, n_lives=N_LIVES):
        super().__init__()
        self.draw_line()
        self.lives = []
        self.x_pos = 280
        self.n_lives = n_lives
        self.remaining_lives = n_lives
        self.create_lives()

    def create_lives(self):
        for life in range(self.n_lives):
            life = Turtle()
            life.color('white')
            life.shapesize(1.5)
            life.penup()
            life.fillcolor('white')
            self.lives.append(life)
        self.draw_lives()

    def draw_lives(self):
        self.showturtle()
        for life in self.lives:
            life.setpos(self.x_pos, 370)
            self.x_pos -= 17
        self.write_text()

    def draw_line(self):
        self.ht()
        self.penup()
        self.pencolor('white')
        self.pensize(2)
        self.goto(-300, 350)
        self.pendown()
        self.goto(300, 350)
        self.penup()

    def write_text(self):
        self.setx(self.xcor() - 65)
        self.sety(self.ycor() + 32)
        self.write('Remaining lives:', align='center', font=('verdana', 10, 'normal'))

    def decrease_life(self):
        self.remaining_lives -= 1
        i = self.remaining_lives
        self.lives[i].fillcolor('black')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.color('white')
        self.goto(0, 360)

    def display_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Verdana', 24, 'normal'))

    def increase_score(self, amount=10):
        self.score += amount
