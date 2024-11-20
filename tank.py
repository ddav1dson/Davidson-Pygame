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
        self.explosion_image = pygame.image.load('tiny_tanks/PNG/Retina/explosion2.png')
        self.explosion_image = pygame.transform.scale_by(self.explosion_image, 3)
        self.explosion_timer = 0
        self.explosion_length = 750

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
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        # Draw the tank body (fixed)
        # rotate the tank image to face the correct direction
        rotated_image = pygame.transform.rotate(self.orig_image, self.theta)
        # Get the rect for the rotated image and adjust position
        self.rect = rotated_image.get_rect(center=self.rect.center)
        #update the image to the rotated one
        self.image = rotated_image

        if self.color =='red':
            self.check_keys() # only red is influenced by keys
            dx = mouse_x - self.rect.centerx
            dy = mouse_y - self.rect.centery
            angle = degrees(atan2(dy, dx))  # atan2 returns angle in radians, works from -pi to pi

            # Rotate the turret by the calculated angle
            self.turrent_image = pygame.transform.rotate(self.orig_turrent, -angle + 90)

            # Recalculate the rect for the rotated turret to position it correctly
            self.turrent_rect = self.turrent_image.get_rect(center =(self.rect.width//2, self.rect.height//2))
            self.image.blit(self.turrent_image, self.turrent_rect)
        
        else:
            self.track_player()

        # check on the explosion status
        if self.explosion_timer != 0:
            delta_time = pygame.time.get_ticks() - self.explosion_timer
            # if we have reached kill time, kill the ship
            if delta_time >= self.explosion_length:
                print("killing ship")
                self.kill()
                self.speed = 0
            # ship is in explosion sequence
            # grow the ship based on time
            if delta_time < (self.explosion_length/2):
                # grow the explosion
                self.orig_image = pygame.transform.scale_by(self.explosion_image, delta_time/1000)
            else:
                # shrink the explosion
                self.orig_image = pygame.transform.scale_by(self.explosion_image, self.explosion_length/1000 - (delta_time - self.explosion_length/2)/1000)
        
        self.check_border()
        # moves our tank at each frame
        # get x and y components of speed
        theta_rad = self.deg_to_rad(self.theta + 90)
        x_dot = cos(theta_rad) * self.speed
        y_dot = sin(theta_rad) * self.speed

        self.x += x_dot
        self.y -= y_dot
        self.rect.center = (self.x,self.y)
        
    
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


    def track_player(self):
        # this code is in EnemyTank class
        pass

    def explode(self):
        # if the timer is already set, do nothing
        if self.explosion_timer ==0:
            # start a timer so that it gets killed later
            self.explosion_timer = pygame.time.get_ticks()
            print("explosion timer set!")
            self.speed = 0
