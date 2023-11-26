import pygame
import math
pygame.init()
screen = pygame.display.set_mode([900,900])
screen.fill([255,255,255])

my_ball = pygame.image.load("beach_ball.png")

screen.blit(my_ball,[0,0])

pygame.display.flip()

pygame.time.delay(2000)

pygame.quit()
