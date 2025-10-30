import pygame

pygame.init()

#Setting up the python window
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Motorcycle Game')

def road_creator():
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
def reset_screen():
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

reset_screen()
#Game Loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x = 230
    y = 290
    w = 50
    h = 100
    velocity = 5
    moving_object = pygame.Rect(x,y,w,h)
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_object.x -= velocity
        moving_object.w -= velocity
        road_creator()
        pygame.display.flip()
    if keys[pygame.K_RIGHT]:
        moving_object.x += velocity
        moving_object.w += velocity
        road_creator()
        pygame.display.flip()
    if keys[pygame.K_UP]:
        moving_object.y -= velocity
        moving_object.h -= velocity
        road_creator()
        pygame.display.flip()
    if keys[pygame.K_DOWN]:
        moving_object.y += velocity
        moving_object.h += velocity
        road_creator()
        pygame.display.flip()
    
    pygame.draw.rect(screen, (0,0,255), moving_object)
    pygame.display.flip()

    
'''
        else:
            while event.type == pygame.KEYDOWN:
                moving_object.(5,5)
'''