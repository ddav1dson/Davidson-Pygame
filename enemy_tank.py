import pygame
from tank import Tank
from math import degrees, atan2, radians, cos, sin
from bullet import Bullet

# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class EnemyTank(Tank):
    def __init__(self, player, screen, x, y, WIDTH, HEIGHT, bullet_group, theta=270, color='gray'):
        super().__init__(screen, x, y, WIDTH, HEIGHT, bullet_group, theta, color)
        self.player = player
    
    def track_player(self):
        # overwriting checking keyboard and instead ship makes its own decisions
        # set the speed
        self.speed = 1
        # get the position of the player (lag)
        delta_x = self.player.x - self.x
        delta_y = self.player.y - self.y
        # if delta is too small do nothing!
        if delta_x**2 + delta_y**2 > 5:
            self.theta = degrees(atan2(-delta_x,-delta_y))
