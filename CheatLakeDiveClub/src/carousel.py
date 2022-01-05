import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

def drawCarousel(screen, width, height, path):
    bg = pygame.image.load(path)
    bg = pygame.transform.scale(bg, (width, height))

    screen.blit(bg, (0, 0))
    pygame.display.update()

def directory(screen, width, height, path):
    for i in range(0, 25, 2):
        if(i < 10):
            final = '0' + str(i) + '.jpeg'
        else:
            final = str(i) + '.jpeg'
        drawCarousel(screen, width, height, path + final)

def rotate(screen, width, height, option):
    if(option == 0):
        path = '../assets/girlLeft/Gender Screen GIF_0000'
        directory(screen, width, height, path)
    if (option == 1):
        path = '../assets/girlRight/Gender Screen GIF_0000'
        directory(screen, width, height, path)
    if (option == 2):
        path = '../assets/boyLeft/Gender Screen GIF_0000'
        directory(screen, width, height, path)
    if (option == 3):
        path = '../assets/boyRight/Gender Screen GIF_0000'
        directory(screen, width, height, path)