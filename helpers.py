import pygame
from random import randint

def build_background(WIDTH, HEIGHT):
    # Create the Background
    background = pygame.Surface((WIDTH,HEIGHT))
    background.fill((255,0,0))

    # get the players rect
    player_tank = pygame.image.load('tiny_tanks/PNG/Tiles/tankBody_red.png')
    player_rect = player_tank.get_rect()

    # Load the Tiles
    grass = pygame.image.load('tiny_tanks/PNG/Tiles/tileGrass1.png')
    sand = pygame.image.load('tiny_tanks/PNG/Tiles/tileSand1.png')
    grass_and_sand = pygame.image.load('tiny_tanks/PNG/Tiles/tileGrass_transitionW.png')
    sand_road_horizontal = pygame.image.load('tiny_tanks/PNG/Tiles/tileSand_roadEast.png')
    sand_road_vertical = pygame.image.load('tiny_tanks/PNG/Tiles/tileSand_roadNorth.png')
    grass_road_horizontal = pygame.image.load('tiny_tanks/PNG/Tiles/tileGrass_roadEast.png')
    grass_road_vertical = pygame.image.load('tiny_tanks/PNG/Tiles/tileGrass_roadNorth.png')
    grass_and_sand_road_horizontal = pygame.image.load('tiny_tanks/PNG/Tiles/tileGrass_roadTransitionW.png')
    
    sandbag = pygame.image.load('tiny_tanks/PNG/Retina/sandbagBrown.png')
    rotated_vertical_sandbag = pygame.transform.rotate(sandbag, 90)
    rotated_right_sandbag = pygame.transform.rotate(sandbag, 45)
    rotated_left_sandbag = pygame.transform.rotate(sandbag, -45)
    sandbag_desert= pygame.image.load('tiny_tanks/PNG/Retina/sandbagBeige.png')
    wood_barricade = pygame.image.load('tiny_tanks/PNG/Retina/barricadeWood.png')
    green_tree_large = pygame.image.load('tiny_tanks/PNG/Retina/treeGreen_large.png')
    brown_tree_large = pygame.image.load('tiny_tanks/PNG/Retina/treeBrown_large.png')
    green_tree_small = pygame.image.load('tiny_tanks/PNG/Retina/treeGreen_small.png')
    brown_tree_small = pygame.image.load('tiny_tanks/PNG/Retina/treeBrown_small.png')
    barrel_top = pygame.image.load('tiny_tanks/PNG/Retina/barrelRust_top.png')
    barrel_side = pygame.image.load('tiny_tanks/PNG/Retina/barrelRust_side.png')
    green_twigs = pygame.image.load('tiny_tanks/PNG/Retina/treeGreen_twigs.png')
    brown_twigs = pygame.image.load('tiny_tanks/PNG/Retina/treeBrown_twigs.png')

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

    #add random trees
    # add some random trees and twigs
    num_trees = 2
    # loop over num trees
    for i in range(num_trees):
        # generate coords
        coords = (randint(WIDTH//2, WIDTH), randint(0,HEIGHT//2))
        # blit the rock on the bg
        background.blit(green_twigs, coords)
    
    for i in range(num_trees):
        # generate coords
        coords = (randint(WIDTH//2, WIDTH), randint(0,HEIGHT//2))
        # blit the rock on the bg
        background.blit(green_tree_large, coords)

    for i in range(num_trees):
        # generate coords
        coords = (randint(0, WIDTH//2), randint(HEIGHT//2,HEIGHT))
        # blit the rock on the bg
        background.blit(brown_twigs, coords)

    for i in range(num_trees):
        # generate coords
        coords = (randint(0, WIDTH//2), randint(HEIGHT//2,HEIGHT))
        # blit the rock on the bg
        background.blit(brown_tree_large, coords)
    #blit background decorations
    background.blit(rotated_vertical_sandbag, (900,500))
    background.blit(rotated_right_sandbag, (900,427))
    background.blit(rotated_left_sandbag, (900,560))
    background.blit(wood_barricade, (WIDTH//2,0))
    background.blit(wood_barricade, (WIDTH//2,55))
    background.blit(wood_barricade, (WIDTH//2,110))
    background.blit(barrel_top, (180,160))
    background.blit(barrel_top, (210,200))
    background.blit(barrel_side, (215,250))
    
    #make decorations obstacles
    barrel_top_rect = barrel_top.get_rect()

    if player_rect.colliderect(barrel_top_rect):
        print(f"collision detected11")
        player_rect.x -= 1

    return background




    
