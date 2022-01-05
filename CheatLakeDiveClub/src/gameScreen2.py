from inventoryScreen2 import inventory2
from inventoryScreen2 import determineInventory2
import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

air = 0
timeLeft = 0
lookLeft = 0
leftX = -450

def drawGame(screen, bg):
    screen.blit(bg, (0, 0))
    pygame.display.update()

class Sprite:
    def __init__(self, x, y, gender):
        self.x = x
        self.y = y
        self.width = 700
        self.height = 500
        self.gender = gender
        self.hellbender = pygame.image.load("../assets/hellbender.png")
        self.hellbender2 = pygame.image.load("../assets/hellbender2.png")
        self.bubble = pygame.image.load("../assets/Bubbles.png")
        self.background = pygame.image.load("../assets/gamescreen.png")
        self.gameover = pygame.image.load("../assets/game_over.png")

        self.femaleEast = pygame.image.load("../assets/girlMove/Female_east.png")
        self.femaleNorth = pygame.image.load("../assets/girlMove/Female_north.png")
        self.femaleNorthEast = pygame.image.load("../assets/girlMove/Female_northeast.png")
        self.femaleNorthWest = pygame.image.load("../assets/girlMove/Female_northwest.png")
        self.femaleSouth = pygame.image.load("../assets/girlMove/Female_south.png")
        self.femaleSouthEast = pygame.image.load("../assets/girlMove/Female_southeast.png")
        self.femaleSouthWest = pygame.image.load("../assets/girlMove/Female_southwest.png")
        self.femaleWest = pygame.image.load("../assets/girlMove/Female_west.png")

        self.maleEast = pygame.image.load("../assets/boyMove/Male_east.png")
        self.maleNorth = pygame.image.load("../assets/boyMove/Male_north.png")
        self.maleNorthEast = pygame.image.load("../assets/boyMove/Male_northeast.png")
        self.maleNorthWest = pygame.image.load("../assets/boyMove/Male_northwest.png")
        self.maleSouth = pygame.image.load("../assets/boyMove/Male_south.png")
        self.maleSouthEast = pygame.image.load("../assets/boyMove/Male_southeast.png")
        self.maleSouthWest = pygame.image.load("../assets/boyMove/Male_southwest.png")
        self.maleWest = pygame.image.load("../assets/boyMove/Male_west.png")

    def render(self, screen, direction):
        global air

        print('-------------------------------')
        print('PlayerX:', self.x)
        print('PlayerY:', self.y)

        screen.blit(self.background, (self.x, self.y))

        if self.gender == 'female':  # Female Diver
            if (direction == 'northwest'):
                screen.blit(pygame.transform.scale(self.femaleNorthWest, (400, 425)), (600, 300))
            if (direction == 'northeast'):
                screen.blit(pygame.transform.scale(self.femaleNorthEast, (400, 425)), (600, 300))
            if (direction == 'southwest'):
                screen.blit(pygame.transform.scale(self.femaleSouthWest, (400, 425)), (600, 300))
            if (direction == 'southeast'):
                screen.blit(pygame.transform.scale(self.femaleSouthEast, (400, 425)), (600, 300))
            if (direction == 'west'):
                screen.blit(pygame.transform.scale(self.femaleWest, (500, 300)), (600, 300))
            if (direction == 'east'):
                screen.blit(pygame.transform.scale(self.femaleEast, (500, 300)), (600, 300))
            if (direction == 'north'):
                screen.blit(pygame.transform.scale(self.femaleNorth, (300, 500)), (600, 300))
            if (direction == 'south'):
                screen.blit(pygame.transform.scale(self.femaleSouth, (300, 500)), (600, 300))
        else:  # Male Diver
            if (direction == 'northwest'):
                screen.blit(pygame.transform.scale(self.maleNorthWest, (400, 425)), (600, 300))
            if (direction == 'northeast'):
                screen.blit(pygame.transform.scale(self.maleNorthEast, (400, 425)), (600, 300))
            if (direction == 'southwest'):
                screen.blit(pygame.transform.scale(self.maleSouthWest, (400, 425)), (600, 300))
            if (direction == 'southeast'):
                screen.blit(pygame.transform.scale(self.maleSouthEast, (400, 425)), (600, 300))
            if (direction == 'west'):
                screen.blit(pygame.transform.scale(self.femaleWest, (500, 300)), (600, 300))
            if (direction == 'west'):
                screen.blit(pygame.transform.scale(self.maleWest, (500, 300)), (600, 300))
            if (direction == 'east'):
                screen.blit(pygame.transform.scale(self.maleEast, (500, 300)), (600, 300))
            if (direction == 'north'):
                screen.blit(pygame.transform.scale(self.maleNorth, (300, 500)), (600, 300))
            if (direction == 'south'):
                screen.blit(pygame.transform.scale(self.maleSouth, (300, 500)), (600, 300))

        if (air > 4000):
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1500, 800))
        elif (air > 3000):
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1400, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1500, 800))
        elif (air > 2000):
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1300, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1400, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1500, 800))
        elif (air > 1000):
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1200, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1300, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1400, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1500, 800))
        else:
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1100, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1200, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1300, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1400, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1500, 800))

        global leftX

        if (timeLeft > 110):
            air = 5050;

        if (timeLeft > 50):
            screen.blit(pygame.transform.scale(self.hellbender2, (400, 150)), (leftX, 450))
            leftX += 20
        else:
            if(leftX > -450):
                screen.blit(pygame.transform.scale(self.hellbender, (400, 150)), (leftX, 450))
                leftX -= 45
        
               
        effect = pygame.mixer.Sound('../assets/hookednt.wav')
        
        # BEWARE THE HOOKS! THESE KILL THE PLAYER!!!!!!!!!!!!!!
        # (In order from left most hook to right most hook)
        if (self.x > -800 and self.x < -125 and self.y > -2350 and self.y < -2050):
            effect.play()
