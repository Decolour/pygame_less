import pygame
import random
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TARGET_SPEED = 0.3
MAX_SPEED = 0.5
DETECTION_RADIUS = 100

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Гитлер капут!')
icon = pygame.image.load('images/pngwing.com.png')
pygame.display.set_icon(icon)

target_img = pygame.image.load('images/icons8-гитлер-50.png')
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def move_target_away_from_cursor(target_x, target_y, cursor_x, cursor_y, speed, max_speed):
    # Calculate the center of the target
    center_x = target_x + target_width / 2
    center_y = target_y + target_height / 2

    angle = math.atan2(center_y - cursor_y, center_x - cursor_x)
    new_target_x = target_x + speed * math.cos(angle)
    new_target_y = target_y + speed * math.sin(angle)

    # Calculate actual speed to apply max speed limit
    actual_speed = math.sqrt((new_target_x - target_x) ** 2 + (new_target_y - target_y) ** 2)
    if actual_speed > max_speed:
        ratio = max_speed / actual_speed
        new_target_x = target_x + (new_target_x - target_x) * ratio
        new_target_y = target_y + (new_target_y - target_y) * ratio

    # Ensure target stays within screen bounds
    if new_target_x < 0 or new_target_x > SCREEN_WIDTH - target_width:
        new_target_x = target_x - speed * math.cos(angle)

    if new_target_y < 0 or new_target_y > SCREEN_HEIGHT - target_height:
        new_target_y = target_y - speed * math.sin(angle)

    return new_target_x, new_target_y


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate the center of the target
    center_x = target_x + target_width / 2
    center_y = target_y + target_height / 2

    distance_to_cursor = get_distance(center_x, center_y, mouse_x, mouse_y)

    if distance_to_cursor < DETECTION_RADIUS:
        target_x, target_y = move_target_away_from_cursor(target_x, target_y, mouse_x, mouse_y, TARGET_SPEED, MAX_SPEED)

        # Ensure target stays within screen bounds
        target_x = max(0, min(target_x, SCREEN_WIDTH - target_width))
        target_y = max(0, min(target_y, SCREEN_HEIGHT - target_height))

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()
