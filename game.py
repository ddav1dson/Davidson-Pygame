import pygame
from helpers import build_background, make_instructions, game_over
from tank import Tank
from bullet import Bullet
from enemy_tank import EnemyTank
from random import randint

# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
score = [0]

# import background
background = build_background(WIDTH, HEIGHT)

# make a sprite group
enemy_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
all_tanks_group = pygame.sprite.Group()

# create the tanks
player1 = Tank(screen, 100,200, WIDTH, HEIGHT, bullet_group, color = 'red')
enemy1 = EnemyTank(player1, screen, 800,HEIGHT//2, WIDTH, HEIGHT, bullet_group, color = 'enemy')

# add our sprite to the sprite group
player_group.add(player1)
enemy_group.add(enemy1)
all_tanks_group.add(player_group)
all_tanks_group.add(enemy_group)

# make colors
black = (0,0,0)
white = (255,255,255)

# spawn tanks in after one tank dies
num_tanks = [0]
def spawn_tanks(WIDTH, HEIGHT, num_tanks, enemy_group):
    # check the number of ships, and spawn more as needed
    # get the number of ships right now
    n = len(enemy_group)
    for i in range(n, num_tanks[0]):
        x = randint(0, WIDTH)
        y = randint(0, HEIGHT)
        speed = randint(1, 5)
        enemy = EnemyTank(player1, screen, x,y, WIDTH, HEIGHT, bullet_group, color='enemy')
        enemy_group.add(enemy)
        
    num_tanks[0] = len(enemy_group)

waiting = 1
# if we see the spacebar, exit the loop (break)
while waiting:
# pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            waiting = 0
        if event.type == pygame.KEYDOWN:
            # if any key pressed, break
            waiting = 0
    
    make_instructions(screen)
    pygame.display.flip()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    spawn_tanks(WIDTH, HEIGHT, num_tanks, enemy_group)

    player_group.update()
    enemy_group.update()
    bullet_group.update()

    # Blit the background to the screen
    screen.blit(background,(0,0))   

    # right now only the background has been created
    # check r,g,b to see if either player or enemy hits an obstacle
    player1.check_obstacle()
    for enemy in enemy_group:
        enemy.check_obstacle()
    # check r,g,b if any bullets hit an obstacle
    [bullet.check_obstacle() for bullet in bullet_group]
    
    # Draw the score
    font = pygame.font.Font('kenney_fonts\Fonts\Kenney Blocks.ttf', 36)
    score_text = font.render(f"Score: {score[0]}", True, black)
    screen.blit(score_text, (10, 10))
    
    #Draw the player, enemies and bullets
    player_group.draw(screen)
    enemy_group.draw(screen)
    bullet_group.draw(screen)

    Tank.kill_tanks(enemy_group, bullet_group, score, num_tanks)
    Tank.kill_tanks(player_group, bullet_group, score, num_tanks)
        
    #game over screen if player dies

    if not player1.alive():
        running = False 
        
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60


#pygame.quit()

death = 1
# if we see the spacebar, exit the loop (break)
while death:
# pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            death = 0

    
    game_over(screen)
    pygame.display.flip()

pygame.quit()