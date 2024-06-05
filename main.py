import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

running = True

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('images/pngwing.com.png')
pygame.display.set_icon(icon)

target_img = pygame.image.load('images/icons8-гитлер-50.png')
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

while running:
    pass

pygame.quit()

