
import pygame

pygame.init()

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
            # define the RGB value for white,
            #  green, blue colour .
            white = (255, 255, 255)
            green = (0, 255, 0)
            blue = (0, 0, 128)

            # assigning values to X and Y variable
            X = 400
            Y = 400

            # create the display surface object
            # of specific dimension..e(X, Y).
            display_surface = pygame.display.set_mode((X, Y))

            # set the pygame window name
            pygame.display.set_caption('Motorcycle Game')

            # create a font object.
            # 1st parameter is the font file
            # which is present in pygame.
            # 2nd parameter is size of the font
            font = pygame.font.Font('freesansbold.ttf', 32)


            # create a text surface object,
            # on which text is drawn on it.
            text = font.render('Single Player', True, green, blue)
            text2 = font.render('MultiPlayer', True, green, blue)

            # create a rectangular object for the
            # text surface object
            textRect = text.get_rect()
            textRect2 = text2.get_rect()

            # set the center of the rectangular object.
            textRect.center = (X // 2, Y // 2)
            textRect2.center = (X // 2, (Y+100) // 2)

            # infinite loop
            while True:

                # completely fill the surface object
                # with white color
                display_surface.fill(white)

                # copying the text surface object
                # to the display surface object
                # at the center coordinate.
                display_surface.blit(text, textRect)
                display_surface.blit(text2, textRect2)

                # iterate over the list of Event objects
                # that was returned by pygame.event.get() method.
                for event in pygame.event.get():

                    # if event object type is QUIT
                    # then quitting the pygame
                    # and program both.
                    if event.type == pygame.QUIT:

                        # deactivates the pygame library
                        pygame.quit()

                        # quit the program.
                        quit()

                    # Draws the surface object to the screen.
                    pygame.display.update()
                    
                    # Detect mouse button down event
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # event.button represents which mouse button was clicked:
                        # 1: Left mouse button
                        # 2: Middle mouse button (scroll wheel)
                        # 3: Right mouse button
                        # 4: Scroll up
                        # 5: Scroll down
                        pygame.draw.rect(screen, (0,0,0), [145,0,375,650], 0)
                        pygame.display.update()
                        break
                    












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
'''
'''