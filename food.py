import pygame
import constant as c

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, c.SQUARE_SIZE, c.SQUARE_SIZE)
        self.rect.inflate_ip(-3, -3)

    def collide(self, snake):
        for n,[x,y] in enumerate(snake.pos) :
            if n < snake.render:
                if x == self.x and y == self.y and n < snake.render:
                    return True
            else:
                break
        return False

    def draw(self, win):
        pygame.draw.rect(win, (255,0,0) , self.rect)