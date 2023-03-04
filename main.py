from turtle import Turtle, Screen
from spaceship import Spaceship
from alien import Alien
import time
from scoreboard import Lives, Score

# Create variables and empty arrays
ALIEN_AMOUNT = 5
aliens = []
to_be_deleted_aliens = []
spawnpoints = []

# Screen setup
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=800)
screen.tracer(0)

# Create objects
ship = Spaceship()
lives = Lives()
score = Score()

# Scoreboard setup
lives.draw_line()
score.display_score()

# Generate alien spawnpoints
for i in range(ALIEN_AMOUNT):
    spawnpoints.append(i * 60)
# Create an alien object for every spawnpoint
for _ in range(ALIEN_AMOUNT):
    alien = Alien(positions=spawnpoints)
    aliens.append(alien)
    spawnpoints = alien.spawn()
    print(spawnpoints)

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
        if ship.projectiles[0].ycor() < -320:
            ship.delete_projectile()
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

    # Alien projectile collision with player
    if not invulnerable:
        for alien in aliens:
            for enemy_proj in alien.projectiles:
                if enemy_proj.distance(ship) < 15:
                    ship.decrease_lives()  # -- Potentially useless instruction
                    lives.decrease_life()
                    alien.remove_projectile(enemy_proj)
                    invulnerable = True  # Makes player invulnerable for a short time
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
        print(time.time())
    # Loop debugger
    if iteration % 100 == 0:
        print(len(to_be_deleted_aliens))
        print(len(aliens))

    # Update changes to screen
    screen.update()
    time.sleep(0.001)
    iteration += 1

screen.exitonclick()
