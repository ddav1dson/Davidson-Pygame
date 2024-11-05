from math import cos, sin, pi
import pygame

class Tank():
    def __init__(self, x, y, WIDTH, HEIGHT, theta=180, color='red'):
        self.x = x
        self.y = y
        self.speed = 0
        self.theta = theta # degrees
        self.orig_image = pygame.image.load('tiny_tanks/PNG/Tiles/tank_red.png')
        self.image = self.orig_image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.screen_w = WIDTH
        self.screen_h = HEIGHT
        self.border = 15
    
    def deg_to_rad(self, deg):
        # converts deg to rad
        rad = (deg/180) * pi
        return rad

    def check_keys(self):
        acceleration = 0.5
        max_speed = 3
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.speed -= acceleration
        elif keys[pygame.K_s]:
            self.speed += acceleration
        else: 
            self.speed *= 0.7

        if self.speed > max_speed:
            self.speed = max_speed
        if self.speed < -max_speed:
            self.speed = -max_speed

        if keys[pygame.K_a]:
            self.theta += 1.5
        if keys[pygame.K_d]:
            self.theta -= 1.5

    def check_border(self):
    # check the border and set speed to 0, if we hit it
        # Stop the tank when hitting the left wall
        if self.x < self.border:
            self.x = self.border
            self.speed = 0  
        # Stop the tank when hitting the right wall   
        elif self.x > self.screen_w - self.border:
            self.x = self.screen_w - self.border
            self.speed = 0  
        # Stop the tank when hitting the top wall
        if self.y < self.border:
            self.y = self.border
            self.speed = 0 
        # Stop the tank when hitting the bottom wall
        elif self.y > self.screen_h - self.border:
            self.y = self.screen_h - self.border
            self.speed = 0 

    

    def update(self):
        self.check_keys()
        self.check_border()
        # moves our ship at each frame
        # get x and y components of speed
        theta_rad = self.deg_to_rad(self.theta + 90)
        x_dot = cos(theta_rad) * self.speed
        y_dot = sin(theta_rad) * self.speed

        self.x += x_dot
        self.y -= y_dot
        self.rect.center = self.x,self.y
        #update rectangle
        


    
    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.orig_image, self.theta)
        # Get the new rect for the rotated image and set its center to the original rect center
        new_rect = rotated_image.get_rect(center=self.rect.center)
        # Draw the rotated image at the center
        screen.blit(rotated_image, new_rect.topleft)
        