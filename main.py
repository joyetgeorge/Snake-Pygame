import pygame
import random
import math

running = True
pygame.init()

direction = ""

snake_list = []
temp = []
score = 0

font = pygame.font.Font('freesansbold.ttf', 15)

snakeX = random.randrange(0, 500, 15)
snakeY = random.randrange(0, 500, 15)

snakeX_change = 0
snakeY_change = 0
snake_length = 1

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
                if direction != "LEFT":
                    snakeX_change = 15
                    snakeY_change = 0
                    direction = "RIGHT"
            if event.key == pygame.K_LEFT:
                if direction != "RIGHT":
                    snakeX_change = -15
                    snakeY_change = 0
                    direction = "LEFT"
            if event.key == pygame.K_DOWN:
                if direction != "UP":
                    snakeY_change = 15
                    snakeX_change = 0
                    direction = "DOWN"
            if event.key == pygame.K_UP:
                if direction != "DOWN":
                    snakeY_change = -15
                    snakeX_change = 0
                    direction = "UP"
    
    print(snake_list)

    for i, j in snake_list:
        if i == fruitX and j == fruitY:
            fruitX = random.randrange(0, 500, 15)
            fruitY = random.randrange(0, 500, 15)

    if len(snake_list):
        if i == snakeX and j == snakeY:
            print("snake hit")

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


    temp = []

    temp.append(snakeX)
    temp.append(snakeY)

    snake_list.append(temp)

    if len(snake_list) > snake_length:
        del snake_list[0]

    for i, j in snake_list:
        pygame.draw.rect(screen, [163, 190, 140], (i, j, 15, 15))
        if i > 510 or j > 510 or i < 0 or j < 0:
            running = False
    text = font.render('SCORE : '+str(score), True, (216, 222, 233))
    screen.blit(text, (420, 14))
    pygame.draw.rect(screen, [191, 97, 106], (fruitX, fruitY, 15, 15))
    pygame.display.update()
