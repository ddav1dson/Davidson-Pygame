import pygame
from helpers import build_background
from tank import Tank
# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# import background
background = build_background(WIDTH, HEIGHT)

# make a sprite group
tank_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group() 

# create the tanks
player1 = Tank(screen, 200,200, WIDTH, HEIGHT, bullet_group)
enemy1 = Tank(screen, 400,200, WIDTH, HEIGHT, bullet_group, color = 'enemy')

# add our sprite to the sprite group
tank_group.add(player1)
tank_group.add(enemy1)
# Render your game here


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    #player1.update()
    player1.update()
    player1.rotate_turret(mouse_x, mouse_y)

    bullet_group.update()
    #tank_group.update()
    # check for collision
    has_collided = pygame.sprite.collide_rect(player1,enemy1)
    
    if has_collided:
        enemy1.kill()
    player1.check_keys()

    # Blit the background to the screen
    screen.blit(background,(0,0))   
    player1.draw(screen)
    bullet_group.draw(screen)
 
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()