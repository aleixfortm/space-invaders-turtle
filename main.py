from turtle import Screen
from spaceship import Spaceship
from alien import Alien
from scoreboard import Lives, Score
from stars import Star

import random
import time

# EDITABLE CONSTANTS
N_LIVES = 3
N_ALIENS = 12

# Create variables and empty arrays
aliens = []
to_be_deleted_aliens = []
spawnpoints = []

# Screen setup
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=800)
screen.tracer(0)

# Draw stars
n_stars = random.randint(40, 80)
for _ in range(n_stars):
    x = random.randint(-300, 300)
    y = random.randint(-400, 350)
    star = Star(x, y)

# Create objects
ship = Spaceship(N_LIVES)
lives = Lives(N_LIVES)
score = Score()

# Scoreboard setup
lives.draw_line()
score.display_score()

# Generate alien spawnpoints
for i in range(N_ALIENS):
    spawnpoints.append(i * 60)
    spawnpoints.append(i * 60)

# Create an alien object for every spawnpoint
x = None
for _ in range(N_ALIENS):
        alien = Alien(positions=spawnpoints)
        aliens.append(alien)
        spawnpoints, x = alien.spawn(x)

# Set up timer
init_time = time.time()


def reset_timer():
    global init_time
    init_time = time.time()


def elapsed_time():
    return round(time.time() - init_time, 2)


# Set up controls
screen.listen()
screen.onkey(ship.move_left, 'Left')
screen.onkey(ship.move_right, 'Right')
screen.onkey(ship.check_projectiles, 'Up')
screen.onkey(lives.decrease_life, 'c')

# Main loop
iteration = 0
invulnerable = False
game_is_on = True

while game_is_on:
    # Advance projectiles
    ship.advance_projectiles()
    for alien in aliens:
        alien.try_projectile()

    # Delete out-of-range player projectiles
    if ship.projectiles:
        if ship.projectiles[0].ycor() > 340:
            ship.remove_projectile()
    # Delete out-of-range enemy projectiles
    for alien in aliens:
        for enemy_proj in alien.projectiles:
            if enemy_proj.ycor() < -400:
                alien.remove_projectile(enemy_proj)

    # Ship projectile collision with enemy ships
    for proj in ship.projectiles:
        for alien in aliens:
            if proj.distance(alien) < 15 and alien not in to_be_deleted_aliens:
                alien.stop_shooting()
                to_be_deleted_aliens.append(alien)
                score.increase_score(10)

    # Alien projectile collision with player
    if not invulnerable:
        for alien in aliens:
            for enemy_proj in alien.projectiles:
                if enemy_proj.distance(ship) < 15:
                    ship.decrease_lives()  # -- Potentially useless instruction
                    lives.decrease_life()
                    alien.remove_projectile(enemy_proj)
                    invulnerable = True  # Makes player invulnerable for a short time
                    reset_timer()
                    if ship.lives == 0:
                        game_is_on = False

    # Check to-be-deleted aliens
    if to_be_deleted_aliens:  # If not empty
        for alien in to_be_deleted_aliens:
            if not alien.projectiles:  # If no existing projectiles on-screen
                to_be_deleted_aliens.remove(alien)
                aliens.remove(alien)

    # Invulnerability timer
    if invulnerable:
        ship.flicker(elapsed_time())
        if elapsed_time() > 2:
            invulnerable = False

    # Loop debugger
    if iteration % 100 == 0:
        pass

    # Update changes to screen
    score.display_score()
    screen.update()
    time.sleep(0.0001)
    iteration += 1

ship.game_over()

screen.exitonclick()
