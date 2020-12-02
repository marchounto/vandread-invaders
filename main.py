import pygame
import sys
import random



pygame.init()

game_screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("VANDREAD INVADERS")
game_icon = pygame.image.load("robot.png")
pygame.display.set_icon(game_icon)
player = pygame.image.load("robot.png")
playerX = 350
playerY = 500
player_offset = 0
virus_offsetX = 0.7
virus_offsetY = 0.7
running = True

virus = pygame.image.load("coronavirus.png")
virusX = random.randint(60,720)
virusY = random.randint(0,250)

bullet = pygame.image.load("bullet.png")
bulletY=0;
bulletX=0;

background = pygame.image.load("battlefield.png")
background = pygame.transform.scale(background, (800, 600))


def drawPlayer(x , y ):
    game_screen.blit(player,(x, y))

def drawVirus(x,y):
    game_screen.blit(virus, (x, y))

def drawBullet(x,y):
    game_screen.blit(bullet, (x, y))

def checkBoundaries(x, y):
    if x < 0:
        x = 0
    elif x >= 730:
        x = 730
    elif y <0:
        y = 0
    elif y >= 500:
        y = 500
    return x, y



while running:
    game_screen.fill((0, 0, 0))
    game_screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                player_offset = -0.5
            if event.key == pygame.K_RIGHT:
                player_offset = 0.5
            if event.key == pygame.K_SPACE:
                bulletY=playerY
                bulletX=playerX
                drawBullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_offset = 0
    playerX += player_offset
    playerX, playerY = checkBoundaries(playerX, playerY)


    if virusX >= 730:
        virus_offsetX = -0.7
    if virusX <40 :
        virus_offsetX = 0.7
    if virusY >550 :
        virusY = 550
    virusX += virus_offsetX
    virusY += virus_offsetY
    bulletY += -1;


    drawPlayer(playerX, playerY )
    drawVirus(virusX, virusY)
    drawBullet(bulletX, bulletY)
    pygame.display.update()
