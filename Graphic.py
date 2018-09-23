import os
import pygame
from Cell import *
from Entity import *
from Board import *
def drawBoard(board):
    for i in range(10):
        for j in range(10):
            sprite = pygame.image.load(board.cells[i][j].sprite_path).convert_alpha()
            fenetre.blit(sprite,(i*55,j*55))
            if board.cells[i][j].occupying is not None:
                sprite = pygame.image.load(board.cells[i][j].occupying.sprite_path).convert_alpha()
                fenetre.blit(sprite,(i*55+3,j*55+3))
    pygame.display.flip()


def play():
    board = Board(10)
    player = Player(board.cells[1][1])

    drawBoard(board)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    player.moveUp(board)
                    drawBoard(board)
                if event.key == pygame.K_s:
                    player.moveDown(board)
                    drawBoard(board)
                if event.key == pygame.K_q:
                     player.moveLeft(board)
                     drawBoard(board)
                if event.key == pygame.K_d:
                      player.moveRight(board)
                      drawBoard(board)

pygame.init()
fenetre = pygame.display.set_mode((750, 750))
pygame.key.set_repeat(300,300)
play()
