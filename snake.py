import pygame
import constant as c

class Snake:
    def __init__(self, x, y, renderTail):
        self.score = 0
        self.desiredD = ''
        self.x = x 
        self.y = y
        self.HIDDENTAIL = 3
        self.direction = 'r'
        self.pos = []
        self.render = renderTail
        self.length = self.render + self.HIDDENTAIL 
        self.deltaX = 0
        self.deltaY = 0
        self.speed = c.SQUARE_SIZE
        self.body = pygame.Rect( (self.x,self.y, c.SQUARE_SIZE, c.SQUARE_SIZE))

        for i in range(self.length):
            self.pos.append( [self.x - c.SQUARE_SIZE*i, self.y] )

        
    def move(self):
        #checking
        if self.desiredD == '':
            return
        if self.direction != 'l' and self.desiredD == 'r':
            self.direction = self.desiredD
        elif self.direction != 'r' and self.desiredD == 'l':
            self.direction = self.desiredD
        elif self.direction != 'd' and self.desiredD == 'u': 
            self.direction = self.desiredD
        elif self.direction != 'u' and self.desiredD == 'd':
            self.direction = self.desiredD

        #move
        if self.direction == 'l':
            self.deltaX -= self.speed
        elif self.direction == 'r' :
            self.deltaX += self.speed
        elif self.direction == 'd' : 
            self.deltaY += self.speed
        elif self.direction == 'u' :
            self.deltaY -= self.speed
        
        self.x = self.x + self.deltaX
        self.y = self.y + self.deltaY
        self.pos.insert(0, [self.x, self.y ])
        self.deltaX = 0
        self.deltaY = 0
    
    def changeDirection(self, direction):
        if len(direction) == 1:
            self.desiredD = direction
        else:
            if self.direction == 'u' or self.direction == 'd':
                self.desiredD = direction[1]
            else:
                self.desiredD = direction[0]

    def getInput(self, up, down, left, right):
        d = [up, down, left, right]
        d2 = ['u', 'd', 'l', 'r']
        d3 = ""
        for n,i in enumerate(d):
            if i:
                d3 += d2[n]
        if len(d3) != 0:
            self.changeDirection(d3)

        
    def collideItself(self):
        for n,[x,y] in enumerate(self.pos):
            if n < self.render :
                if self.pos[0][0] == x and self.pos[0][1] == y and n != 0:
                    return True
            else:
                break
        return False

    def collideWall(self):
        if self.pos[0][0] < 0 or self.pos[0][1] < 0 or self.pos[0][0] > c.SQUARE_SIZE*(c.WIN_CONSTANT - 1) or self.pos[0][1] > c.SQUARE_SIZE*(c.WIN_CONSTANT - 1):
            return True
        return False

    def draw(self, win):
        for n,[x,y] in enumerate(self.pos):
            tail = pygame.Rect(x,y,c.SQUARE_SIZE,c.SQUARE_SIZE)
            if n != 0 and n < self.render:
                pygame.draw.rect(win, (200,200,200) , tail)
            elif n == 0:
                pygame.draw.rect(win, (0,255,0) , tail)