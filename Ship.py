import pygame
from Shot import Shot


class Ship:
    # Метод (Конструктор)
    def __init__(self, start_pos, hp):
        # Тут описываем все свойства объекта
        self.image = pygame.image.load("Images/Ships/ship03_1_small.png").convert_alpha()
        self.image = pygame.transform.rotate(self.image, -90)
        self.pos = pygame.Vector2(start_pos)
        self.rect = self.image.get_rect(center=self.pos)
        self.hp = hp
        self.speed = pygame.Vector2(0, 0)
        self.shots = []

    def control(self, e):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.speed.y = -6  # движение вверх
        if keys[pygame.K_s]:  # Нажата клавиша "S"
            self.speed.y = +6  # движение вниз

        if e.type == pygame.KEYUP:
            self.speed = pygame.Vector2(0, 0)

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                shot = Shot(self.pos, (10, 0))
                self.shots.append(shot)
                # Стреляем

    def take_damage(self, object):
        self.hp -= object.damage
        # print("hp = ", self.hp)

    def move(self):
        self.pos += self.speed
        self.rect.center = self.pos
        for shot in self.shots:
            shot.move()

    # Тут описываем все методы - функции, которые выполняют операции на свойствами
    def draw(self, screen):
        # Внутри метода ко всем свойствам обращаемся через self...
        screen.blit(self.image, self.rect)
        for shot in self.shots:
            shot.draw(screen)

# ship = Ship((100, 100), 80)
