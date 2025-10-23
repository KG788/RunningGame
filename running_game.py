import pygame

pygame.init()

flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World')


screen.fill((255,0,0))
pygame.display.flip()

pygame.draw.rect(screen, (225,100,0), [100,100,100,100], 1)
pygame.display.update()

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    