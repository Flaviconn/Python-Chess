#DONT FORGET EDITS WERE MADE IN PYGAME ROGERS MODULE!!! (image.convert_alpha())
#changed masking code in pygame rogers to allow for 80x80 pawn dimensions
import pygame
import random
import math
import time
from pygameRogers import Game
from pygameRogers import Room
from pygameRogers import GameObject
from pygameRogers import TextRectangle

path = "SAVE.txt"
file = open(path, "r")


#   -
#   RESOURCES
#   -

#Create a new game
g = Game(820,640)

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
TAN = (204, 194, 139)

#Global Variables
CLICKED = None
GAME = 1

#background
simpleBackground = g.makeBackground(TAN)

#All my images!
CB = g.makeSpriteImage("CB.png")
BOARD1= g.makeSpriteImage("BOARD1.png")
BOARD2= g.makeSpriteImage("BOARD2.png")
BOARD1S= g.makeSpriteImage("BOARD1S.png")
BOARD2S= g.makeSpriteImage("BOARD2S.png")
START= g.makeSpriteImage("INTRO.png")

#Default chess board
PBoard=[['BR.png', 'BN.png', 'BB.png', 'BQ.png', 'BK.png', 'BB.png', 'BN.png', 'BR.png'],
        ['BP.png', 'BP.png', 'BP.png', 'BP.png', 'BP.png', 'BP.png', 'BP.png', 'BP.png'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['WP.png', 'WP.png', 'WP.png', 'WP.png', 'WP.png', 'WP.png', 'WP.png', 'WP.png'],
        ['WR.png', 'WN.png', 'WB.png', 'WQ.png', 'WK.png', 'WB.png', 'WN.png', 'WR.png']]

#creating a board from the save
LBoard=[]

for i in range(0,8):
    Temp=file.readline()
    if Temp == "" :
        break
    else:
        TempList=((((Temp.rstrip("\n")).replace("'", "")).split(" ")))
        LBoard.append(TempList)

print(LBoard)

#Font!
ADB = g.makeFont("adobecleanblack", 12)
BADB = g.makeFont("adobecleanblack", 20)

#Create Rooms
r1 = Room("Startup", simpleBackground)
g.addRoom(r1)

r2 = Room("Game", simpleBackground)
g.addRoom(r2)


#   -
#   GAMEOBJECTCLASSES
#   -

#New Game object
class NG(TextRectangle):
    def update(self):
        self.checkMousePressedOnMe(event)
        if self.mouseHasPressedOnMe == True and event.type == pygame.MOUSEBUTTONUP:

#Makes it white's turn            
            global GAME
            GAME = 1

#Searches and clears the board
            TempList = []
            for y in range (0, 8):
                for x in range(0,8):
                    if GSquares[y][x].piece != None:

                        if (str(GSquares[y][x].piece.sv) == str('BK.png')) or (str(GSquares[y][x].piece.sv) == str('WK.png')):
                            print("king")
                            GSquares[y][x].piece.K = False                          
                        
                        GSquares[y][x].piece.play=False
                        GSquares[y][x].piece.square = None
                        GSquares[y][x].piece.move(700, 700)
                        GSquares[y][x].piece = None
                        GSquares[y][x].selected=False
                        
                x=0

#Moves any win messages
            BW.rect.x = 700
            BW.rect.y = 700

            WW.rect.x = 700
            WW.rect.y = 700

#Creates the new pieces
            TempList = []
            for y in range (0, 8):
                for x in range(0,8):
                    print(PBoard[y][x])
                    if PBoard[y][x]=='BP.png':
                        tempImg=g.makeSpriteImage(PBoard[y][x])
                        temp=Pawn(tempImg, 80*x, 80*y, 'B', 'BP.png')
                        r2.addObject(temp)
                        temp.add(GSquares[y][x])
                        GSquares[y][x].add(temp)
                    elif PBoard[y][x]=='BR.png':
                        tempImg=g.makeSpriteImage(PBoard[y][x])
                        temp=Rook(tempImg, 80*x, 80*y, 'B', 'BR.png')
                        r2.addObject(temp)
                        temp.add(GSquares[y][x])
                        GSquares[y][x].add(temp)        
                    elif PBoard[y][x]=='BN.png':
                        tempImg=g.makeSpriteImage(PBoard[y][x])
                        temp=Knight(tempImg, 80*x, 80*y, 'B', 'BN.png')
                        r2.addObject(temp)
                        temp.add(GSquares[y][x])
                        GSquares[y][x].add(temp)            
                    elif PBoard[y][x]=='BB.png':
                        tempImg=g.makeSpriteImage(PBoard[y][x])
                        temp=Bishop(tempImg, 80*x, 80*y, 'B', 'BB.png')
                        r2.addObject(temp)
                        temp.add(GSquares[y][x])
                        GSquares[y][x].add(temp)
                    elif PBoard[y][x]=='BQ.png':
                        tempImg=g.makeSpriteImage(PBoard[y][x])
                        temp=Queen(tempImg, 80*x, 80*y, 'B', 'BQ.png')
                        r2.addObject(temp)
                        temp.add(GSquares[y][x])
                        GSquares[y][x].add(temp)
                    elif PBoard[y][x]=='BK.png':
                        tempImg=g.makeSpriteImage(PBoard[y][x])
                        temp=King(tempImg, 80*x, 80*y, 'B', 'BK.png')
                        r2.addObject(temp)
                        temp.add(GSquares[y][x])
                        GSquares[y][x].add(temp)
                        
                    elif PBoard[y][x]=='WP.png':
                        tempImg=g.makeSpriteImage(PBoard[y][x])
                        temp=Pawn(tempImg, 80*x, 80*y, 'W', 'WP.png')
                        r2.addObject(temp)
                        temp.add(GSquares[y][x])
                        GSquares[y][x].add(temp)
                    elif PBoard[y][x]=='WR.png':
                        tempImg=g.makeSpriteImage(PBoard[y][x])
                        temp=Rook(tempImg, 80*x, 80*y, 'W', 'WR.png')
                        r2.addObject(temp)
                        temp.add(GSquares[y][x])
                        GSquares[y][x].add(temp)
                    elif PBoard[y][x]=='WN.png':
                        tempImg=g.makeSpriteImage(PBoard[y][x])
                        temp=Knight(tempImg, 80*x, 80*y, 'W', 'WN.png')
                        r2.addObject(temp)
                        temp.add(GSquares[y][x])
                        GSquares[y][x].add(temp)
                    elif PBoard[y][x]=='WB.png':
                        tempImg=g.makeSpriteImage(PBoard[y][x])
                        temp=Bishop(tempImg, 80*x, 80*y, 'W', 'WB.png')
                        r2.addObject(temp)
                        temp.add(GSquares[y][x])
                        GSquares[y][x].add(temp)
                    elif PBoard[y][x]=='WQ.png':
                        tempImg=g.makeSpriteImage(PBoard[y][x])
                        temp=Queen(tempImg, 80*x, 80*y, 'W', 'WQ.png')
                        r2.addObject(temp)
                        temp.add(GSquares[y][x])
                        GSquares[y][x].add(temp)
                    elif PBoard[y][x]=='WK.png':
                        tempImg=g.makeSpriteImage(PBoard[y][x])
                        temp=King(tempImg, 80*x, 80*y, 'W', 'WK.png')
                        r2.addObject(temp)
                        temp.add(GSquares[y][x])
                        GSquares[y][x].add(temp)
                    
                    GSquares.append(tempList)
                x=0

#Moves to the game room if on a different one.                
            g.goToRoom(1)
            self.mouseHasPressedOnMe = False

#Loading Game button
class LG(TextRectangle):
    def update(self):
        self.checkMousePressedOnMe(event)
        if self.mouseHasPressedOnMe == True and event.type == pygame.MOUSEBUTTONUP:

#If there is a savefile, loads the game.
            if LBoard != []:
                TempList = []
                for y in range (0, 8):
                    for x in range(0,8):
                        print(LBoard[y][x])
                        if LBoard[y][x]=='BP.png':
                            tempImg=g.makeSpriteImage(LBoard[y][x])
                            temp=Pawn(tempImg, 80*x, 80*y, 'B', 'BP.png')
                            r2.addObject(temp)
                            temp.add(GSquares[y][x])
                            GSquares[y][x].add(temp)
                        elif LBoard[y][x]=='BR.png':
                            tempImg=g.makeSpriteImage(LBoard[y][x])
                            temp=Rook(tempImg, 80*x, 80*y, 'B', 'BR.png')
                            r2.addObject(temp)
                            temp.add(GSquares[y][x])
                            GSquares[y][x].add(temp)        
                        elif LBoard[y][x]=='BN.png':
                            tempImg=g.makeSpriteImage(LBoard[y][x])
                            temp=Knight(tempImg, 80*x, 80*y, 'B', 'BN.png')
                            r2.addObject(temp)
                            temp.add(GSquares[y][x])
                            GSquares[y][x].add(temp)            
                        elif LBoard[y][x]=='BB.png':
                            tempImg=g.makeSpriteImage(LBoard[y][x])
                            temp=Bishop(tempImg, 80*x, 80*y, 'B', 'BB.png')
                            r2.addObject(temp)
                            temp.add(GSquares[y][x])
                            GSquares[y][x].add(temp)
                        elif LBoard[y][x]=='BQ.png':
                            tempImg=g.makeSpriteImage(LBoard[y][x])
                            temp=Queen(tempImg, 80*x, 80*y, 'B', 'BQ.png')
                            r2.addObject(temp)
                            temp.add(GSquares[y][x])
                            GSquares[y][x].add(temp)
                        elif LBoard[y][x]=='BK.png':
                            tempImg=g.makeSpriteImage(LBoard[y][x])
                            temp=King(tempImg, 80*x, 80*y, 'B', 'BK.png')
                            r2.addObject(temp)
                            temp.add(GSquares[y][x])
                            GSquares[y][x].add(temp)
                            
                        elif LBoard[y][x]=='WP.png':
                            tempImg=g.makeSpriteImage(LBoard[y][x])
                            temp=Pawn(tempImg, 80*x, 80*y, 'W', 'WP.png')
                            r2.addObject(temp)
                            temp.add(GSquares[y][x])
                            GSquares[y][x].add(temp)
                        elif LBoard[y][x]=='WR.png':
                            tempImg=g.makeSpriteImage(LBoard[y][x])
                            temp=Rook(tempImg, 80*x, 80*y, 'W', 'WR.png')
                            r2.addObject(temp)
                            temp.add(GSquares[y][x])
                            GSquares[y][x].add(temp)
                        elif LBoard[y][x]=='WN.png':
                            tempImg=g.makeSpriteImage(LBoard[y][x])
                            temp=Knight(tempImg, 80*x, 80*y, 'W', 'WN.png')
                            r2.addObject(temp)
                            temp.add(GSquares[y][x])
                            GSquares[y][x].add(temp)
                        elif LBoard[y][x]=='WB.png':
                            tempImg=g.makeSpriteImage(LBoard[y][x])
                            temp=Bishop(tempImg, 80*x, 80*y, 'W', 'WB.png')
                            r2.addObject(temp)
                            temp.add(GSquares[y][x])
                            GSquares[y][x].add(temp)
                        elif LBoard[y][x]=='WQ.png':
                            tempImg=g.makeSpriteImage(LBoard[y][x])
                            temp=Queen(tempImg, 80*x, 80*y, 'W', 'WQ.png')
                            r2.addObject(temp)
                            temp.add(GSquares[y][x])
                            GSquares[y][x].add(temp)
                        elif LBoard[y][x]=='WK.png':
                            tempImg=g.makeSpriteImage(LBoard[y][x])
                            temp=King(tempImg, 80*x, 80*y, 'W', 'WK.png')
                            r2.addObject(temp)
                            temp.add(GSquares[y][x])
                            GSquares[y][x].add(temp)
                        
                        GSquares.append(tempList)
                    x=0

#Finds which player's turn
                Temp1=file.readline().rstrip("\n")
                global GAME
                GAME=int(Temp1)
                    
                g.goToRoom(1)
                
            self.mouseHasPressedOnMe = False

#image object for background
class Img(GameObject):
    def __init__(self, picture, x, y):
        GameObject.__init__(self, picture)
        
        self.rect.x = x
        self.rect.y = y

#Piece Object
class Piece(GameObject):
    def __init__(self, picture, x, y, colour, sv):
        GameObject.__init__(self, picture)

        self.picture = picture
        self.colour = colour
        self.sv = sv

        self.x=x
        self.y=y
        
        self.rect.x = x
        self.rect.y = y

        self.play = True

        self.square = None

    def add(self, square):
        self.square = square
        
    def move(self, x, y):
        self.rect.x = x
        self.rect.y =y

    def update(self):
        if self.play == True:
            self.checkMousePressedOnMe(event)    
            if self.mouseHasPressedOnMe == True and event.type == pygame.MOUSEBUTTONUP:
                self.y = self.rect.y
                self.x = self.rect.x

#ensures all tiles are deselected
                for y in range(0,8):
                    for x in range(0,8):
                         GSquares[y][x].selected=False
                    x=0

#Only scans if it is that player's turn
                global GAME
                
                if GAME == 1 and self.colour == 'W':
                    self.scan()
                elif GAME == -1 and self.colour == 'B':
                    self.scan()
                self.mouseHasPressedOnMe = False

class Pawn(Piece):
    def scan(self):
        global CLICKED
        CLICKED=self
        print(CLICKED)

        print(self.y/80, self.x/80)
        
        if self.colour == 'W':
            if int((self.y-80)/80)>=0 and (GSquares[int((self.y-80)/80)][int((self.x)/80)]).piece==None:
                GSquares[int((self.y-80)/80)][int((self.x)/80)].select()
                    
            if int((self.y-80)/80)>=0 and int((self.x+80)/80)<=7 and (GSquares[int((self.y-80)/80)][int((self.x+80)/80)]).piece != None and (GSquares[int((self.y-80)/80)][int((self.x+80)/80)]).piece.colour == 'B':
                GSquares[int((self.y-80)/80)][int((self.x+80)/80)].select()
                    
            if int((self.y-80)/80)>=0 and int((self.x-80)/80)>=0 and (GSquares[int((self.y-80)/80)][int((self.x-80)/80)]).piece != None and (GSquares[int((self.y-80)/80)][int((self.x-80)/80)]).piece.colour == 'B':
                GSquares[int((self.y-80)/80)][int((self.x-80)/80)].select()

            if (int(self.y/80))==6 and (GSquares[int((self.y-80)/80)][int((self.x)/80)]).piece==None and (GSquares[int((self.y-160)/80)][int((self.x)/80)]).piece==None:
                GSquares[int((self.y-160)/80)][int(self.x/80)].select()
 
            
        elif self.colour == 'B':
            if int((self.y+80)/80)<=7 and (GSquares[int((self.y+80)/80)][int((self.x)/80)]).piece==None:                
                GSquares[int((self.y+80)/80)][int((self.x)/80)].select()

            if int((self.y+80)/80)<=7 and int((self.x+80)/80)<=7 and (GSquares[int((self.y+80)/80)][int((self.x+80)/80)]).piece != None and (GSquares[int((self.y+80)/80)][int((self.x+80)/80)]).piece.colour == 'W':                    
                GSquares[int((self.y+80)/80)][int((self.x+80)/80)].select()

            if int((self.y+80)/80)<=7 and int((self.x-80)/80)>=0 and (GSquares[int((self.y+80)/80)][int((self.x-80)/80)]).piece != None and (GSquares[int((self.y+80)/80)][int((self.x-80)/80)]).piece.colour == 'W':                    
                GSquares[int((self.y+80)/80)][int((self.x-80)/80)].select()

            if (int(self.y/80))==1 and (GSquares[int((self.y+80)/80)][int((self.x)/80)]).piece==None and (GSquares[int((self.y+160)/80)][int((self.x)/80)]).piece==None:
                GSquares[int((self.y+160)/80)][int(self.x/80)].select()

    def update(self):        
        if self.colour == 'W':
            if int((self.y)/80)==0:
                self.move(700, 700)
                self.play = False                    
                self.square = None
                temp=Queen(g.makeSpriteImage('WQ.png'), self.x, self.y, 'W', 'WQ.png')
                r2.addObject(temp)
                temp.add(GSquares[int(self.y/80)][int(self.x/80)])
                (GSquares[int(self.y/80)][int(self.x/80)]).add(temp)
                self.y=700

        elif self.colour == 'B':
            if int((self.y)/80)==7:
                self.move(700, 700)
                self.play = False                    
                self.square = None
                temp=Queen(g.makeSpriteImage('BQ.png'), self.x, self.y, 'B', 'BQ.png')
                r2.addObject(temp)
                temp.add(GSquares[int(self.y/80)][int(self.x/80)])
                (GSquares[int(self.y/80)][int(self.x/80)]).add(temp)
                self.y=700                

                    
        if self.play == True:
            self.checkMousePressedOnMe(event)    
            if self.mouseHasPressedOnMe == True and event.type == pygame.MOUSEBUTTONUP:
                self.y = self.rect.y
                self.x = self.rect.x

                for y in range(0,8):
                    for x in range(0,8):
                         GSquares[y][x].selected=False
                    x=0

                global GAME
                
                if GAME == 1 and self.colour == 'W':
                    self.scan()
                elif GAME == -1 and self.colour == 'B':
                    self.scan()
                self.mouseHasPressedOnMe = False
            

class Knight(Piece):
    def scan(self):
        global CLICKED
        CLICKED=self
        print(CLICKED)

        print(self.y/80, self.x/80)

        def search(c):
            if int((self.y+160)/80)<=7 and int((self.x+80)/80)<=7 and (GSquares[int((self.y+160)/80)][int((self.x+80)/80)].piece == None or GSquares[int((self.y+160)/80)][int((self.x+80)/80)].piece.colour == c):
                GSquares[int((self.y+160)/80)][int((self.x+80)/80)].select()
                
            if int((self.y+160)/80)<=7 and int((self.x-80)/80)>=0 and (GSquares[int((self.y+160)/80)][int((self.x-80)/80)].piece == None or GSquares[int((self.y+160)/80)][int((self.x-80)/80)].piece.colour == c):
                GSquares[int((self.y+160)/80)][int((self.x-80)/80)].select()

            if int((self.y-160)/80)>=0 and int((self.x+80)/80)<=7 and (GSquares[int((self.y-160)/80)][int((self.x+80)/80)].piece == None or GSquares[int((self.y-160)/80)][int((self.x+80)/80)].piece.colour == c):                
                GSquares[int((self.y-160)/80)][int((self.x+80)/80)].select()

            if int((self.y-160)/80)>=0 and int((self.x-80)/80)>=0 and (GSquares[int((self.y-160)/80)][int((self.x-80)/80)].piece == None or GSquares[int((self.y-160)/80)][int((self.x-80)/80)].piece.colour == c):            
                GSquares[int((self.y-160)/80)][int((self.x-80)/80)].select()

            if int((self.y+80)/80)<=7 and int((self.x+160)/80)<=7 and (GSquares[int((self.y+80)/80)][int((self.x+160)/80)].piece == None or GSquares[int((self.y+80)/80)][int((self.x+160)/80)].piece.colour == c):            
                GSquares[int((self.y+80)/80)][int((self.x+160)/80)].select()

            if int((self.y+80)/80)<=7 and int((self.x-160)/80)>=0 and (GSquares[int((self.y+80)/80)][int((self.x-160)/80)].piece == None or GSquares[int((self.y+80)/80)][int((self.x-160)/80)].piece.colour == c):               
                GSquares[int((self.y+80)/80)][int((self.x-160)/80)].select()

            if int((self.y-80)/80)>=0 and int((self.x+160)/80)<=7 and (GSquares[int((self.y-80)/80)][int((self.x+160)/80)].piece == None or GSquares[int((self.y-80)/80)][int((self.x+160)/80)].piece.colour == c):               
                GSquares[int((self.y-80)/80)][int((self.x+160)/80)].select()

            if int((self.y-80)/80)>=0 and int((self.x-160)/80)>=0 and (GSquares[int((self.y-80)/80)][int((self.x-160)/80)].piece == None or GSquares[int((self.y-80)/80)][int((self.x-160)/80)].piece.colour == c):               
                GSquares[int((self.y-80)/80)][int((self.x-160)/80)].select()
        
        if self.colour == 'W':
            search('B')
            
            
        elif self.colour == 'B':
            search('W')

class Bishop(Piece):
    def scan(self):
        global CLICKED
        CLICKED=self
        print(CLICKED)

        print(self.y/80, self.x/80)

        def search(c):
            for i in range(1,8):
                if int((self.y+i*80)/80)<=7 and int((self.x+i*80)/80)<=7 and (GSquares[int((self.y+i*80)/80)][int((self.x+i*80)/80)].piece == None or GSquares[int((self.y+i*80)/80)][int((self.x+i*80)/80)].piece.colour == c):
                    GSquares[int((self.y+i*80)/80)][int((self.x+i*80)/80)].select()

                    if GSquares[int((self.y+i*80)/80)][int((self.x+i*80)/80)].piece != None:
                        break
                else:
                    break

            for i in range(1,8):
                if int((self.y+i*80)/80)<=7 and int((self.x-i*80)/80)>=0 and (GSquares[int((self.y+i*80)/80)][int((self.x-i*80)/80)].piece == None or GSquares[int((self.y+i*80)/80)][int((self.x-i*80)/80)].piece.colour == c):                
                    GSquares[int((self.y+i*80)/80)][int((self.x-i*80)/80)].select()

                    if GSquares[int((self.y+i*80)/80)][int((self.x-i*80)/80)].piece != None:
                        break                    
                else:
                    break

            for i in range(1,8):
                if int((self.y-i*80)/80)>=0 and int((self.x+i*80)/80)<=7 and (GSquares[int((self.y-i*80)/80)][int((self.x+i*80)/80)].piece == None or GSquares[int((self.y-i*80)/80)][int((self.x+i*80)/80)].piece.colour == c):                
                    GSquares[int((self.y-i*80)/80)][int((self.x+i*80)/80)].select()

                    if GSquares[int((self.y-i*80)/80)][int((self.x+i*80)/80)].piece != None:
                        break                    
                else:
                    break

            for i in range(1,8):
                if int((self.y-i*80)/80)>=0 and int((self.x-i*80)/80)>=0 and (GSquares[int((self.y-i*80)/80)][int((self.x-i*80)/80)].piece == None or GSquares[int((self.y-i*80)/80)][int((self.x-i*80)/80)].piece.colour == c):                
                    GSquares[int((self.y-i*80)/80)][int((self.x-i*80)/80)].select()

                    if GSquares[int((self.y-i*80)/80)][int((self.x-i*80)/80)].piece != None:
                        break                    
                else:
                    break
        
        if self.colour == 'W':
            search('B')
        elif self.colour == 'B':
            search('W')

class Rook(Piece):
    def scan(self):
        global CLICKED
        CLICKED=self
        print(CLICKED)

        print(self.y/80, self.x/80)

        def search(c):
            for i in range(1,8):
                if int((self.y+i*80)/80)<=7 and (GSquares[int((self.y+i*80)/80)][int(self.x/80)].piece == None or GSquares[int((self.y+i*80)/80)][int(self.x/80)].piece.colour == c):
                    GSquares[int((self.y+i*80)/80)][int(self.x/80)].select()

                    if GSquares[int((self.y+i*80)/80)][int(self.x/80)].piece != None:
                        break
                else:
                    break
                
            for i in range(1,8):
                if int((self.y-i*80)/80)>=0 and (GSquares[int((self.y-i*80)/80)][int(self.x/80)].piece == None or GSquares[int((self.y-i*80)/80)][int(self.x/80)].piece.colour == c):
                    GSquares[int((self.y-i*80)/80)][int(self.x/80)].select()

                    if GSquares[int((self.y-i*80)/80)][int(self.x/80)].piece != None:
                        break
                else:
                    break

            for i in range(1,8):
                if int((self.x+i*80)/80)<=7 and (GSquares[int((self.y)/80)][int((self.x+i*80)/80)].piece == None or GSquares[int((self.y)/80)][int((self.x+i*80)/80)].piece.colour == c):
                    GSquares[int((self.y)/80)][int((self.x+i*80)/80)].select()

                    if GSquares[int((self.y)/80)][int((self.x+i*80)/80)].piece != None:
                        break
                else:
                    break

            for i in range(1,8):
                if int((self.x-i*80)/80)>=0 and (GSquares[int((self.y)/80)][int((self.x-i*80)/80)].piece == None or GSquares[int((self.y)/80)][int((self.x-i*80)/80)].piece.colour == c):
                    GSquares[int((self.y)/80)][int((self.x-i*80)/80)].select()

                    if GSquares[int((self.y)/80)][int((self.x-i*80)/80)].piece != None:
                        break
                else:
                    break 
        
        if self.colour == 'W':
            search('B')                     
        elif self.colour == 'B':
            search('W')

class Queen(Piece):
    def scan(self):
        global CLICKED
        CLICKED=self
        print(CLICKED)

        print(self.y/80, self.x/80)

        def search(c):
            for i in range(1,8):
                if int((self.y+i*80)/80)<=7 and (GSquares[int((self.y+i*80)/80)][int(self.x/80)].piece == None or GSquares[int((self.y+i*80)/80)][int(self.x/80)].piece.colour == c):
                    GSquares[int((self.y+i*80)/80)][int(self.x/80)].select()

                    if GSquares[int((self.y+i*80)/80)][int(self.x/80)].piece != None:
                        break
                else:
                    break
                
            for i in range(1,8):
                if int((self.y-i*80)/80)>=0 and (GSquares[int((self.y-i*80)/80)][int(self.x/80)].piece == None or GSquares[int((self.y-i*80)/80)][int(self.x/80)].piece.colour == c):
                    GSquares[int((self.y-i*80)/80)][int(self.x/80)].select()

                    if GSquares[int((self.y-i*80)/80)][int(self.x/80)].piece != None:
                        break
                else:
                    break

            for i in range(1,8):
                if int((self.x+i*80)/80)<=7 and (GSquares[int((self.y)/80)][int((self.x+i*80)/80)].piece == None or GSquares[int((self.y)/80)][int((self.x+i*80)/80)].piece.colour == c):
                    GSquares[int((self.y)/80)][int((self.x+i*80)/80)].select()

                    if GSquares[int((self.y)/80)][int((self.x+i*80)/80)].piece != None:
                        break
                else:
                    break

            for i in range(1,8):
                if int((self.x-i*80)/80)>=0 and (GSquares[int((self.y)/80)][int((self.x-i*80)/80)].piece == None or GSquares[int((self.y)/80)][int((self.x-i*80)/80)].piece.colour == c):
                    GSquares[int((self.y)/80)][int((self.x-i*80)/80)].select()

                    if GSquares[int((self.y)/80)][int((self.x-i*80)/80)].piece != None:
                        break
                else:
                    break

            for i in range(1,8):
                if int((self.y+i*80)/80)<=7 and int((self.x+i*80)/80)<=7 and (GSquares[int((self.y+i*80)/80)][int((self.x+i*80)/80)].piece == None or GSquares[int((self.y+i*80)/80)][int((self.x+i*80)/80)].piece.colour == c):
                    GSquares[int((self.y+i*80)/80)][int((self.x+i*80)/80)].select()

                    if GSquares[int((self.y+i*80)/80)][int((self.x+i*80)/80)].piece != None:
                        break
                else:
                    break

            for i in range(1,8):
                if int((self.y+i*80)/80)<=7 and int((self.x-i*80)/80)>=0 and (GSquares[int((self.y+i*80)/80)][int((self.x-i*80)/80)].piece == None or GSquares[int((self.y+i*80)/80)][int((self.x-i*80)/80)].piece.colour == c):                
                    GSquares[int((self.y+i*80)/80)][int((self.x-i*80)/80)].select()

                    if GSquares[int((self.y+i*80)/80)][int((self.x-i*80)/80)].piece != None:
                        break                    
                else:
                    break

            for i in range(1,8):
                if int((self.y-i*80)/80)>=0 and int((self.x+i*80)/80)<=7 and (GSquares[int((self.y-i*80)/80)][int((self.x+i*80)/80)].piece == None or GSquares[int((self.y-i*80)/80)][int((self.x+i*80)/80)].piece.colour == c):                
                    GSquares[int((self.y-i*80)/80)][int((self.x+i*80)/80)].select()

                    if GSquares[int((self.y-i*80)/80)][int((self.x+i*80)/80)].piece != None:
                        break                    
                else:
                    break

            for i in range(1,8):
                if int((self.y-i*80)/80)>=0 and int((self.x-i*80)/80)>=0 and (GSquares[int((self.y-i*80)/80)][int((self.x-i*80)/80)].piece == None or GSquares[int((self.y-i*80)/80)][int((self.x-i*80)/80)].piece.colour == c):                
                    GSquares[int((self.y-i*80)/80)][int((self.x-i*80)/80)].select()

                    if GSquares[int((self.y-i*80)/80)][int((self.x-i*80)/80)].piece != None:
                        break                    
                else:
                    break 
        
        if self.colour == 'W':
            search('B')               

        
        elif self.colour == 'B':
            search('W')

class King(Piece):
    def __init__(self, picture, x, y, colour, sv):
        Piece.__init__(self, picture, x, y, colour, sv)
        self.K=True
                
    def scan(self):
        global CLICKED
        CLICKED=self
        print(CLICKED)

        print(self.y/80, self.x/80)

        def search(c):
            if int((self.y+80)/80)<=7 and (GSquares[int((self.y+80)/80)][int(self.x/80)].piece == None or GSquares[int((self.y+80)/80)][int(self.x/80)].piece.colour == c):
                GSquares[int((self.y+80)/80)][int(self.x/80)].select()

            if int((self.y+80)/80)<=7 and int((self.x+80)/80)<=7 and (GSquares[int((self.y+80)/80)][int((self.x+80)/80)].piece == None or GSquares[int((self.y+80)/80)][int((self.x+80)/80)].piece.colour == c):
                GSquares[int((self.y+80)/80)][int((self.x+80)/80)].select()

            if int((self.y+80)/80)<=7 and int((self.x-80)/80)>=0 and (GSquares[int((self.y+80)/80)][int((self.x-80)/80)].piece == None or GSquares[int((self.y+80)/80)][int((self.x-80)/80)].piece.colour == c):
                GSquares[int((self.y+80)/80)][int((self.x-80)/80)].select()

            if int((self.y-80)/80)>=0 and (GSquares[int((self.y-80)/80)][int(self.x/80)].piece == None or GSquares[int((self.y-80)/80)][int(self.x/80)].piece.colour == c):
                GSquares[int((self.y-80)/80)][int((self.x)/80)].select()

            if int((self.y-80)/80)>=0 and int((self.x+80)/80)<=7 and (GSquares[int((self.y-80)/80)][int((self.x+80)/80)].piece == None or GSquares[int((self.y-80)/80)][int((self.x+80)/80)].piece.colour == c):
                GSquares[int((self.y-80)/80)][int((self.x+80)/80)].select()

            if int((self.y-80)/80)>=0 and int((self.x-80)/80)>=0 and (GSquares[int((self.y-80)/80)][int((self.x-80)/80)].piece == None or GSquares[int((self.y-80)/80)][int((self.x-80)/80)].piece.colour == c):
                GSquares[int((self.y-80)/80)][int((self.x-80)/80)].select()

            if int((self.x+80)/80)<=7 and (GSquares[int((self.y)/80)][int((self.x+80)/80)].piece == None or GSquares[int((self.y)/80)][int((self.x+80)/80)].piece.colour == c):
                GSquares[int((self.y)/80)][int((self.x+80)/80)].select()

            if int((self.x-80)/80)>=0 and (GSquares[int((self.y)/80)][int((self.x-80)/80)].piece == None or GSquares[int((self.y)/80)][int((self.x-80)/80)].piece.colour == c):
                GSquares[int((self.y)/80)][int((self.x-80)/80)].select()
                
        if self.colour == 'W':
            search('B')

                
        elif self.colour == 'B':
            search('W')

    def update(self):
        if self.play == True:
            self.checkMousePressedOnMe(event)    
            if self.mouseHasPressedOnMe == True and event.type == pygame.MOUSEBUTTONUP:
                self.y = self.rect.y
                self.x = self.rect.x

                for y in range(0,8):
                    for x in range(0,8):
                         GSquares[y][x].selected=False
                    x=0

                global GAME
                
                if GAME == 1 and self.colour == 'W':
                    self.scan()
                elif GAME == -1 and self.colour == 'B':
                    self.scan()
                self.mouseHasPressedOnMe = False

        elif self.play == False:
            if self.K == True:
                if self.colour == 'W':
                    BW.rect.x = 240
                    BW.rect.y = 280
                    self.K=False
                elif self.colour == 'B':
                    WW.rect.x = 240
                    WW.rect.y = 280
                    self.K = False
                    
                TempList = []
                for y in range (0, 8):
                    for x in range(0,8):
                        if GSquares[y][x].piece != None:
                            
                            if GSquares[y][x].piece.sv == 'BK.png':
                                GSquares[y][x].piece.K = False
                            if GSquares[y][x].piece.sv == 'WK.png':
                                GSquares[y][x].piece.K = False
                                
                            GSquares[y][x].piece.play=False
                
#GameBoard Object
class GameSquare(GameObject):
    def __init__(self, picture, x, y, n):
        GameObject.__init__(self, picture)
        self.x=x
        self.y=y

        self.n=n
        
        self.rect.x = x
        self.rect.y = y
        self.selected=False

        self.piece = None

#selects the square and adds the highlight
    def select(self):
        self.selected=True

        if self.n == 1:
            self.image=BOARD1S
        elif self.n == 2:
            self.image=BOARD2S

    def add(self, piece):
        self.piece = piece

    def rem(self):
        self.piece = None

    def update(self):
#Removes the highlight if there is no piece selected or if the squares is not selected
        global CLICKED
        
        if CLICKED == None:
            self.selected=False

        if self.selected==False:
            if self.n == 1:
                self.image=BOARD1
            elif self.n == 2:
                self.image=BOARD2        

            
        self.checkMousePressedOnMe(event)    
        if self.mouseHasPressedOnMe == True and event.type == pygame.MOUSEBUTTONUP:
            if CLICKED == None:
                pass
#Moves the piece to the position
            elif self.selected==True:
                CLICKED.rect.x = self.x
                CLICKED.rect.y = self.y

#Resetting variables of where the piece exists.
                if self.piece != None:
                    self.piece.square = None
                    self.piece.play= False
                    self.piece.move(700, 700)
                    
                CLICKED.square.piece = None
                CLICKED.add(self)
                self.add(CLICKED)

                global GAME
                GAME *= -1
                
                CLICKED = None
            else:
                CLICKED = None
            self.mouseHasPressedOnMe = False


#   -
#   ADDINGGAMEOBJECTS
#   -

#MAIN GAME OBJECTS            

#GAME ROOM OBJECTS

#Creating the game board
GSquares = []
c=(-1)
for y in range (0, 8):
    tempList=[]

    TESTLIST = []
    
    c*=(-1)
    for x in range(0,4):
        if c>0:
            tempList.append(GameSquare(BOARD1, (160*x), (80*y), 1))
            r2.addObject(tempList[2*x])
            tempList.append(GameSquare(BOARD2, (160*x+80), (80*y), 2))
            r2.addObject(tempList[2*x+1])
        else:
            tempList.append(GameSquare(BOARD2, (160*x), (80*y), 2))
            r2.addObject(tempList[2*x])
            tempList.append(GameSquare(BOARD1, (160*x+80), (80*y), 1))
            r2.addObject(tempList[2*x+1])
    GSquares.append(tempList)
    x=0

#STARTUP ROOM OBJECTS
Title = Img(START, 0, 0)
NewGame = NG("New Game", 290, 160, ADB, BLACK, 240, 40, WHITE)
LoadGame = LG("Load Game", 290, 220, ADB, BLACK, 240, 40, WHITE)
NewGame1 = NG("New Game", 680, 560, ADB, BLACK, 100, 40, WHITE)

WW = TextRectangle("White Wins!", 700, 700, BADB, BLACK, 160, 80, WHITE)
BW = TextRectangle("Black Wins!", 700, 700, BADB, BLACK, 160, 80, WHITE)
r1.addObject(Title)
r1.addObject(NewGame)
r1.addObject(LoadGame)
r2.addObject(NewGame1)
r2.addObject(BW)
r2.addObject(WW)

#   -
#   GAMECODE
#   -

#Initialize the game
g.start()

#Game Loop
while g.running:

        #Limit the game execution framerate
        dt = g.clock.tick(60)

        #Check for Events
        for event in  pygame.event.get():

                #Quit if user clicks[x]
                if event.type == pygame.QUIT:
                        #Saves the game data to the chosen file.
                        file1=open(path, "w")
                        for y in range (0, 8):
                                for x in range (0, 8):
                                        if GSquares[y][x].piece != None:
                                                file1.write(str(GSquares[y][x].piece.sv))
                                        else:
                                                file1.write(str('.'))
                                        file1.write(" ")
                                        x+=1
                                file1.write("\n")
                                x=0
                                y+=1
                                
                        file1.write(str(GAME))

                        file.close()
                        file1.close()
                        g.stop()

        #Update the gamestate of all the objects
        g.currentRoom().updateObjects()

        #Render the background to the window surface
        g.currentRoom().renderBackground(g)

        #Render the object images to the background
        g.currentRoom().renderObjects(g)

        #Draw everything on the screen
        pygame.display.flip()

pygame.quit()
