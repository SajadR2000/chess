import pygame
import sys
import Gameplay
from pygame.locals import *
#Definitions:
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 255, 255)
width = 713
height = 713
#start
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('chess game')
clock = pygame.time.Clock()
Runing = True
while Runing != False:
    for event in pygame.event.get():
        ###Runing = Gameplay.Run()
        if event.type == QUIT:
            pygame.quit()
            Runing = False
            sys.exit()
            break
        gameDisplay.fill(white)
        gameDisplay.blit(Gameplay.piece.boardimg,(width * 0.3,height * 0.3))
        for piece in Gameplay.piece.pieceslist:
            gameDisplay.blit(piece.pimg,(width * 0.36 + (piece.currentx - 1) * 0.0305 * width ,height * 0.575 - (8 - piece.currenty) * 0.03 * height ))
    pygame.display.update()
    clock.tick(5)