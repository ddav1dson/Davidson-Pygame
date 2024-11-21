import pygame
from tank import Tank
from math import degrees, atan2, radians, cos, sin

class EnemyTank(Tank):
    def __init__(self, player, screen, x, y, WIDTH, HEIGHT, bullet_group, theta=180, color='enemy'):
        super().__init__(screen, x, y, WIDTH, HEIGHT, bullet_group, theta=180, color = 'enemy')
        self.player = player
        print(self.color)
    
def track_player(self):
        # overwriting checking keyboard and instead tank makes its own decisions
        # set the speed
        self.speed = 1
        print('tracking')
        print(self.player.x, self.player.y)
        # get the position of the player (lag)
        delta_x = self.player.x - self.x
        delta_y = self.player.y - self.y
        # if delta is too small do nothing!
        if delta_x**2 + delta_y**2 > 5:
            self.theta = degrees(atan2(-delta_y,delta_x))
        