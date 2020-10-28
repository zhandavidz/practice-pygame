import pygame
pygame.init()

screen_width = 500
screen_height = 480

win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("First Game")

# load imgs
walkRight = [pygame.image.load('img/R1.png'), pygame.image.load('img/R2.png'), pygame.image.load('img/R3.png'), pygame.image.load('img/R4.png'), pygame.image.load('img/R5.png'), pygame.image.load('img/R6.png'), pygame.image.load('img/R7.png'), pygame.image.load('img/R8.png'), pygame.image.load('img/R9.png')]
walkLeft = [pygame.image.load('img/L1.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L7.png'), pygame.image.load('img/L8.png'), pygame.image.load('img/L9.png')]
bg = pygame.image.load('img/bg.jpg')
char = pygame.image.load('img/standing.png')

clock = pygame.time.Clock()

width = 64
height = 64
x = 50
y = screen_height - height
vel = 10

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount

    win.blit(bg, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))
    pygame.display.update()


run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    left = False
    right = False
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
        left = True
    elif keys[pygame.K_RIGHT] and x < screen_width - width:
        x += vel
        right = True
    else:
        walkCount = 0

    if not isJump:
        if keys[pygame.K_UP]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * .5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()

pygame.quit()
