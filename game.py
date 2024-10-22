# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create the Background
    background = pygame.Surface((WIDTH,HEIGHT))
    background.fill((255,0,0))

    # Load the Tiles
    dirt_floor = pygame.image.load('tiny_dungeon/Tiles/tile_0000.png')     # tile_0000
    stone_wall = pygame.image.load('tiny_dungeon/Tiles/tile_0014.png')
    golem = pygame.image.load('tiny_dungeon/Tiles/tile_0020.png')
    # pygame.transform.scale() to resize a tile
    dirt_floor = pygame.transform.scale(dirt_floor, (32,32))
    stone_wall = pygame.transform.scale(stone_wall, (32,32))
    golem = pygame.transform.scale(stone_wall, (32,32))
    # Create the background
    # Get to the tile_size
    TILE_SIZE = dirt_floor.get_width()

    # loop over x direction
    for x in range(0,WIDTH,TILE_SIZE):
        # loop over y direction
        for y in range(0,HEIGHT, TILE_SIZE):
            # blit the tile to our BG
            background.blit(dirt_floor, (x,y))
            if x<TILE_SIZE:
                background.blit(stone_wall, (x,y))
            #elif x<(2*TILE_SIZE):
               #background.blit(golem, (x,y))

    # RENDER YOUR GAME HERE
    
    # Blit the background to the screen
    screen.blit(background,(0,0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()