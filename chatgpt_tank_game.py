import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tank Battle")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Tank class
class Tank(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, speed):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (40, 40))  # Scale image to 40x40 (optional)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.angle = 0

    def update(self):
        # Update tank movement and rotation based on key presses
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.angle -= 5
        if keys[pygame.K_RIGHT]:
            self.angle += 5

        if keys[pygame.K_UP]:
            self.rect.x += self.speed * math.cos(math.radians(self.angle))
            self.rect.y -= self.speed * math.sin(math.radians(self.angle))
        if keys[pygame.K_DOWN]:
            self.rect.x -= self.speed * math.cos(math.radians(self.angle))
            self.rect.y += self.speed * math.sin(math.radians(self.angle))

        # Prevent the tank from going off-screen
        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, screen_height - self.rect.height))

    def rotate(self, angle):
        self.angle += angle


# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, speed=10):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = angle
        self.speed = speed

    def update(self):
        # Move the bullet in the direction of the angle
        self.rect.x += self.speed * math.cos(math.radians(self.angle))
        self.rect.y -= self.speed * math.sin(math.radians(self.angle))

        # Delete bullet when it goes off screen
        if self.rect.x < 0 or self.rect.x > screen_width or self.rect.y < 0 or self.rect.y > screen_height:
            self.kill()


# Enemy Tank class (moves randomly)
class EnemyTank(Tank):
    def __init__(self, image_path, x, y, speed):
        super().__init__(image_path, x, y, speed)
        self.path = random.choice(['up', 'down', 'left', 'right'])

    def update(self):
        if self.path == 'up':
            self.rect.y -= self.speed
        elif self.path == 'down':
            self.rect.y += self.speed
        elif self.path == 'left':
            self.rect.x -= self.speed
        elif self.path == 'right':
            self.rect.x += self.speed

        # Change direction when hitting boundaries
        if self.rect.x <= 0 or self.rect.x >= screen_width - self.rect.width:
            self.path = random.choice(['up', 'down', 'left', 'right'])
        if self.rect.y <= 0 or self.rect.y >= screen_height - self.rect.height:
            self.path = random.choice(['up', 'down', 'left', 'right'])


# Main Game Loop
def game_loop():
    clock = pygame.time.Clock()

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # Create the player tank
    player_tank = Tank('tiny_tanks/PNG/Tiles/tank_red.png', screen_width // 4, screen_height // 2, speed=5)
    all_sprites.add(player_tank)

    # Create the enemy tank
    enemy_tank = EnemyTank('tiny_tanks/PNG/Tiles/tank_huge.png', screen_width * 3 // 4, screen_height // 2, speed=3)
    all_sprites.add(enemy_tank)

    # Game variables
    score = 0
    running = True

    # Main loop
    while running:
        screen.fill(WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Get the position of the mouse relative to the screen
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Calculate the angle to the mouse cursor
                    angle_to_mouse = math.degrees(math.atan2(mouse_y - player_tank.rect.centery, mouse_x - player_tank.rect.centerx))

                    # Create a new bullet when space is pressed
                    bullet = Bullet(player_tank.rect.centerx, player_tank.rect.centery, angle_to_mouse)
                    all_sprites.add(bullet)
                    bullets.add(bullet)

        # Update player tank and enemy tank
        player_tank.update()
        enemy_tank.update()

        # Update all sprites
        all_sprites.update()

        # Check for bullet collisions
        for bullet in bullets:
            if bullet.rect.colliderect(enemy_tank.rect):
                bullet.kill()
                score += 1
                # Move the enemy tank to a random location after being hit
                enemy_tank.rect.center = (random.randint(100, screen_width - 100), random.randint(100, screen_height - 100))

        # Draw everything
        all_sprites.draw(screen)

        # Draw the score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update the screen
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()


# Start the game loop
game_loop()
