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
image_file  = "beach_ball.png"
location = [10, 10]
ball = MyBallClass(image_file, location)
screen.blit(ball.image, ball.rect)

pygame.display.flip()

pygame.time.delay(2000)

pygame.quit()
