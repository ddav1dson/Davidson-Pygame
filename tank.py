from math import cos, sin, pi, degrees, radians, atan2
import pygame
from bullet import Bullet

class Tank(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, WIDTH, HEIGHT, bullet_group, theta=180, color='red'):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 0
        self.theta = theta # degrees
        # self.orig_image = pygame.image.load('tiny_tanks/PNG/Tiles/tank_red.png')
        self.color = color
        if color == 'red':
            self.orig_image = pygame.image.load('tiny_tanks/PNG/Tiles/tankBody_red.png')
            self.orig_turrent = pygame.image.load('tiny_tanks/PNG/Tiles/tankRed_barrel1.png')
        else:
            self.orig_image = pygame.image.load('tiny_tanks/PNG/Tiles/tank_huge.png')
            self.orig_turrent = pygame.image.load('tiny_tanks/PNG/Tiles/tankRed_barrel1.png')
        self.image = self.orig_image
        self.turrent_image = self.orig_turrent
        self.rect = self.image.get_rect()
        self.turrent_rect = self.turrent_image.get_rect()
        self.rect.center = (self.x, self.y)
        self.screen_w = WIDTH
        self.screen_h = HEIGHT
        self.border = 15 # A margin representing the distance to the edge of the screen. 
        # self.bullet = pygame.image.load('tiny_tanks/PNG/Tiles/bulletRed3_outline.png')
        self.reverse_time = pygame.time.get_ticks()
        self.screen = screen
        self.bullet_group = bullet_group
        self.reload_time = 0
        self.reload_wait = 1000

    def deg_to_rad(self, deg):
        # converts deg to rad
        rad = (deg/180) * pi
        return rad

    def check_keys(self):
        acceleration = 0.3
        max_speed = 3
        keys = pygame.key.get_pressed()
        # moves the tank forward and backward
        if keys[pygame.K_w]:
            self.speed -= acceleration
        elif keys[pygame.K_s]:
            self.speed += acceleration
        else: 
            self.speed *= 0.7
        # keeps tank to the max speed
        if self.speed > max_speed:
            self.speed = max_speed
        if self.speed < -max_speed:
            self.speed = -max_speed
        # keys to turn the tank left or right
        if keys[pygame.K_a]:
            self.theta += 1.5
        if keys[pygame.K_d]:
            self.theta -= 1.5

        # check for space bar to shoot
        if keys[pygame.K_SPACE]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.shoot(mouse_x, mouse_y)
    


    def check_border(self):    
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
        if self.color =='red':   
            self.check_keys() # only red is influenced by keys
        self.check_border()
        # moves our tank at each frame
        # get x and y components of speed
        theta_rad = self.deg_to_rad(self.theta + 90)
        x_dot = cos(theta_rad) * self.speed
        y_dot = sin(theta_rad) * self.speed

        self.x += x_dot
        self.y -= y_dot
        self.rect.center = self.x,self.y
        # rotate the image and draw new rectangle
        self.image = pygame.transform.rotozoom(self.orig_image, self.theta, 1)
        self.turrent_image = pygame.transform.rotozoom(self.orig_turrent, self.theta, 1)

    def draw(self, screen):
        # Draw the tank body (fixed)
        rotated_image = pygame.transform.rotate(self.orig_image, self.theta)
        new_rect = rotated_image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, new_rect.topleft)

        # Draw the rotated turret
        screen.blit(self.turrent_image, self.turrent_rect.topleft)

    def rotate_turret(self, mouse_x, mouse_y):
        # Calculate the angle to the mouse cursor
        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery
        angle = degrees(atan2(dy, dx))  # atan2 returns angle in radians

          # Rotate the turret by the calculated angle
        self.turrent_image = pygame.transform.rotate(self.orig_turrent, -angle + 90)

        # Recalculate the rect for the rotated turret to position it correctly
        self.turrent_rect = self.turrent_image.get_rect(center=self.rect.center)
    
    def shoot(self, mouse_x, mouse_y):
       # only shoot if the time has elapsed
        if pygame.time.get_ticks() - self.reload_time > self.reload_wait:
            self.reload_time = pygame.time.get_ticks()
            dx = mouse_x - self.rect.centerx
            dy = mouse_y - self.rect.centery
            angle = degrees(atan2(dy, dx))  # atan2 returns angle in radians
            b = Bullet(self.screen, self, self.x, self.y, -angle)
            # put the bullet in a group
            self.bullet_group.add(b)