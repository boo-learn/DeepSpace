import pygame
import random


class Asteroid:
    def __init__(self, start_pos, speed):
        self.image = pygame.image.load("Images/Asteroids/asteroid01.png").convert_alpha()
        self.pos = pygame.Vector2(start_pos)
        self.rect = self.image.get_rect(center=self.pos)
        self.speed = pygame.Vector2(speed)
        self.damage = 10

    def move(self):
        self.pos += self.speed
        self.rect.center = self.pos
        if self.rect.right < 0:
            return "del me"
            # self.pos = pygame.Vector2(850, random.randint(200, 700))
            # self.rect.center = self.pos

    def collide(self, other_object):
        return self.rect.colliderect(other_object.rect)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# asteroid.collide(ship)
