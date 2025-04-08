import pygame
import time
import random

# Initialize pygame
pygame.init()

# Colors
black= (255, 255, 255)
violet  = (213, 50, 80)
green = (0,255,0)
blue = (50, 153, 213)

# Screen dimensions
width = 700
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake game by Musfirah')

# Snake settings
block_size = 10
speed = 1

clock = pygame.time.Clock()
font = pygame.font.SysFont("bahnschrift", 25)

def show_score(score):
    value = font.render("Score: " + str(score), True, black)
    window.blit(value, [10, 10])

def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], block_size, block_size])

def message(msg, color):
    mesg = font.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0

    snake = []
    snake_length = 1

    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            window.fill(black)
            message("Game Over! Press C to Play Again or Q to Quit", violet)
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        window.fill(blue)
        pygame.draw.rect(window, violet, [food_x, food_y, block_size, block_size])

        head = [x, y]
        snake.append(head)
        if len(snake) > snake_length:
            del snake[0]

        for segment in snake[:-1]:
            if segment == head:
                game_close = True

        draw_snake(block_size, snake)
        show_score(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

game_loop()