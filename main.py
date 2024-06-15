import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Гитлер капут!')
icon = pygame.image.load('images/pngwing.com.png')
pygame.display.set_icon(icon)

target_img = pygame.image.load('images/icons8-гитлер-50.png')
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# Загрузка изображения прицела
crosshair_img = pygame.image.load('images/crosshair.png')
crosshair_img = pygame.transform.scale(crosshair_img, (150, 175)) # Измените размер по необходимости
crosshair_rect = crosshair_img.get_rect()

# Скрыть системный курсор
pygame.mouse.set_visible(False)


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_img, (target_x, target_y))
    screen.blit(crosshair_img, crosshair_rect)
    # Получение позиции мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Обновление позиции изображения прицела
    crosshair_rect.center = (mouse_x, mouse_y)

    pygame.display.update()

pygame.quit()
