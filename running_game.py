import pygame

pygame.init()

#Setting up the python window
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Motorcycle Game')


screen.fill((124,252,0))
pygame.display.flip()

#Main Road
pygame.draw.rect(screen, (0,0,0), [100,0,200,400], 0)

#Lane Stripes
pygame.draw.rect(screen, (255,255,255), [195,0,10,40], 0)
pygame.draw.rect(screen, (255,255,255), [195,80,10,40], 0)
pygame.draw.rect(screen, (255,255,255), [195,160,10,40], 0)
pygame.draw.rect(screen, (255,255,255), [195,240,10,40], 0)
pygame.draw.rect(screen, (255,255,255), [195,320,10,40], 0)
pygame.draw.rect(screen, (255,255,255), [195,390,10,30], 0)
pygame.display.update()

#Game Loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    