import pygame
import random

pygame.init()

def multiplayer():
    start_time = 0
    timer = 0
    #Setting up the python window
    flags = pygame.FULLSCREEN
    screen = pygame.display.set_mode((650, 650))
    pygame.display.set_caption('Motorcycle Game')
    clock = pygame.time.Clock()

    obstacles = random.randint(1,5)
    #obstacles1 = random.randint(1,5)
    obstacles2 = random.randint(1,5)
    #obstacles3 = random.randint(1,5)
    #obstacles4 = random.randint(1,5)
    yy = 0
    yyy = 0


    def reset_screen():
        screen.fill((124,252,0))
        pygame.display.flip()

        #Main Road
        pygame.draw.rect(screen, (0,0,0), [145,0,375,650], 0)

        #Lane Stripes
        pygame.draw.rect(screen, (255,255,255), [325,yyy,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy+80,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy+160,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy+240,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy+320,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy+400,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy+480,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy+560,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy+640,10,40], 0)

        pygame.draw.rect(screen, (255,255,255), [325,yyy,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy-80,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy-160,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy-240,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy-320,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy-400,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy-480,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy-560,10,40], 0)
        pygame.draw.rect(screen, (255,255,255), [325,yy-640,10,40], 0)

        pygame.display.update()
        

        if obstacles == 1:
            pygame.draw.rect(screen,(255,165,0), [370,yy,150,50], 0)
        elif obstacles == 2:
            pygame.draw.rect(screen,(255,165,0), [395,yy,125,50], 0)
            pygame.draw.rect(screen,(255,165,0), [336.5,yy,30,50], 0)
        elif obstacles == 3:
            pygame.draw.rect(screen,(255,165,0), [450,yy,70,50], 0)
            pygame.draw.rect(screen,(255,165,0), [336.5,yy,75,50], 0)
        elif obstacles == 4:
            pygame.draw.rect(screen,(255,165,0), [475,yy,45,50], 0)
            pygame.draw.rect(screen,(255,165,0), [336.5,yy,100,50], 0)
        elif obstacles == 5:
            pygame.draw.rect(screen,(255,165,0), [336.5,yy,145,50], 0)
        
        
        if obstacles2 == 1:
            pygame.draw.rect(screen,(255,255,0), [180,yy,145,50], 0)
        elif obstacles2 == 2:
            pygame.draw.rect(screen,(255,255,0), [204,yy,120,50], 0)
            pygame.draw.rect(screen,(255,255,0), [145,yy,30,50], 0)
        elif obstacles2 == 3:
            pygame.draw.rect(screen,(255,255,0), [250,yy,75,50], 0)
            pygame.draw.rect(screen,(255,255,0), [145,yy,70,50], 0)
        elif obstacles2 == 4:
            pygame.draw.rect(screen,(255,255,0), [295,yy,30,50], 0)
            pygame.draw.rect(screen,(255,255,0), [145,yy,115,50], 0)
        elif obstacles2 == 5:
            pygame.draw.rect(screen,(255,255,0), [145,yy,145,50], 0)
        
    x = 425
    y = 600
    w = 20
    h = 45
    X = x - 200
    Y = 600
    W = 20
    H = 45
    velocity = 5    
    reset_screen()
    #Game Loop
    running = True
    while running == True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        moving_object = pygame.Rect(x,yy,w,h)
        moving_object2 = pygame.Rect(X,yy,W,H) 
        pygame.display.update()

        if event.type == pygame.KEYDOWN:
            start_time = pygame.time.get_ticks()
            timer = start_time / 1000
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= velocity
        if keys[pygame.K_RIGHT]:
            x += velocity
        #if keys[pygame.K_UP]:
        #    y -= velocity
        #if keys[pygame.K_DOWN]:
        #    y += velocity

        if keys[pygame.K_a]:
            X -= velocity
        if keys[pygame.K_d]:
            X += velocity
        #if keys[pygame.K_w]:
        #    Y -= velocity
        #if keys[pygame.K_s]:
        #    Y += velocity
        yy+=5
        yyy+=5
        if yy > 650:
            yy = 0
            obstacles = random.randint(1,5)
            obstacles2 = random.randint(1,5)
        if yyy > 650:
            yyy = 0



        reset_screen()
        pygame.draw.rect(screen, (0,0,255), (x,y,w,h))
        pygame.draw.rect(screen, (100,0,0), (X,Y,W,H))
        pygame.display.update()

    if timer >= 60:
        timer = timer/60
        print(f'{timer} minutes')
    else:
        print(f'{timer} seconds')

