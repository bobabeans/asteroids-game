import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        x, y = self.position.x, self.position.y
        random_angle = random.uniform(20, 50)
        split_radius = self.radius - ASTEROID_MIN_RADIUS

        split_one = Asteroid(x, y, split_radius)
        split_two = Asteroid(x, y, split_radius)

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif self.radius > 38 and self.radius < 45:
            split_one.velocity = self.velocity.rotate(random_angle) * 2
            split_two.velocity = self.velocity.rotate(-random_angle) * 2
        elif self.radius > 44:
            split_one.velocity = self.velocity.rotate(random_angle) * 2
            split_two.velocity = self.velocity.rotate(-random_angle) * 2 