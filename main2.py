import random
import pygame
import math

pygame.init()
screen=pygame.display.set_mode((900,800))
pygame.display.set_caption("Space Invaders")
#player
player_img=pygame.Surface((64,64))
player_img.fill((0,255,0))
player_x=370
player_y=480
player_x_change=0

#enemy
enemy_img=pygame.Surface((64,64))
enemy_img.fill((255,0,0))
enemy_x=random.randint(0,736)
enemy_y=random.randint(50,150)
enemy_x_change=2
enemy_y_change=20

#bullet
bullet_img=pygame.Surface((8,20))
bullet_img.fill((0,0,255))
bullet_x=0
bullet_y=480
bullet_y_change=10
bullet_state="ready"

#score
score=0
font=pygame.font.Font(None,36)
text_x=10
text_y=10

def show_score(x,y):
    score_value=font.render("Score : "+str(score),True,(255,255,255))
    screen.blit(score_value,(x,y))

def player(x,y):
    screen.blit(player_img,(x,y))

def enemy(x,y):
    screen.blit(enemy_img,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet_img,(x+28,y+10))

def is_collision(enemy_x,enemy_y,bullet_x,bullet_y):
    distance=math.sqrt((math.pow(enemy_x-bullet_x,2))+(math.pow(enemy_y-bullet_y,2)))
    return distance<27