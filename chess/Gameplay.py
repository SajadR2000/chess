import piece2
import board
while True:
    curntx = int(input("enter current x: ")) #coordinates of chosen square. 2000 means quit
    if curntx == 2000:
        break
    curnty = int(input("enter current y: ")) 
    deltax = int(input("enter delta x: "))   #positive deltax equals going right and negetive deltax equals goinig left
    deltay = int(input("enter delta y: "))   #positive deltay equals going down and negetive deltay equals going up 
    i = 0
    emptysignal = 1 # 0 means bocc or wocc. 1 means empty
    while i < len(piece2.pieceslist):
        if curntx == piece2.pieceslist[i].currentx and curnty == piece2.pieceslist[i].currenty:
            chosenpiece = piece2.pieceslist[i]
            break
        i += 1
    i = 0
    while i < len(board.squareslist):
        if board.squareslist[i].x == curntx and board.squareslist[i].y == curnty:
            chosensquare = board.squareslist[i]
            break
        i += 1
    i = 0
    chosenpiece.x = deltax
    chosenpiece.y = deltay
    while i < len(board.squareslist):
        if board.squareslist[i].x == (chosenpiece.currentx +chosenpiece.x) and board.squareslist[i].y == (chosenpiece.currenty +chosenpiece.y):
            newchosensquare = board.squareslist[i]
            break
        i += 1
    i = 0
    while i < len(piece2.pieceslist):
        if piece2.pieceslist[i].currentx == (chosenpiece.currentx +chosenpiece.x) and piece2.pieceslist[i].currenty == (chosenpiece.currenty +chosenpiece.y):
            piecetobedeleted = piece2.pieceslist[i]
            emptysignal = 0
            break
        i += 1
    if chosenpiece.movement() != False:
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
            elif chosenpiece.color == "black" and newchosensquare.state == "wocc":
                piece2.pieceslist.remove(piecetobedeleted)
                newchosensquare.state = "bocc"
            elif chosenpiece.color =="white" and newchosensquare.state == "bocc":
                piece2.pieceslist.remove(piecetobedeleted)
                newchosensquare.state = "wocc"
    else:
        print("Error Enter again2!")
for i in piece2.pieceslist:
    print(i.ptype)

                