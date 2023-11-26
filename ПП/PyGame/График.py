# Построение графика функции
# Необходимо определить свою Функцию в функции "f_graph"
# и границы вычисления, определяемые переменными "a" и "b"

import pygame
import math

def f_graph(x1):
    y1 = math.sin(x1) # функцию менять здесь!
    return(y1)

a = -10  # левая граница для вычисления
b = 10 # правая граница для вычисления

grModeX = 1600 # ширина окна
grModeY = 900 # высота окна
pygame.init()
screen = pygame.display.set_mode([grModeX,grModeY],pygame.FULLSCREEN)
screen.fill([255,255,255])
fontObj = pygame.font.Font('tahoma.ttf',20)
text = fontObj.render("y",True,(0,0,0))
screen.blit(text,[850,10])
fontObj2 = pygame.font.Font('tahoma.ttf',20)
text = fontObj.render("x",True,(0,0,0))
screen.blit(text,[1550,460])
sx = grModeX/(b - a) # массштаб по X
h = 1/sx # шаг изменения аргумента
xmid = grModeX // 2 # середина области построения по X
ymid = grModeY // 2 # середина области построения по Y

x = a
maxF = f_graph(x)
minF = maxF
while x <= b:
    y = f_graph(x)
    if y < minF:
        minF = y # определяем минимальное значение функции
    if y > maxF:
        maxF = y # определяем максимальное значение функции
    x = x + h

sy = grModeY/(maxF - minF) # массштаб по Y

# рисуем ось X
pygame.draw.line(screen,[0,0,0],[0,ymid],[grModeX,ymid])

# рисуем ось Y
pygame.draw.line(screen,[0,0,0],[xmid,0],[xmid,grModeY])

# рисуем график функции
x = a
#y = f_graph(x)

while x <= b:
    y = f_graph(x)
    screen.set_at([xmid + round(sx*x),ymid-round(sy*y)],[0,0,0])
    x = x + h
    pygame.time.delay(1)
    pygame.display.flip()
    
pygame.time.delay(2000)

pygame.quit()

