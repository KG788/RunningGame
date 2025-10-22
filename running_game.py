import pygame

pygame.init()

flags = pygame.FULLSCREEN
pygame.display.set_mode(size=(400, 400), flags=0, depth=5, display=0, vsync=0)

running = True
while running == True:

    print('hello')
    running = False