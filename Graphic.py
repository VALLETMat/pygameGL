import os
import pygame
import Inventory


from Cell import *
from Entity import *
from Board import *

def drawTEXT(fenetre, string):
    font = pygame.font.SysFont("monospace", 15)

    pygame.draw.rect(fenetre, (1,1,1), [550, 10, 650, 50], 0)
    pygame.draw.rect(fenetre, (251,251,251), [550, 10, 650, 50], 1)

    desc = font.render(string, 1, (255,255,255))
    fenetre.blit(desc, (550,10))
    pygame.display.flip()

def drawInfo(fenetre,player):
    font = pygame.font.SysFont("monospace", 15)

    pygame.draw.rect(fenetre, (1,1,1), [50, 555, 375, 150], 0)
    pygame.draw.rect(fenetre, (251,251,251), [50, 555, 375, 150], 1)

    lvl = font.render("LVL : 1" , 1, (255,255,255))
    hp =  font.render("HP :  "+ str(player.HP) , 1, (255,255,255))
    ATK = font.render("ATK : "+ str(player.ATK) , 1, (255,255,255))
    defense = font.render("DEF : "+ str(player.DEF) , 1, (255,255,255))
    if player.inventory.Armor is None:
        armor  = font.render("Armor : Butt-naked" , 1, (255,255,255))
    else :
        armor  = font.render("Armor :     "+ player.inventory.Armor.inspect() , 1, (255,255,255))
    if player.inventory.Accessory is None:
        access = font.render("Accessory : None" , 1, (255,255,255))
    else:
        access = font.render("Accessory : "+ player.inventory.Accessory.inspect() , 1, (255,255,255))
    if player.inventory.Weapon is None:
        weapon = font.render("Weapon :    Fist" , 1, (255,255,255))
    else :
        weapon = font.render("Weapon :    "+ player.inventory.Weapon.inspect() , 1, (255,255,255))

    fenetre.blit(lvl, (50,555))
    fenetre.blit(hp,  (50,590))
    fenetre.blit(ATK, (50,625))
    fenetre.blit(defense, (50,660))
    fenetre.blit(weapon, (200,555))
    fenetre.blit(access, (200,600))
    fenetre.blit(armor,  (200,650))

def entitiesAct(entities,player,board):
    for e in entities:
        e.act(player,board)
def getPos(position,board):
    return (int(position[0]/55),int(position[1]/55))

def drawBoard(board,player):
    for i in range(10):
        for j in range(10):
            if(board.cells[i][j].__class__ == StairUp(-1,-1,None).__class__):
                sprite = pygame.image.load(board.cells[i][j].underneath_sprite_path).convert_alpha()
                fenetre.blit(sprite,(i*55,j*55))
            sprite = pygame.image.load(board.cells[i][j].sprite_path).convert_alpha()
            fenetre.blit(sprite,(i*55,j*55))
            if board.cells[i][j].item is not None:
                sprite = pygame.image.load(board.cells[i][j].item.sprite_path).convert_alpha()
                fenetre.blit(sprite,(i*55+3,j*55+3))
            if board.cells[i][j].occupying is not None:
                sprite = pygame.image.load(board.cells[i][j].occupying.sprite_path).convert_alpha()
                fenetre.blit(sprite,(i*55+3,j*55+3))
    drawInfo(fenetre,player)
    pygame.display.flip()

def play():
    board = Board(10)
    player = Player(board.cells[2][2])
    rat = Rat(board.cells[7][7])

    entities = [rat]
    drawBoard(board,player)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    player.moveUp(board)
                if event.key == pygame.K_s:
                        player.moveDown(board)
                if event.key == pygame.K_q:
                         player.moveLeft(board)
                if event.key == pygame.K_d:
                      player.moveRight(board)

                player.applyMove(board)
                drawBoard(board,player)
                entitiesAct(entities,player,board)
                drawBoard(board,player)
            if event.type == pygame.MOUSEBUTTONDOWN:
                tuplePos = getPos(pygame.mouse.get_pos(),board)
                if posIsCorrect(board,tuplePos[0],tuplePos[1]):
                    cell = board.cells[tuplePos[0]][tuplePos[1]]
                    drawBoard(board,player)
                    cell.interract(player)
                    entitiesAct(entities,player,board)
                    drawBoard(board,player)
            if event.type == pygame.MOUSEMOTION:
                if abs(pygame.mouse.get_rel()[0]) +abs(pygame.mouse.get_rel()[1]) ==1:
                    tuplePos = getPos(pygame.mouse.get_pos(),board)
                    if posIsCorrect(board,tuplePos[0],tuplePos[1]):
                        cell = board.cells[tuplePos[0]][tuplePos[1]]
                        if cell.occupying is not None or cell.item is not None:
                            drawBoard(board,player)
                            drawTEXT(fenetre,cell.inspect())

pygame.init()
fenetre = pygame.display.set_mode((750, 750))
pygame.key.set_repeat(300,300)
play()
