import pygame
import math
pygame.init()
screen = pygame.display.set_mode([400,300])
screen.fill([255,255,255])

plotPoint = []
for x in range(0,300):
    y = int(math.sin(x / 300.0 * 4 * math.pi) * 150 + 150)
    plotPoint.append([x,y])
pygame.draw.lines(screen,[0,0,0],False,plotPoint,1)    
screen.set_at([x,y],[0,0,0])

pygame.display.flip()

pygame.time.delay(2000)

pygame.quit()
