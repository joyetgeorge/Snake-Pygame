import pygame
import random
import math

running = True
pygame.init()

# Snake

snake_list = []
temp = []

snakeX = random.randrange(0, 500, 15)
snakeY = random.randrange(0, 500, 15)

temp.append(snakeX)
temp.append(snakeY)

snake_list.append(temp)

# print(snakeX, snakeY)
snakeX_change = 0
snakeY_change = 0
score = 0
snake_length = 1

# Fruit
fruitX = random.randrange(0, 500, 15)
fruitY = random.randrange(0, 500, 15)
fruitX_change = 0
fruitY_change = 0


screen = pygame.display.set_mode((510, 510))

clock = pygame.time.Clock()


def isCollided(snakeX, snakeY, fruitX, fruitY):
    distance = math.sqrt((math.pow(snakeX-fruitX, 2)) +
                         (math.pow(snakeY-fruitY, 2)))
    if distance < 15:
        return True
    else:
        return False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snakeX_change = 15
                snakeY_change = 0
            if event.key == pygame.K_LEFT:
                snakeX_change = -15
                snakeY_change = 0
            if event.key == pygame.K_DOWN:
                snakeY_change = 15
                snakeX_change = 0
            if event.key == pygame.K_UP:
                snakeY_change = -15
                snakeX_change = 0

    snakeX += snakeX_change
    snakeY += snakeY_change

    collision = isCollided(snakeX, snakeY, fruitX, fruitY)

    if collision:
        fruitX = random.randrange(0, 500, 15)
        fruitY = random.randrange(0, 500, 15)
        score += 1
        snake_length += 1

    clock.tick(15)

    print(score)
    screen.fill([46, 52, 64])

    for i, j in snake_list:
        if i == fruitX and j == fruitY:
            fruitX = random.randrange(0, 500, 15)
            fruitY = random.randrange(0, 500, 15)
            print("respawn")

        if i == snakeX and j == snakeY:
            print("snake hit")

    temp = []

    temp.append(snakeX)
    temp.append(snakeY)

    snake_list.append(temp)

    if len(snake_list) > snake_length:
        del snake_list[0]

    for i, j in snake_list:
        pygame.draw.rect(screen, [163, 190, 140], (i, j, 15, 15))
    print(snake_list)

    pygame.draw.rect(screen, [191, 97, 106], (fruitX, fruitY, 15, 15))
    pygame.display.update()
