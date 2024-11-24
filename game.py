import pygame
from helpers import build_background
from tank import Tank
from bullet import Bullet
from enemy_tank import EnemyTank

# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
score = 0

# import background
background = build_background(WIDTH, HEIGHT)

# import decorations
barrel_top = pygame.image.load('tiny_tanks/PNG/Retina/barrelRust_top.png')
barrel_side = pygame.image.load('tiny_tanks/PNG/Retina/barrelRust_side.png')

# get the players rect
player_tank = pygame.image.load('tiny_tanks/PNG/Tiles/tankBody_red.png')
player_rect = player_tank.get_rect()

# get decorations rectangles
barrel_top_rect = barrel_top.get_rect()
barrel_side_rect = barrel_side.get_rect()

# make a sprite group
tank_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
decoration_group = pygame.sprite.Group()

# create the tanks
player1 = Tank(screen, 100,200, WIDTH, HEIGHT, bullet_group, color = 'red')
enemy1 = EnemyTank(player1, screen, 400,200, WIDTH, HEIGHT, bullet_group, color = 'enemy')

# add our sprite to the sprite group
tank_group.add(player1)
tank_group.add(enemy1)
# Render your game here

# make colors
black = (0,0,0)
white = (255,255,255)

# make font

# make an instructions screen
def make_instructions(screen):
    # black screen
    screen.fill(black)
    instructions = [
        'Tank Busters',
        'Use W, A, S, D to move your tank',
        'Press Spacebar to shoot your cannon',
        '',
        '**Press P To Play**'
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
    #get the mouse position
    #mouse_x, mouse_y = pygame.mouse.get_pos()

    tank_group.update()
    bullet_group.update()
    
    # check for bullets hitting tanks
    coll_dict = pygame.sprite.groupcollide(tank_group,bullet_group,0,0)
    # check and see if a bullet collides with something that is not its mother\
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
                    score += 1

    
    # Blit the background to the screen
    screen.blit(background,(0,0))   
    tank_group.draw(screen)
    
    bullet_group.draw(screen)
    
    # Draw the score
    font = pygame.font.Font('kenney_fonts\Fonts\Kenney Blocks.ttf', 36)
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()