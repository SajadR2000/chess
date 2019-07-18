import pygame
import sys
import piece
from pygame.locals import *
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 255, 255)
width = 713
height = 713
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('chess game')
clock = pygame.time.Clock()
Runing = True

def pieces_Display():
    for x in piece.pieceslist:
        gameDisplay.blit(x.pimg,(width * 0.36 + (x.currentx - 1) * 0.0305 * width ,height * 0.575 - (8 - x.currenty) * 0.0305 * height ))


def Game_loop():
    while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    break
                gameDisplay.fill(white)
                gameDisplay.blit(piece.boardimg,(width * 0.3,height * 0.3))
                pieces_Display()
                pygame.display.update()
                clock.tick(60)
                return 0
                