def single_player():
    start_time = 0
    timer = 0  
    obstacle1 = pygame.Rect(215,0,305,100)
    obstacle2 = obstacle1
    #Setting up the python window
    flags = pygame.FULLSCREEN
    screen = pygame.display.set_mode((650, 650))
    pygame.display.set_caption('Motorcycle Game')
    clock = pygame.time.Clock()

    obstacles = random.randint(1,5)
    yy = 0 


    def reset_screen():
        screen.fill((124,252,0))
        pygame.display.flip()

        #Main Road
        pygame.draw.rect(screen, (0,0,0), [145,0,375,650], 0)

        pygame.display.update()


        if obstacles == 1:
            obstacle1 = pygame.Rect(215,yy,305,100)
            obstacle2 = obstacle1
            pygame.draw.rect(screen,(255,0,255), obstacle1)
        elif obstacles == 2:
            obstacle1 = pygame.Rect(275,yy,245,100)
            obstacle2 = pygame.Rect(145,yy,60,100)
            pygame.draw.rect(screen,(255,0,255), obstacle1)
            pygame.draw.rect(screen,(255,0,255), obstacle2)
            #pygame.draw.rect(screen,(255,0,255), [275,0,245,100], 0)
            #pygame.draw.rect(screen,(255,0,255), [145,0,60,100], 0)
        elif obstacles == 3:
            obstacle1 = pygame.Rect(370,yy,150,100)
            obstacle2 = pygame.Rect(145,yy,150,100)
            pygame.draw.rect(screen,(255,0,255), obstacle1)
            pygame.draw.rect(screen,(255,0,255), obstacle2)
            #pygame.draw.rect(screen,(255,0,255), [370,0,150,100], 0)
            #pygame.draw.rect(screen,(255,0,255), [145,0,150,100], 0)
        elif obstacles == 4:
            obstacle1 = pygame.Rect(445,yy,75,100)
            obstacle2 = pygame.Rect(145,yy,225,100)
            pygame.draw.rect(screen,(255,0,255), obstacle1)
            pygame.draw.rect(screen,(255,0,255), obstacle2)
            #pygame.draw.rect(screen,(255,0,255), [445,0,75,100], 0)
            #pygame.draw.rect(screen,(255,0,255), [145,0,225,100], 0)
        elif obstacles == 5:
            obstacle1 = pygame.Rect(145,yy,300,100)
            obstacle2 = obstacle1
            pygame.draw.rect(screen,(255,0,255), obstacle1)
            #pygame.draw.rect(screen,(255,0,255), [145,0,300,100], 0)
    x = 315
    y = 525
    w = 50
    h = 100
    reset_screen()
    #Game Loop
    running = True
    while running == True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        velocity = 5
        moving_object = pygame.Rect(x,y,w,h)

        if event.type == pygame.KEYDOWN:
            start_time = pygame.time.get_ticks()
            timer = start_time / 1000

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= velocity
        if keys[pygame.K_RIGHT]:
            x += velocity
        #if keys[pygame.K_UP]:
        #    y -= velocity
        #if keys[pygame.K_DOWN]:
        #    y += velocity
        yy += 5
        reset_screen()
        if yy == 650:
            yy = 0
            obstacles = obstacles = random.randint(1,5)
        #pygame.draw.rect(screen,(255,0,255), obstacle1)
        pygame.draw.rect(screen, (0,0,255), (x,y,w,h))
        pygame.display.update()
        #obstacles = obstacles = random.randint(1,5)

    if timer >= 60:
        timer = timer/60
        print(f'{timer:.2f} minutes')
    else:
        print(f'{timer:.2f} seconds')

    

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