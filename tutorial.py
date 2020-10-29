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

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    win.blit(bg, (0,0))

    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()

# main loop
man = player(50, 416, 64, 64)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        facing = -1
        if man.right:
            facing = 1
        bullets.append(projectile(man.x + man.width // 2, man.y + man.height // 2, 6, (0,0,0), facing))

    if keys[pygame.K_LEFT] and man.x > 0:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.walkCount = 0
        man.standing = True

    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            # man.right = False
            # man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= round((man.jumpCount ** 2) * .5 * neg)
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
