import pygame

pygame.init()

def multiplayer():
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

def single_player():   
    #Setting up the python window
    flags = pygame.FULLSCREEN
    screen = pygame.display.set_mode((650, 650))
    pygame.display.set_caption('Motorcycle Game')


    def reset_screen():
        screen.fill((124,252,0))
        pygame.display.flip()

        #Main Road
        pygame.draw.rect(screen, (0,0,0), [145,0,375,650], 0)

        '''
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
        '''
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
        #moving_object2 = pygame.Rect(x-200,y,w,h) 
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
        '''
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
        '''
        pygame.draw.rect(screen, (0,0,255), moving_object)
        #pygame.draw.rect(screen, (100,0,0), moving_object2)
        pygame.display.flip()

#Creating user interface
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((650, 650))
pygame.display.set_caption('Motorcycle Game')


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            
            white = (255, 255, 255)
            green = (0, 255, 0)
            blue = (0, 0, 128)

            
            X = 400
            Y = 400

            
            display_surface = pygame.display.set_mode((X, Y))

        
            pygame.display.set_caption('Motorcycle Game')

           
            font = pygame.font.Font('freesansbold.ttf', 32)


            
            text = font.render('Single Player', True, green, blue)
            text2 = font.render('MultiPlayer', True, green, blue)

            
            textRect = text.get_rect()
            textRect2 = text2.get_rect()

            
            textRect.center = (X // 2, Y // 2)
            textRect2.center = (X // 2, (Y+100) // 2)

        while running:

            display_surface.fill(white)

            display_surface.blit(text, textRect)
            display_surface.blit(text2, textRect2)

            for event in pygame.event.get():

                
                if event.type == pygame.QUIT:

                    
                    pygame.quit()

                    
                    quit()

                
                pygame.display.update()
                
           
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if textRect2.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, (0,0,0), [145,0,375,650], 0)
                    pygame.display.update()
                    multiplayer()
                    running = False
                elif textRect.collidepoint(mouse_pos):
                    single_player()
                    running = False
                
'''
'''