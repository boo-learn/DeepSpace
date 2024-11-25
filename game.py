import sys
import random
import pygame
from Ship import Ship
from Asteroid import Asteroid

# 0: ****** Подготовка ******
pygame.init()  # инициализация
pygame.font.init()  # активируем работу со шрифтами
my_font = pygame.font.SysFont('Comic Sans MS', 10)
display = pygame.display.set_mode((800, 800))  # создание окна
screen = pygame.display.get_surface()  # получаем поверхность для рисования

# Создание игровых объектов:
ship = Ship((100, 100), 100)
# asteroid = Asteroid((700, 150), (-2, 0))
asteroids = [
    Asteroid((700, 150), (-2, 0)),
    Asteroid((700, 250), (-2.5, 0)),
    Asteroid((770, 450), (-1.8, 0)),
]
clock = pygame.time.Clock()
FPS = 60

while True:  # главный цикл программы
    dt = clock.tick(FPS)
    pygame.display.set_caption("FPS = " + str(clock.get_fps()))
    # 1: ****** Обработка событий ******
    for e in pygame.event.get():  # цикл обработки очереди событий окна
        ship.control(e)
        if e.type == pygame.QUIT:  # Обработка события "Закрытие окна"
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:  # Событие "Клавиша нажата"
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # 2: ****** Изменение свойств игровых объектов ******
    ship.move()
    for asteroid in asteroids:
        if asteroid.move() == "del me":
            # print("del")
            asteroids.remove(asteroid)
    # print(len(asteroids))
    # Проверка столновений
    for asteroid in asteroids:
        if asteroid.collide(ship):
            asteroids.remove(asteroid)
            ship.take_damage(asteroid)
    # 3: ****** Отрисовка игрового кадра ******
    screen.fill((0, 0, 0))  # Очищаем экран, заливая его (R, G, B) цветом
    ship.draw(screen)
    for asteroid in asteroids:
        asteroid.draw(screen)
    # Отображение сцены на экране(мониторе)
    pygame.display.flip()

# Полезные инструменты

# Как изменить размер загруженной картинки:
# 1. Загружаем картинку:
# image = pygame.image.load("Images/Units/aer2.png")
# 2. Изменяем размер
# image = pygame.transform.scale(image, (100, 100))
# 100, 100 - это новый размер картинки

# Как повернуть картинку на определенный угол:
# 1. Загружаем картинку:
# image = pygame.image.load("Images/Units/aer2.png")
# 2. Поворачиваем картинку
# rotated_image = pygame.transform.rotate(image, 45)
# 45 - угол поворота

# Как отразить картинку(flip) зеркально:
# 1. Загружаем картинку:
# image = pygame.image.load("Images/Units/aer2.png")
# 2. Поворачиваем картинку
# flip_image = pygame.transform.flip(image, True, False)
# True - отразить по вертикали, False(меняем на True) - если нужно отразить по горизонтали

# Как проверить столкновение объектов:
# if object1["rect"].colliderect(object2["rect"]):
#     print("Объекты столкнулись")


# Полезные ссылки:
# Online редактор изображений: https://www.iloveimg.com/resize-image
