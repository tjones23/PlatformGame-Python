import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

def drawFinal():
    print('Temp')

def gameOver(screen, width, height):
    mainMenu = pygame.image.load('../assets/gameMenu.png')
    restart = pygame.image.load('../assets/gameRestart.png')
    nextLevel = pygame.image.load('../assets/gameLevel.png')

    mainMenu = pygame.transform.scale(mainMenu, (width, height))
    restart = pygame.transform.scale(restart, (width, height))
    nextLevel = pygame.transform.scale(nextLevel, (width, height))
    cont = 1

    screen.blit(mainMenu, (0, 0))
    pygame.display.update()

    if (width == 1920 and height == 1080):
        y_min, y_max = 790, 850
        x1_min, x1_max = 180, 560
        x2_min, x2_max = 810, 1096
        x3_min, x3_max = 1376, 1750
    else:
        y_min, y_max = 650, 730
        x1_min, x1_max = 150, 460
        x2_min, x2_max = 670, 920
        x3_min, x3_max = 1140, 1450

    while cont == 1:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()

            x, y = pygame.mouse.get_pos()

            if(y > y_min and y < y_max):
                if(x > x1_min and x < x1_max):
                    screen.blit(mainMenu, (0, 0))
                if(x > x2_min and x < x2_max):
                    screen.blit(restart, (0, 0))
                if(x > x3_min and x < x3_max):
                    screen.blit(nextLevel, (0, 0))

            pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
            if(y > y_min and y < y_max and pressed1 == 1):
                if(x > x1_min and x < x1_max and pressed1 == 1):
                    return 1
                if(x > x2_min and x < x2_max and pressed1 == 1):
                    return 2
                if(x > x3_min and x < x3_max and pressed1 == 1):
                    return 3

            pygame.display.update()


