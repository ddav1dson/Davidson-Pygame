# Example file showing a basic pygame "game loop"
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
    
# create the tank
player1 = Tank(200,200, WIDTH, HEIGHT)

background = build_background(WIDTH, HEIGHT)

# Render your game here
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    player1.update()
    player1.check_keys()

    # Blit the background to the screen
    screen.blit(background,(0,0))   
    
    player1.draw(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()