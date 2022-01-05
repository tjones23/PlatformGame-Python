from loadingScreen import title
from genderScreen import gender
from gameScreen1 import game1
from gameScreen2 import game2
from finalScreen import gameOver

import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

def main():
    #Two Options
    #Option 1 - 1920 x 1080 (width x height)
    #Option 2 - 1600 x 900

    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

    while (True):
        title(screen, width, height)
        playerGender = gender(screen, width, height)

        keepPlaying = 1
        while (keepPlaying == 1):
            if (width == 1920 and height == 1080):      #1920 x 1080
                game1(screen, playerGender)
            else:                                       #1600 x 900 (everything else)
                game2(screen, playerGender)

            choice = gameOver(screen, width, height)

            if choice == 1:
                keepPlaying = 0
            if choice == 3:
                pygame.quit()

main()