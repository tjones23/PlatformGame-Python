from carousel import rotate

import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

def drawGender(screen, bg):
    screen.blit(bg, (0, 0))
    pygame.display.update()

def gender(screen, width, height):
    bg = pygame.image.load('../assets/gender_girl.png')
    bg = pygame.transform.scale(bg, (width, height))
    drawGender(screen, bg)

    # Gender Screen Loop
    genderContinue = True
    currentGender = 'female'

    while genderContinue:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()

            if currentGender == 'female' and keys[pygame.K_LEFT]:
                currentGender = 'male'
                rotate(screen, width, height, 0)
            elif currentGender == 'female' and keys[pygame.K_RIGHT]:
                currentGender = 'male'
                rotate(screen, width, height, 1)
            elif currentGender == 'male' and keys[pygame.K_LEFT]:
                currentGender = 'female'
                rotate(screen, width, height, 2)
            elif currentGender == 'male' and keys[pygame.K_RIGHT]:
                currentGender = 'female'
                rotate(screen, width, height, 3)
            elif keys[pygame.K_SPACE] and currentGender == 'female':
                genderContinue = False
            elif keys[pygame.K_SPACE] and currentGender == 'male':
                genderContinue = False

    return currentGender