#             effect.stop()
            air = 5050
        if (self.x > -1200 and self.x < -525 and self.y > -3125 and self.y < -2850):
            effect.play()
#             effect.stop()
            air = 5050
        if (self.x > -4575 and self.x < -3900 and self.y > -2750 and self.y < -2475):
            effect.play()
#             effect.stop()
            air = 5050

def game2(screen, playerGender):
    inventoryItems = [0, 0, 0, 0, 0, 0, 0]
    clock = pygame.time.Clock()
    playerX, playerY = 0, 0
    player = Sprite(-800, -300, playerGender)
    gameContinue = True

    # make air a global value to be used in other functions
    global air
    air = 0
    direction = 'east'

    while gameContinue:
        global timeLeft, lookLeft

        if (lookLeft != 1):
            timeLeft += 1

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                #print(keys[pygame.K_RIGHT], keys[pygame.K_UP])
                if keys[pygame.K_LEFT] and keys[pygame.K_UP] and player.x < -200 and player.y < -100:
                    playerX += 20
                    playerY += 20
                    direction = 'northwest'
                elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN] and player.x < -200 and player.y > -3930:
                    playerX += 20
                    playerY += -20
                    direction = 'southwest'
                elif keys[pygame.K_RIGHT] and keys[pygame.K_UP] and player.x > -5750 and player.y < -100:
                    playerX += -20
                    playerY += 20
                    direction = 'northeast'
                elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and player.x > -5750 and player.y > -3800:
                    playerX += -20
                    playerY += -20
                    direction = 'southeast'
                elif event.key == pygame.K_LEFT and player.x < -200:
                    playerX += 25
                    direction = 'west'
                    timeLeft = 0
                    lookLeft = 1
                elif event.key == pygame.K_RIGHT and player.x > -5750:
                    playerX += -25
                    direction = 'east'
                    lookLeft = 0
                elif event.key == pygame.K_UP and player.y < -200:
                    playerY += 25
                    direction = 'north'
                elif event.key == pygame.K_DOWN and player.y > -3800:
                    playerY += -25
                    direction = 'south'
                elif event.key == pygame.K_i:
                    inventory2(screen, inventoryItems)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    playerX = 0
                if event.key == pygame.K_RIGHT:
                    playerX = 0
                if event.key == pygame.K_UP:
                    playerY = 0
                if event.key == pygame.K_DOWN:
                    playerY = 0

        if (player.y > -300):
            air = 0
        else:
            air += 8

        player.x += playerX
        player.y += playerY
        determineInventory2(player.x, player.y, inventoryItems)
        player.render(screen, direction)

        if(air > 5000):
            return

        clock.tick(60)
        pygame.display.flip()