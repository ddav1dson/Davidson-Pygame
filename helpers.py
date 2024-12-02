import pygame
from random import randint
from enemy_tank import EnemyTank
from tank import Tank

pygame.init()
WIDTH = 1280
HEIGHT = 720
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

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
        background.blit(green_tree_large, coords)

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

    return background

def kill_tanks(tank_group, bullet_group, score, num_tanks):
        # check for bullets hitting ships
    coll_dict = pygame.sprite.groupcollide(tank_group,bullet_group,0,0)
    # check and see if a bullet collides with something that is not its mother
    for t,bs in coll_dict.items():
        # tank is k, bullet list is v
        # check for non empty values
        if bs:
            #loop over each bullet check its mom
            for b in bs:
                # check if bullet.mom is the tank
                if b.mom != t:
                    # kill the tank
                    b.kill()
                    t.explode()
                    # update the score
                    score[0] += 1
                    # increase the number of spawned ships by chance
                    if randint(0,10)<3:
                        num_tanks[0]+=1

# make an instructions screen
def make_instructions(screen):
    # black screen
    screen.fill(black)
    instructions = [
        '',
        'Tank Busters',
        'Use W, A, S, D to move your tank',
        'Press Spacebar to shoot your cannon',
        'Aim with the mouse',
        'Enemies can spawn anywhere so stay mobile!',
        '**Press Any Key To Play**'
    ]
    # make an instruction font
    i_font = pygame.font.Font('kenney_fonts\Fonts\Kenney Blocks.ttf',size=40)
    spacing = 80
    # render (make surface) for each instruction
    for ii in range(len(instructions)):
        # render the font
        font_surf = i_font.render(instructions[ii], True, white)
        # get a rect
        font_rect = font_surf.get_rect()
        font_rect.center = (WIDTH//2, spacing + ii * spacing)
        # blit it to the screen
        screen.blit(font_surf, font_rect)

def make_death_screen(screen):
    # black screen
    screen.fill(black)
    instructions = [
        '',
        '',
        '',
        'Your tank was busted!'
    ]
    # make an instruction font
    i_font = pygame.font.Font('kenney_fonts\Fonts\Kenney Blocks.ttf',size=60)
    spacing = 80
    # render (make surface) for each instruction
    for ii in range(len(instructions)):
        # render the font
        font_surf = i_font.render(instructions[ii], True, red)
        # get a rect
        font_rect = font_surf.get_rect()
        font_rect.center = (WIDTH//2, spacing + ii * spacing)
        # blit it to the screen
        screen.blit(font_surf, font_rect)
    
