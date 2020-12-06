import pygame
import sys
import random
import math
from pygame import  mixer




pygame.init()

game_screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("VANDREAD INVADERS")
game_icon = pygame.image.load("robot.png")
pygame.display.set_icon(game_icon)
player = pygame.image.load("robot.png")
playerX = 350
playerY = 500
player_offset = 0
virus_offsetX = 0.1
virus_offsetY = 0.1
running = True

virus = pygame.image.load("coronavirus.png")
virusX = random.randint(60,720)
virusY = random.randint(0,75)

bullet = pygame.image.load("bullet.png")
bulletY=0;
bulletX=0;

background = pygame.image.load("battlefield.png")
background = pygame.transform.scale(background, (800, 600))

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10;
textY = 10;


over_font = pygame.font.Font("freesansbold.ttf", 32)



def showScore(x,y):
    score = font.render("Score:  " + str(score_value), True, (255,255,255))
    game_screen.blit(score, (x, y))

def game_over():
    over_text = font.render("Too bad you are infected ", True, (255,255,255))
    game_screen.blit(over_text, (200, 250))




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

def bulletCollisionEnnemy(bullet,ennemy):
    if math.sqrt(((bullet[0]-ennemy[0])**2)+((bullet[1]-ennemy[1])**2)) < 25:
        return True
    else:
        return False




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
        virus_offsetX = -0.1
    if virusX <40 :
        virus_offsetX = 0.1
    if virusY >550 :
        game_over()
        break
    virusX += virus_offsetX
    virusY += virus_offsetY
    bulletY += -0.6;


    drawPlayer(playerX, playerY )
    if bulletCollisionEnnemy([bulletX,bulletY],[virusX,virusY]):
        virusX = random.randint(60, 720)
        virusY = random.randint(0, 250)
        bulletX = -50
        bulletY = -50
        score_value += 1
    drawVirus(virusX, virusY)
    drawBullet(bulletX, bulletY)
    showScore(textX,textY)
    pygame.display.update()
