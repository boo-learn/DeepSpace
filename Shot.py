import pygame


class Shot:
    def __init__(self, start_pos, speed):
        self.image = pygame.image.load("Images/Shots/yellow_shot.png").convert_alpha()
        self.pos = pygame.Vector2(start_pos)
        self.rect = self.image.get_rect(center=self.pos)
        self.speed = pygame.Vector2(speed)

    def move(self):
        self.pos += self.speed
        self.rect.center = self.pos

    def collide(self, other_object):
        if self.rect.colliderect(other_object.rect):
            return True
        else:
            return False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
