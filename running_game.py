import pygame

pygame.init()

#















#Setting up the python window
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((650, 650))
pygame.display.set_caption('Motorcycle Game')


def reset_screen():
    screen.fill((124,252,0))
    pygame.display.flip()

    #Main Road
    pygame.draw.rect(screen, (0,0,0), [145,0,375,650], 0)

    #Lane Stripes
    pygame.draw.rect(screen, (255,255,255), [325,0,10,40], 0)
    pygame.draw.rect(screen, (255,255,255), [325,80,10,40], 0)
    pygame.draw.rect(screen, (255,255,255), [325,160,10,40], 0)
    pygame.draw.rect(screen, (255,255,255), [325,240,10,40], 0)
    pygame.draw.rect(screen, (255,255,255), [325,320,10,40], 0)
    pygame.draw.rect(screen, (255,255,255), [325,400,10,40], 0)
    pygame.draw.rect(screen, (255,255,255), [325,480,10,40], 0)
    pygame.draw.rect(screen, (255,255,255), [325,560,10,40], 0)
    pygame.draw.rect(screen, (255,255,255), [325,640,10,40], 0)

    pygame.display.update()

reset_screen()
#Game Loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x = 400
    y = 525
    w = 50
    h = 100
    velocity = 5
    moving_object = pygame.Rect(x,y,w,h)
    moving_object2 = pygame.Rect(x-200,y,w,h) 
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_object.x -= velocity
        reset_screen()
        pygame.display.flip()
    if keys[pygame.K_RIGHT]:
        moving_object.x += velocity
        reset_screen()
        pygame.display.flip()
    if keys[pygame.K_UP]:
        moving_object.y -= velocity
        velocity *= 2
        reset_screen()
        pygame.display.flip()
    if keys[pygame.K_DOWN]:
        moving_object.y += velocity
        reset_screen()
        pygame.display.flip()

    if keys[pygame.K_a]:
        moving_object2.x -= velocity
        pygame.display.flip()
        reset_screen()
    if keys[pygame.K_d]:
        moving_object2.x += velocity
        pygame.display.flip()
        reset_screen()
    if keys[pygame.K_w]:
        moving_object2.y -= velocity
        velocity *= 2
        pygame.display.flip()
        reset_screen()
    if keys[pygame.K_s]:
        moving_object2.y += velocity
        pygame.display.flip()
        reset_screen()
    
    pygame.draw.rect(screen, (0,0,255), moving_object)
    pygame.draw.rect(screen, (100,0,0), moving_object2)
    pygame.display.flip()


    