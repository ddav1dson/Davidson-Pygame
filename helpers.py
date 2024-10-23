import pygame

def build_background(WIDTH, HEIGHT):
    # Create the Background
    background = pygame.Surface((WIDTH,HEIGHT))
    background.fill((255,0,0))

    # Load the Tiles
    grass = pygame.image.load('tiny_tanks/PNG/Tiles/tileGrass1.png')
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
            if x == 1/2*WIDTH:
                background.blit(grass_and_sand, (x,y))
            elif x < 1/2*WIDTH:
                background.blit(sand, (x,y))
    for x in range(0, WIDTH//2):
        background.blit(sand_road_horizontal, (x,360))
    for x in range(0, WIDTH):
        if x > WIDTH//2:
            background.blit(grass_road_horizontal, (x,360))
        
    background.blit(grass_and_sand_road_horizontal, (640,360))

    return background