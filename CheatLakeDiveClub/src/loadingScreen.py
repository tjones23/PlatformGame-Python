import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

class duck(object):
    def __init__(self, img, x, y, width, height, start, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.start = start
        self.end = end
        self.path = [self.x, self.end]
        self.vel = 10
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (width, height))

    def draw(self, screen):
        self.move('right')
        screen.blit(self.img, (self.x, self.y))

    def move(self, direction):
        if direction == 'right':
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.x = self.start

def drawTitle(screen, textX, textY, bg, sign, mallard_1, mallard_2, mallard_3, diver, promptFont):
    screen.blit(bg, (0, 0))
    if(textX == 720):
        sign_x = 1000
        sign_y = 80
    if(textX == 850):
        sign_x = 1205
        sign_y = 97

    screen.blit(sign, (sign_x, sign_y))
    mallard_1.draw(screen)
    mallard_2.draw(screen)
    mallard_3.draw(screen)
    screen.blit(diver, (0, 0))
    screen.blit(promptFont, (textX, textY))
    pygame.display.update()

def title(screen, width, height):
    if (width == 1920 and height == 1080):
        textX, textY = 850, 750
        y_min, y_max = 700, 800
        sign_width, sign_height = 662, 435
        duck1, duck2, duck3 = 500, 505, 550
    else:
        textX, textY = 720, 650
        y_min, y_max = 600, 700
        sign_width, sign_height = 550, 370
        duck1, duck2, duck3 = 415, 420, 450

    pygame.display.set_caption("Cheat Lake Dive Club")
    clock = pygame.time.Clock()

    # Rockwell Nova MS
    myfont = pygame.font.Font('../assets/fredoka.ttf', 100)
    promptFont = myfont.render('Press A to Begin', True, (255, 255, 255))

    # Load Background + Scale
    bg = pygame.image.load('../assets/background.png')
    bg = pygame.transform.scale(bg, (width, height))

    # Play Background Sounds
    pygame.mixer.music.load("../assets/Lake_Sounds.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.3)

    # Load Assets + Scale
    sign = pygame.image.load('../assets/CheatLakeSign.png')
    sign = pygame.transform.scale(sign, (sign_width, sign_height))
    diver = pygame.image.load('../assets/diver.png')
    diver = pygame.transform.scale(diver, (width, height))
    mallard_1 = duck('../assets/Mallard.png', -300, duck1, 97, 50, -300, 2300)
    mallard_2 = duck('../assets/Mallard.png', -150, duck2, 117, 60, -150, 2450)
    mallard_3 = duck('../assets/Mallard.png', -255, duck3, 136, 70, -255, 2345)

    # Title Screen Loop

    introContinue = True
    down = 1
    redUnicode = 0
    keyHit = False

    while introContinue:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pygame.quit()

        if keys[pygame.K_a]:
            keyHit = True

        if keyHit == True:
            redUnicode += 5
            promptFont = myfont.render('Press A to Begin', True, (redUnicode, 0, 0))
            if(redUnicode == 200):
                introContinue = False

        if (textY <= y_max and down == 1):
            textY += 2
        if (textY == y_max and down == 1):
            down = 0
        if (down == 0):
            textY -= 2
        if (textY == y_min and down == 0):
            down = 1

        drawTitle(screen, textX, textY, bg, sign, mallard_1, mallard_2, mallard_3, diver, promptFont)
