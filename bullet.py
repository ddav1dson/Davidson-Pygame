import pygame
from math import sin, cos, radians

# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen,mom, x,y,theta,speed = 7):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = speed
        self.theta = theta # degrees
        self.base_image = pygame.image.load('tiny_tanks/PNG/Tiles/bulletRed3_outline.png')
        self.image = pygame.transform.scale_by(self.base_image, 1.25)
        self.orig_image = self.image
        self.rect = self.image.get_rect()
        # place the bullet
        self.rect.center = (self.x,self.y)
        self.screen = screen
        print(screen)
        self.screen_rect = screen.get_rect()
        self.mom = mom
        

    def update(self):
        dx = self.speed * cos(radians(self.theta))
        dy = self.speed * sin(radians(self.theta))

        # set initial position before moving
        self.initial_x = self.x
        self.initial_y = self.y

        self.x += dx
        self.y -= dy
        # update the rect
        self.rect.center = (self.x,self.y)
        
        # Rotate the bullet so it faces the direction it is shot
        rotated_image = pygame.transform.rotate(self.orig_image, self.theta - 90)  # - 90 so it faces the right direction
        
        # Get the new rect for the rotated image and adjust position
        self.rect = rotated_image.get_rect(center=self.rect.center)
        
        # Update the image to the rotated one
        self.image = rotated_image
        
        # check if the bullet is inside the screen
        if not self.screen_rect.contains(self.rect):
            # remove the bullet
            self.kill()

        #check r,g,b value for obstacle
        r,g,b,_ = screen.get_at(self.rect.center)
        # check the r g and b to see if we are hitting an obstacles
        if r in range(50,92) or r in range(140, 245) and g in range (70,80) or range(137,225) and b in range (55,65) or range(100,180):
            pass
        else:
            self.kill()
    
    # kill bullets when they hit an obstacle.
    def check_obstacle(self):
        #check r,g,b value for obstacle
        r,g,b,_ = screen.get_at(self.rect.center)

        # check the r g and b to see if we are hitting an obstacles
        if r in range(50,75) or r in range(120, 245) and g in range(137,225) and b in range(100,180):
            pass
        else:
            self.kill()
            
