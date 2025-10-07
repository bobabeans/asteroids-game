import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        neg_dt = -dt
        self.cooldown -= dt
        if self.cooldown < 0:
            self.cooldown = 0

        if keys[pygame.K_a]:
            self.rotate(neg_dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt, PLAYER_SPEED)
        if keys[pygame.K_s]:
            self.move(neg_dt, PLAYER_SPEED)
        if keys[pygame.K_SPACE]:
            if self.cooldown <= 0:
                self.shoot()

    def move(self, dt, speed):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * speed * dt

    def shoot(self):
        self.cooldown = PLAYER_SHOOT_COOLDOWN
        x, y = self.position.x, self.position.y
        shot = Shot(x, y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity += forward * PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)