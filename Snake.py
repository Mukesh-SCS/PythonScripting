import pygame
import random
import time

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

snake_block = 15
speed = 8

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, WHITE, [x[0], x[1], snake_block, snake_block])


game_over = False
x1, y1 = 400, 300
x1_change, y1_change = 0, 0
snake_List = []
Length_of_snake = 1
foodx = round(random.randrange(0, 800 - snake_block) / 10) * 10
foody = round(random.randrange(0, 600 - snake_block) / 10) * 10

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change, y1_change = -snake_block, 0
            elif event.key == pygame.K_RIGHT:
                x1_change, y1_change = snake_block, 0
            elif event.key == pygame.K_UP:
                x1_change, y1_change = 0, -snake_block
            elif event.key == pygame.K_DOWN:
                x1_change, y1_change = 0, snake_block

    if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])

    snake_Head = [x1, y1]
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    for block in snake_List[:-1]:
        if block == snake_Head:
            game_over = True

    draw_snake(snake_block, snake_List)
    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, 800 - snake_block) / snake_block) * snake_block
        foody = round(random.randrange(0, 600 - snake_block) / snake_block) * snake_block
        Length_of_snake += 1

    clock.tick(speed)

time.sleep(1)
pygame.quit()
quit()
