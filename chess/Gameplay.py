import piece
import board
import sys
def searchsquare(x, y):
    for i in board.squareslist:
        if i.x == x and i.y == y:
            return i
    return 0
    

def searchpiece(x, y):
    for i in piece.pieceslist:
        if i.currentx == x and i.currenty == y:
            return i
    return 0


def validmove(piece, dx, dy):
    cx = piece.currentx
    cy = piece.currenty
    fx = piece.currentx + dx
    fy = piece.currenty + dy
    if cx + dx > 8 or cx + dx <= 0 or cy + dy > 8 or cy + dy <= 0:
        print("invalidmove")
        return 0
    if dx == dy and dx < 0:
        cx -= 1
        cy -= 1
        while cx != fx and cy != fy:    
            x = searchsquare(cx, cy)
            if x.state != "empty":
                print("invalidmove")
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


def Run():
    curntx = int(input("enter column number: ")) #coordinates of chosen square. 
    curnty = int(input("enter row number: ")) 
    deltax = int(input("enter delta x: "))   #positive deltax equals going right and negetive deltax equals goinig left
    deltay = int(input("enter delta y: "))   #positive deltay equals going down and negetive deltay equals going up 
    emptysignal = 1 # 0 means bocc or wocc. 1 means empty
    chosenpiece = searchpiece(curntx, curnty)
    chosensquare =  searchsquare(curntx, curnty)
    if chosenpiece == 0 or chosensquare == 0:
        print("Error!")
        return False
    chosenpiece.x = deltax
    chosenpiece.y = deltay
    newchosensquare = searchsquare(chosenpiece.currentx +chosenpiece.x, chosenpiece.currenty +chosenpiece.y)
    piecetobedeleted = searchpiece(chosenpiece.currentx +chosenpiece.x, chosenpiece.currenty +chosenpiece.y)
    if piecetobedeleted == 0:
        del piecetobedeleted
    else:
        emptysignal = 0
    if chosenpiece.movement() != False and validmove(chosenpiece, deltax, deltay) == 1:
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
                piece.pieceslist.remove(piecetobedeleted)
                newchosensquare.state = "bocc"
            elif chosenpiece.color =="white" and newchosensquare.state == "bocc":
                piece.pieceslist.remove(piecetobedeleted)
                newchosensquare.state = "wocc"
    else:
        print("Error Enter again2!")
        return False

                
