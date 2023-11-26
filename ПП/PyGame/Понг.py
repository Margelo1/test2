import pygame
import time

pygame.init()
clock = pygame.time.Clock()

BLACK = (0,0,0)
GREEN = (144,238,144)
YELLOW = (255,238,0)
RED = (255,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

wnWidth = 600
wnHeight = 500
wn = pygame.display.set_mode((wnWidth,wnHeight))
pygame.display.set_caption("Чемпионат 3 курса по Понгу")

startX = wnWidth//2; startY = 0
endx = wnWidth//2; endY = wnHeight;
lineWidth = 5
pWidth = 20
pLength = 100

class Ball:
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.speedx = 8
        self.speedy = -6
        self.scoreA = 0
        self.scoreB = 0

    def update(self):
        self.x = self.x + self.speedx
        self.y = self.y + self.speedy

        if self.x + self.radius < 0:
            self.x = wnWidth//2
            self.y = wnHeight//2
            self.scoreB = self.scoreB + 1
        if self.x - self.raduis > wnWidth:
            self.x = wnWidth//2
            self.y = wnHeight//2
            self.scoreA = self.scoreA + 1
    def draw(self,wn):
        pygame.draw.circle(wn,YELLOW,(self.x,self.y),self.radius)
class Player:
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speedy = 0
    def update(self):
        keystate = pygame.key.get_pressed()
        if self.x == 0:
            if keystate[pygame.K_w]:
                self.speedy = -10
            elif keystate[pygame.K_s]:
                self.speedy = 10
            else:
                self.speedy = 0
        else:
            if keystate[pygame.K_UP]:
                self.speedy = -10
            elif keystate[pygame.K_DOWN]:
                self.speedy = 10
            else:
                self.speedy = 0
            self.y = self.y + self.speedy
    def draw_B(self,wn):
        pygame.draw.rect(wn,BLUE, [self.x, self.y, self.width, self.height])
    def draw_R(self,wn):
        pygame.draw.rect(wn, RED, [self.x, self.y, self.width, self.height])
def scoreBoardA(score):
    font = pygame.font.Font(None,50)
    text = font.render(str(score),True,BLACK)
    textWidth = text.get_width()
    x = int(wnWidth//2-textWidth//2 - 50)
    wn.blit(text,(x,20))
def scoreBoardB(score):
    font = pygame.font.Font(None,50)
    text = font.render(str(score),True,BLACK)
    textWidth = text.get_width()
    x = int(wnWidth//2-textWidth//2 + 50)
    wn.blit(text,(x,20))

radius = 15
ball = Ball(wnWidth//2,wnHeight//2,radius)

playerA = Player(0, wnHeight//2 - pLength/2, pWidth, pLength)
playerB = Player(wnWidth-pWidth, wnHeight//2-pLength/2, pWidth, pLength)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    playerA.update()
    playerB.update()
    ball.update()
    wn.fill(GREEN)

    pygame.draw.line(wn, WHITE,(startX,startY),(endX,endY),lineWidth)
    playerA.draw_B(wn)
    playerB.draw_R(wn)
    ball.draw(wn)
    if ball.x + ball.radius > playerB.x and  ball.x + ball.radius < playerB.x + playerB.width:
        if ball.y + ball.radius > playerB.y and ball.y + ball.radius < playerB.y + playerB.height:
            ball.speedx = -ball.speedx

    if ball.x - ball.radius < playerA.x + playerA.width and ball.x - ball.radius > 0:
        if ball.y + ball.radius > playerA.y and ball.y - ball.radius < playerA.y + playerA.height:
             ball.speedx = -ball.speedx
    scoreBoardA(ball.scoreA)
    scoreBoardB(ball.scoreB)

    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()
        
        
    
                    
        
       
    
        
