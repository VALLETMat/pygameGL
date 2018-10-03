import os
import pygame
import Inventory

from Cell import *
from Entity import *
from Board import *

def drawInventory(fenetre,board,player,selected):
    pygame.draw.rect(fenetre,(1,1,1),[0, 0, 750, 750],0)
    drawInfo(fenetre,player)
    pygame.display.flip()
    font = pygame.font.SysFont("monospace", 15)

    ind = 0
    for it in player.inventory.items:
        if(selected == ind):
            i = font.render(">", 1, (255,255,255))
            fenetre.blit(i, (40, 100 + ind * 30))
        item_name = font.render(it.name(), 1, (255,255,255))
        fenetre.blit(item_name, (55,100 + ind * 30))
        ind += 1
    pygame.display.flip()

def inventoryMode(fenetre,board,player):
    selected = 0
    drawInventory(fenetre,board,player,selected)
    quit = False
    while(not quit):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    quit = True
                if event.key == pygame.K_z:
                    selected = max(selected-1,0)
                if event.key == pygame.K_s:
                    selected = min(selected+1,len(player.inventory.items)-1)
                    print(str(selected)+" "+str(len(player.inventory.items)))
                if event.key == pygame.K_SPACE:
                    player.inventory.equip(player.inventory.items,selected)

                drawInventory(fenetre,board,player,selected)
    drawBoard(board,player)

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

    hp =  font.render("HP :  "+ str(player.HP+player.inventory.getHP()) , 1, (255,255,255))
    ATK = font.render("ATK : "+ str(player.ATK+player.inventory.getATK()) , 1, (255,255,255))
    defense = font.render("DEF : "+ str(player.DEF+player.inventory.getDEF()) , 1, (255,255,255))
    if player.inventory.Armor is None:
        armor  = font.render("Armor : Butt-naked" , 1, (255,255,255))
    else :
        armor  = font.render("Armor :     "+ player.inventory.Armor.name() , 1, (255,255,255))
    if player.inventory.Accessory is None:
        access = font.render("Accessory : None" , 1, (255,255,255))
    else:
        access = font.render("Accessory : "+ player.inventory.Accessory.name() , 1, (255,255,255))
    if player.inventory.Weapon is None:
        weapon = font.render("Weapon :    Fist" , 1, (255,255,255))
    else :
        weapon = font.render("Weapon :    "+ player.inventory.Weapon.name() , 1, (255,255,255))

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
    game = Game()
    level = 0
    board = game.boards[level]
    player = Player(board.cells[2][2])
    drawBoard(board,player)
    gameOver = False

    while(not gameOver):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    inventoryMode(fenetre,board,player)
                if event.key == pygame.K_z:
                    player.moveUp(board)
                if event.key == pygame.K_s:
                        player.moveDown(board)
                if event.key == pygame.K_q:
                         player.moveLeft(board)
                if event.key == pygame.K_d:
                      player.moveRight(board)
                if event.key == pygame.K_z or event.key == pygame.K_q or event.key == pygame.K_s or event.key == pygame.K_d:
                    player.applyMove(board)
                    drawBoard(board,player)
                    entitiesAct(board.entities,player,board)
                    drawBoard(board,player)
            if event.type == pygame.MOUSEBUTTONDOWN:
                tuplePos = getPos(pygame.mouse.get_pos(),board)

                if not posIsCorrect(board,tuplePos[0],tuplePos[1]):
                    return
                cell = board.cells[tuplePos[0]][tuplePos[1]]
                if board.cells[tuplePos[0]][tuplePos[1]].occupying is not None:
                    drawBoard(board,player)
                    cell.interract(player)
                    entitiesAct(board.entities,player,board)
                    drawBoard(board,player)
                    drawTEXT(fenetre,cell.inspect())

                if cell.__class__.__name__ == 'StairDown':
                    board.cells[player.position.x][player.position.y].occupying = None
                    level -=1
                    board = game.boards[level]
                    player.position = board.cells[player.position.x][player.position.y]
                    board.cells[player.position.x][player.position.y].occupying = player
                    entities = board.entities
                    drawBoard(board,player)
                elif posIsCorrect(board,tuplePos[0],tuplePos[1]) and cell.__class__.__name__ == 'StairDown':
                    board.cells[player.position.x][player.position.y].occupying = None
                    level +=1
                    board = game.boards[level]
                    player.position = board.cells[player.position.x][player.position.y]
                    board.cells[player.position.x][player.position.y].occupying = player
                    entities = board.entities
                    drawBoard(board,player)
            if event.type == pygame.MOUSEMOTION:
                if abs(pygame.mouse.get_rel()[0]) +abs(pygame.mouse.get_rel()[1]) ==1:
                    tuplePos = getPos(pygame.mouse.get_pos(),board)
                    if posIsCorrect(board,tuplePos[0],tuplePos[1]):
                        cell = board.cells[tuplePos[0]][tuplePos[1]]
                        if cell.occupying is not None or cell.item is not None:
                            drawBoard(board,player)
                            drawTEXT(fenetre,cell.inspect())
        for e in board.entities:
            if e.HP <= 0:
                board.entities.remove(e)
                board.cells[e.position.x][e.position.y].occupying = None
                drawBoard(board,player)
        if(player.HP <= 0 ):
            gameOver = True
    print("Game Over, thanks for playing")
pygame.init()
fenetre = pygame.display.set_mode((750, 750))
pygame.key.set_repeat(300,300)
play()
