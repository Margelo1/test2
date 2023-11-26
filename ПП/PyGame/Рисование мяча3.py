import pygame
import math
pygame.init()
screen = pygame.display.set_mode([900,900])
screen.fill([255,255,255])

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
    
