import Piece
import board
import sys
import Game_Display 
from checkfunc import check
def searchsquare(x, y):
    for i in board.squareslist:
        if i.x == x and i.y == y:
            return i
    return 0
    

def searchpiece(x, y):
    for i in Piece.pieceslist:
        if i.currentx == x and i.currenty == y:
            return i
    return 0


def validmove(piece, dx, dy):
    cx = piece.currentx
    cy = piece.currenty
    fx = piece.currentx + dx
    fy = piece.currenty + dy
    #determines whether the move is in board
    if fx > 8 or fx <= 0 or fy > 8 or fy <= 0:
        print("invalid move:out of range!")
        return 0
    # determines whether anything blocks the movements
    if piece.ptype == "knight":
        return 1
    elif dx == dy and dx < 0:
        cx -= 1
        cy -= 1
        while cx != fx and cy != fy:    
            x = searchsquare(cx, cy)
            if x.state != "empty":
                print("invalid move")
                return 0
            cx -= 1
            cy -= 1
        return 1
    elif dx == dy and dx > 0:
        cx += 1
        cy += 1
        while cx != fx and cy != fy:    
            x = searchsquare(cx, cy)
            if x.state != "empty":
                print("invalidmove")
                return 0
            cx += 1
            cy += 1
        return 1
    elif dx == (-1) * dy:
        cx += dx/abs(dx)
        cy += dy/abs(dy)
        while cx != fx and cy != fy:    
            x = searchsquare(cx, cy)
            if x.state != "empty":
                print("invalidmove")
                return 0
            cx += dx/abs(dx)
            cy += dy/abs(dy)
        return 1
    elif dx == 0:
        cy += dy/abs(dy)
        while cy != fy:
            x = searchsquare(cx, cy)
            if x.state != "empty":
                print("invalidmove")
                return 0
            cy += dy/abs(dy)
        return 1
    elif dy == 0:
        cx += dx/abs(dx)
        while cx != fx:
            x= searchsquare(cx, cy)
            if x.state != "empty":
                print("invalidmove")
                return 0
            cx += dx/abs(dx)
        return 1


#determines if the move is particular pawn move:
def pawn_particular_move(piece, dx, dy):
    cx = piece.currentx
    cy = piece.currenty
    fx = piece.currentx + dx
    fy = piece.currenty + dy
    if (searchpiece(cx, cy).color == "white" and searchpiece(cx, cy).ptype == "pawn" and searchsquare(fx, fy).state == "bocc") or (searchpiece(cx, cy).color == "black" and searchpiece(cx, cy).ptype == "pawn" and searchsquare(fx, fy).state == "wocc"):
        return 1
    else:
        return 0


# determines if the player is checked or not.                     #not complete yet.
def checkcheck(piece):
    print(piece.color)
    if check(piece.color) == 0:
        return 0
    return 1


# turnes pawn to something else.
def goodpawn(piece):
    name = input("What do you want to turn your pawn into?")
    piece.ptype = name
    if piece.color == "white":
        if name == "queen":
            piece.pimg = Piece.wqueenimg
        elif name == "rook":
            piece.pimg = Piece.wrook1img
        elif name == "bishop":
            piece.pimg = Piece.wbishop1img
        elif name == "knight":
            piece.pimg = Piece.wknight1img
        else:
            print("invalid input")
            goodpawn(piece)
    else:
        if name == "queen":
            piece.pimg = Piece.bqueenimg
        elif name == "rook":
            piece.pimg = Piece.brook1img
        elif name == "bishop":
            piece.pimg = Piece.bbishop1img
        elif name == "knight":
            piece.pimg = Piece.bknight1img
        else:
            print("invalid input")
            goodpawn(piece)


def Run():
    try:
        curntx = int(input("enter column number: ")) #coordinates of chosen square. 
        curnty = int(input("enter row number: ")) 
        deltax = int(input("enter delta x: "))   #positive deltax equals going right and negetive deltax equals goinig left
        deltay = int(input("enter delta y: "))   #positive deltay equals going down and negetive deltay equals going up 
    except:
        print("Enter a valid number!")
        return 0
    emptysignal = 1 # 0 means bocc or wocc. 1 means empty
    chosenpiece = searchpiece(curntx, curnty)
    chosensquare =  searchsquare(curntx, curnty)
    if chosenpiece == 0:
        print("Piece not found!")
        return False
    if chosensquare == 0:
        print("Wrong choice!")
        return False
    chosenpiece.x = deltax
    chosenpiece.y = deltay
    newchosensquare = searchsquare(chosenpiece.currentx +chosenpiece.x, chosenpiece.currenty +chosenpiece.y)
    print(newchosensquare)
    piecetobedeleted = searchpiece(chosenpiece.currentx +chosenpiece.x, chosenpiece.currenty +chosenpiece.y)
    if piecetobedeleted == 0:
        del piecetobedeleted
    else:
        emptysignal = 0
    move2 = validmove(chosenpiece, deltax, deltay)
    if move2 == 1:
        if pawn_particular_move(chosenpiece, deltax, deltay) == 0:
            move1 = chosenpiece.movement()
        else:
            move1 = chosenpiece.particularpawnmove()
    else:
        move1 = False
    if move1 != False:
        if emptysignal == 1:    
            chosensquare.state = "empty"
            if chosenpiece.color == "black":
                newchosensquare.state = "bocc"
            else:
                newchosensquare.state = "wocc"
        else:
            if (newchosensquare.state == "wocc" and chosenpiece.color == "white") or (newchosensquare.state == "bocc" and chosenpiece.color == "black"):  
                print("Error Enter again1!")
                chosenpiece.x = -1 * deltax
                chosenpiece.y = -1 * deltay
                chosenpiece.movement()
                return False
            elif chosenpiece.color == "black" and newchosensquare.state == "wocc":
                Piece.pieceslist.remove(piecetobedeleted)
                chosensquare.state = "empty"
                newchosensquare.state = "bocc"
            elif chosenpiece.color =="white" and newchosensquare.state == "bocc":
                Piece.pieceslist.remove(piecetobedeleted)
                chosensquare.state = "empty"
                newchosensquare.state = "wocc"
        if chosenpiece.ptype == "pawn" and ((chosenpiece.color == "white" and chosenpiece.currenty == 1) or (chosenpiece.color == "black" and chosenpiece.currenty == 8)):
            goodpawn(chosenpiece)
        else:
            pass
    else:
        if move1 == False:
            print("Error Enter again2!")
        if move2 == 0:
            print("Error Enter again3!")
        return False
    check("white")
    check("black")
while True:
    Run()
    Game_Display.Game_loop()
    
                
