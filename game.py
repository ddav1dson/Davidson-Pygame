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
    grass = pygame.image.load('tiny_tanks/PNG/Tiles/tileGrass1.png')     # tile_0000
    sand = pygame.image.load('tiny_tanks/PNG/Tiles/tileSand1.png')
    grass_and_sand = pygame.image.load('tiny_tanks/PNG/Tiles/tileGrass_transitionW.png')
    sand_road_horizontal = pygame.image.load('tiny_tanks/PNG/Tiles/tileSand_roadEast.png')
    sand_road_vertical = pygame.image.load('tiny_tanks/PNG/Tiles/tileSand_roadNorth.png')
    grass_road_horizontal = pygame.image.load('tiny_tanks/PNG/Tiles/tileGrass_roadEast.png')
    grass_road_vertical = pygame.image.load('tiny_tanks/PNG/Tiles/tileGrass_roadNorth.png')
    grass_and_sand_road_horizontal = pygame.image.load('tiny_tanks/PNG/Tiles/tileGrass_roadTransitionW.png')
    
    # Create the background
    # Get to the tile_size
    TILE_SIZE = grass.get_width()

    # loop over x direction
    for x in range(0,WIDTH,TILE_SIZE):
        # loop over y direction
        for y in range(0,HEIGHT, TILE_SIZE):
            # blit the tile to our BG
            background.blit(grass, (x,y))
            if x == 1/2*WIDTH-64:
                background.blit(grass_and_sand, (x,y))
            elif x < 1/2*WIDTH:
                background.blit(sand, (x,y))
    for x in range(0, WIDTH//2-64):
        background.blit(sand_road_horizontal, (x,360))
    background.blit(grass_and_sand_road_horizontal, (x,360))
    for x in range(0, WIDTH):
        if x > WIDTH//2-2:
            background.blit(grass_road_horizontal, (x,360))
    # RENDER YOUR GAME HERE
    
    # Blit the background to the screen
    screen.blit(background,(0,0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()