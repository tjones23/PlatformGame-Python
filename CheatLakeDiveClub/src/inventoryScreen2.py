import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

def drawInventory2(screen, bg, inventoryItems):
    screen.blit(bg, (0, 0))
    pygame.display.update()

    if(inventoryItems[0] == 1):
        door = pygame.image.load('../assets/door.png')
        door = pygame.transform.scale(door, (100, 130))
        screen.blit(door, (85, 172))
    if (inventoryItems[1] == 1):
        fender = pygame.image.load('../assets/fender.png')
        fender = pygame.transform.scale(fender, (120, 80))
        screen.blit(fender, (85, 360))
    if (inventoryItems[2] == 1):
        wheel = pygame.image.load('../assets/wheel.png')
        wheel = pygame.transform.scale(wheel, (130, 130))
        screen.blit(wheel, (75, 510))
    if (inventoryItems[3] == 1):
        windshield = pygame.image.load('../assets/windshield.png')
        windshield = pygame.transform.scale(windshield, (125, 125))
        screen.blit(windshield, (80, 680))
    if (inventoryItems[4] == 1):
        nail = pygame.image.load('../assets/nail.png')
        nail = pygame.transform.scale(nail, (25, 115))
        screen.blit(nail, (320, 180))
    if (inventoryItems[5] == 1):
        barrel = pygame.image.load('../assets/barrel.png')
        barrel = pygame.transform.scale(barrel, (90, 130))
        screen.blit(barrel, (285, 340))
    pygame.display.update()

def inventory2(screen, inventoryItems):
    bg = pygame.image.load('../assets/Inventory.png')
    bg = pygame.transform.scale(bg, (1600, 900))
    cont = 1

    while cont == 1:
        for event in pygame.event.get():
            drawInventory2(screen, bg, inventoryItems)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    cont = 0

def determineInventory2(playerX, playerY, inventoryItems):
    effect = pygame.mixer.Sound('../assets/gotcha.wav')
    if(playerX > -5125 and playerX < -4500 and playerY > -2500 and playerY < -1875):
        if(inventoryItems[0] != 1):
            effect.play()
        inventoryItems[0] = 1
    if (playerX > -500 and playerX < 75 and playerY > -4125 and playerY < -3750):
        if(inventoryItems[1] != 1):
            effect.play()
        inventoryItems[1] = 1
        
    if (playerX > -2075 and playerX < -1300 and playerY > -3900 and playerY < -3450):
        if(inventoryItems[2] != 1):
            effect.play()
        inventoryItems[2] = 1
        
    if (playerX > -5900 and playerX < -5550 and playerY > -4000 and playerY < -3700):
        if(inventoryItems[3] != 1):
            effect.play()
        inventoryItems[3] = 1
        
    if (playerX > -300 and playerX < 100 and playerY > -4100 and playerY < -3700):
        if(inventoryItems[4] != 1):
            effect.play()
        inventoryItems[4] = 1
    if (playerX > -3500 and playerX < -2800 and playerY > -4100 and playerY < -3600):
        if(inventoryItems[5] != 1):
            effect.play()
        inventoryItems[5] = 1
        