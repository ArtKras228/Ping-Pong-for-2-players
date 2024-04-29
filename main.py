import pygame
pygame.init()
from classes import Player_1, Player_2, Enemy

def game():
    win.fill((25,110,22))
    player_1.move()
    player_1.reset()
    player_2.move()
    player_2.reset()

def end_game():
    pass

win = pygame.display.set_mode((800,600))
win.fill((25,110,22))
pygame.display.set_caption('PingPong')

run = True 
finish = False
clock = pygame.time.Clock()
player_1 = Player_1('1rocket.png', 760, 225, 25, 200, 10, win)
player_2 = Player_2('2rocket.png', 15, 225, 25, 200, 10, win)

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    
    if not finish:
        game()
    else:
        end_game()

    pygame.display.update()
    clock.tick(60)