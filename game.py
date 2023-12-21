import pygame
import random

# Initialisierung von Pygame
pygame.init()

# Fenstergröße
width, height = 640, 480
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Schlangenspiel")

# Farben
green = (0, 128, 0)
purple = (128, 0, 128)
black = (0, 0, 0)

# Schlangenkörper
block_size = 20
snake_speed = 15

font = pygame.font.SysFont("bahnschrift", 25)

clock = pygame.time.Clock()

# Funktion zum Zeichnen der Schlange
def our_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(win, purple, [x[0], x[1], block_size, block_size])

# Hauptspiel-Funktion
def gameLoop():
    game_over = False
    game_close = False

    x1, y1 = width / 2, height / 2
    x1_change, y1_change = 0, 0

    snake_List = []
    Length_of_snake = 1

    foodx, foody = round(random.randrange(0, width - block_size) / 20.0) * 20.0, round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            win.fill(black)
            message = font.render("Du hast verloren! Drücke Q-Quit oder C-Play Again", True, purple)
            win.blit(message, [width / 6, height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        win.fill(green)

        pygame.draw.rect(win, black, [foodx, foody, block_size, block_size])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = round(random.randrange(0, width - block_size) / 20.0) * 20.0, round(random.randrange(0, height - block_size) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
