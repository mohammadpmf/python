import pygame
import time

pygame.init() # Since these modules are abstractions for specific hardware, this initialization step is required so that you can work with the same code on Linux, Windows, and Mac.
screen = pygame.display.set_mode((600,400))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((180, 40, 110))
    pygame.draw.circle(screen, (0,200, 14), (300, 200), 50, 100)
    pygame.display.flip()
    time.sleep(0.2)
    pygame.draw.circle(screen, (100,50, 90), (300, 200), 50, 100)
    pygame.display.flip()
    time.sleep(0.2)
    pygame.draw.circle(screen, (200,20, 150), (300, 200), 50, 100)
    pygame.display.flip()
    time.sleep(0.2)
    pygame.draw.circle(screen, (0,140, 0), (300, 200), 50, 100)
    pygame.display.flip()
pygame.quit()