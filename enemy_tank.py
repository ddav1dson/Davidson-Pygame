import pygame
from tank import Tank

class EnemyTank(Tank):
    def __init__(self, screen, x, y, WIDTH, HEIGHT, bullet_group, theta=180, color='red'):
        super().__init__(screen, x, y, WIDTH, HEIGHT, bullet_group, theta=180, color)
    
    def check_keys(self):
        # overwrite old checl_keys and instead tank makes its own decision
        # set the speed
        self.speed = 3
        
        # get the postion of the player's tank
        
        # set the theta
        