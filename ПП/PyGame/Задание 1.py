import pygame
screen = pygame.display.set_mode([1024, 768])
pygame.display.set_caption("Текущее разрешение: 1024 на 768")
pygame.time.delay(2000)


screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Текущее разрешение: 800 на 600")
pygame.time.delay(2000)

screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Текущее разрешение: 640 на 480")
pygame.time.delay(2000)


screen = pygame.display.set_mode([1024, 768], pygame.FULLSCREEN)
pygame.time.delay(2000)

screen = pygame.display.set_mode([800, 600], pygame.FULLSCREEN)
pygame.time.delay(2000)

screen = pygame.display.set_mode([640, 480], pygame.FULLSCREEN)
pygame.time.delay(2000)

pygame.quit()
