import pygame
import math
pygame.init()
screen = pygame.display.set_mode([900,900])
#screen.fill([255,255,255])

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > 900:
            self.speed[0] = -self.speed[0]
        if self.rect.left < 0 or self.rect.bottom > 900:
            self.speed[1] = -self.speed[1]
image_file  = "Ball1.png"
location = [10, 10]
speed = [10, 10]
ball = MyBallClass(image_file, location,speed)

while True:
    pygame.time.delay(30)
    screen.fill([255, 255, 255])
    ball.move()
    screen.blit(ball.image, ball.rect)
    pygame.display.flip()
