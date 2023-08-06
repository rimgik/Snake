import pygame
import os
from snake import Snake
from food import Food
import random
import constant as c

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
windows = pygame.display.set_mode((c.WIN_WIDTH,c.WIN_HEIGHT))
pygame.display.set_caption("Snake!")
windows.fill((0, 0, 0))

font = pygame.font.SysFont("comicsansms", 72)
font2 = pygame.font.SysFont("comicsansms", 40)
base = pygame.Rect(0, c.WIN_HEIGHT - c.BASE_HEIGHT, c.WIN_WIDTH, c.BASE_HEIGHT)

def spawnFood(foods, snake):
    foods.append( Food(c.SQUARE_SIZE*random.randrange(0,(c.WIN_CONSTANT - 1)),c.SQUARE_SIZE*random.randrange(0,(c.WIN_CONSTANT - 1))) )
    if foods[0].collide(snake):
        del foods[0]
        spawnFood(foods, snake)

def gameover(text):
    text2 = font.render("GAME OVER", True, (255, 255, 255))
    text3 = font2.render("press space to try again", True, (255, 255, 255))

    #show losing text
    windows.blit(text, (10, c.WIN_HEIGHT - c.BASE_HEIGHT - 10))
    windows.blit(text2, ( -text2.get_width()/2 + c.WIN_WIDTH/2,-text2.get_height()/2 + (c.WIN_HEIGHT - c.BASE_HEIGHT)/2))
    windows.blit(text3,  ( -text3.get_width()/2 + c.WIN_WIDTH/2,-text3.get_height()/2 + (c.WIN_HEIGHT - c.BASE_HEIGHT)/2 + 80))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE] :
                    main()

def main():
    snake = Snake(c.SQUARE_SIZE*round(c.WIN_CONSTANT/2), c.SQUARE_SIZE*round(c.WIN_CONSTANT/2) ,3)
    foods = [Food(c.SQUARE_SIZE*random.randrange(0,c.WIN_CONSTANT - 1),c.SQUARE_SIZE*random.randrange(0,c.WIN_CONSTANT - 1))]
    running = True
    
    text = font.render("Score: " + str(snake.score), True, (255, 255, 255) )
    while running: 
        up = False
        down = False
        left =False
        right = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_w] :
                    up = True
                if pygame.key.get_pressed()[pygame.K_a] :
                    left = True
                if pygame.key.get_pressed()[pygame.K_s] :
                    down = True
                if pygame.key.get_pressed()[pygame.K_d] :
                    right = True
  
        snake.getInput(up, down, left, right)
        #snake
        snake.move()
        if snake.collideItself() or snake.collideWall():
            running = False
            gameover(text)

        snake.draw(windows)
        
        #food
        for food in foods:
            if food.collide(snake):
                snake.score += 1
                snake.render += 1
                foods.remove(food)
                spawnFood(foods, snake)
                text = font.render("Score: " + str(snake.score), True, (255, 255, 255) )
                
            food.draw(windows)
        #base
        pygame.draw.rect(windows, (37, 40, 219), base)
        #score text
        windows.blit(text, (10, c.WIN_HEIGHT - c.BASE_HEIGHT - 10))
        pygame.display.update()
        #bg
        windows.fill((0,0,0))
        clock.tick(15)
main()
