import pygame
import math
pygame.init()
screen = pygame.display.set_mode([1000,1000])
screen.fill([255,255,255])
#Рисование фигур
'''pygame.draw.circle(screen,[255,0,0],[100,100,],30,1)
pygame.draw.rect(screen,[0,255,0],[100,100,50,50],0)
plotPoints=[[0,0],[30,30],[60,0],[90,30],[120,0]]
pygame.draw.lines(screen,[0,0,255],False,plotPoints,2)'''

#Рисование дуги
'''plotPoint = []
for x in range(0,300):
    y = int(math.sin(x / 300.0 * 4 * math.pi) * 150 + 150)
    plotPoint.append([x,y])
pygame.draw.lines(screen,[0,0,0],False,plotPoint,1)    
screen.set_at([x,y],[0,0,0])'''

#Рисование текста
'''fontObj = pygame.font.Font('tahoma.ttf',20)
text = fontObj.render("Привет,ТАТК!",True,(255,255,0),(0,0,255))
screen.blit(text,[70,100])'''

#Рисование мяча
'''my_ball = pygame.image.load("beach_ball.png")

screen.blit(my_ball,[0,0])'''

# Рисование мяча 2
'''class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
image_file  = "beach_ball.png"
location = [10, 10]
ball = MyBallClass(image_file, location)
screen.blit(ball.image, ball.rect)'''
'''
# рисование мяча 3

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)

image_file  = "Ball1.png"
location = [10, 10]
speed = [2, 2]
ball = MyBallClass(image_file, speed)

while True:
    pygame.time.delay(30)
    screen.fill([255, 255, 255])
    ball.move()
    screen.blit(ball.image, ball.rect)
    pygame.display.flip()
'''
# рисование мяча 4

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.left < 0 or self.rect.right > height:
            self.speed[1] = -self.speed[1]
size = width, height = 300, 400
screen = pygame.display.set_mode(size)
#pygame.display.flip()
