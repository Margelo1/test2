import pygame
import random

pygame.init()
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption('Цветные точки')

for i in range(10000):
    x = random.randint(0, 639)
    y = random.randint(0, 479)
    R = random.randint(0, 254)
    G = random.randint(0, 254)
    B = random.randint(0, 254)

    screen.set_at([x,y],[R,G,B])
    pygame.display.flip()
pygame.time.delay(3000)

pygame.quit()
