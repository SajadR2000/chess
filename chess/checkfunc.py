import Piece
import board
def searchpiece(x, y):
    for i in Piece.pieceslist:
        if i.currentx == x and i.currenty == y:
            return i
    return 0


def searchsquare(x, y):
    for i in board.squareslist:
        if i.x == x and i.y == y:
            return i
    return 0
    

def check(color):
    if color == "black":
        cx = Piece.kingb.currentx
        cxx = cx
        cy = Piece.kingb.currenty
        cyy = cy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cx += 1
                cy += 1
                continue
            else:
                checkpiece = searchpiece(cx, cy)
                if cx == cxx + 1 and cy == cyy + 1:
                    if checkpiece.color == "white":
                        if checkpiece.ptype == "pawn" or checkpiece.ptype == "queen" or checkpiece.ptype == "bishop":
                            print("black is checked!")
                            return 0
                        else:
                            cx += 1
                            cy += 1
                    else:
                        break
                else:
                    if checkpiece.color == "white":
                        if checkpiece.ptype == "queen" or checkpiece.ptype == "bishop":
                            print("black is checked!")
                            return 0
                        else:
                            cx += 1
                            cy += 1
                    else:
                        break
        cx = cxx
        cy =cyy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cx -= 1
                cy += 1
                continue
            else:
                checkpiece = searchpiece(cx, cy)
                if cx == cxx - 1 and cy == cyy + 1:
                    if checkpiece.color == "white":
                        if checkpiece.ptype == "pawn" or checkpiece.ptype == "queen" or checkpiece.ptype == "bishop":
                            print("black is checked!")
                            return 0
                        else:
                            cx -= 1
                            cy += 1
                    else:
                        break
                else:
                    if checkpiece.color == "white":
                        if checkpiece.ptype == "queen" or checkpiece.ptype == "bishop":
                            print("black is checked!")
                            return 0
                        else:
                            cx -= 1
                            cy += 1
                    else:
                        break
        cx = cxx
        cy = cyy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cx -= 1
                cy -= 1
                continue
            else:
                checkpiece = searchpiece(cx, cy)
                if checkpiece.color == "white":
                    if checkpiece.ptype == "queen" or checkpiece.ptype == "bishop":
                        print("black is checked!")
                        return 0
                    else:
                        cx -= 1
                        cy -= 1
                else:
                    break
        cx = cxx
        cy = cyy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cx += 1
                cy -= 1
                continue
            else:
                checkpiece = searchpiece(cx, cy)
                if checkpiece.color == "white":
                    if checkpiece.ptype == "queen" or checkpiece.ptype == "bishop":
                        print("black is checked!")
                        return 0
                    else:
                        cx += 1
                        cy -= 1
                else:
                    break
        cx = cxx
        cy = cyy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cy -= 1
                continue
            else:
                checkpiece = searchpiece(cx, cy)
                if checkpiece.color == "white":
                    if checkpiece.ptype == "queen" or checkpiece.ptype == "rook":
                        print("black is checked")
                        return 0
                    else:
                        cy -= 1
                else:
                    break
        cx = cxx
        cy = cyy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cy += 1
                continue
            else: 
                checkpiece = searchpiece(cx, cy)
                if checkpiece.color == "white":
                    if checkpiece.ptype == "queen" or checkpiece.ptype == "rook":
                        print("black is checked")
                        return 0
                    else:
                        cy += 1
                else:
                    break
        cx = cxx
        cy = cyy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cx -= 1
                continue
            else:
                checkpiece = searchpiece(cx, cy)
                if checkpiece.color == "white":
                    if checkpiece.ptype == "queen" or checkpiece.ptype == "rook":
                        print("black is checked")
                        return 0
                    else:
                        cx -= 1
                else:
                    break
        cx = cxx
        cy = cyy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cx += 1
                continue
            else:
                checkpiece = searchpiece(cx, cy)
                if checkpiece.color == "white":
                    if checkpiece.ptype == "queen" or checkpiece.ptype == "rook":
                        print("black is checked")
                        return 0
                    else:
                        cx += 1
                else:
                    break
        return 1
    elif color == "white":
        cx = Piece.kingw.currentx
        cxx = cx
        cy = Piece.kingw.currenty
        cyy = cy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cx -= 1
                cy -= 1
                continue
            else:
                checkpiece = searchpiece(cx, cy)
                if cx == cxx - 1 and cy == cyy - 1:
                    if checkpiece.color == "black":
                        if checkpiece.ptype == "pawn" or checkpiece.ptype == "queen" or checkpiece.ptype == "bishop":
                            print("white is checked!")
                            return 0
                        else:
                            cx -= 1
                            cy -= 1
                    else:
                        break
                else:
                    if checkpiece.color == "black":
                        if checkpiece.ptype == "queen" or checkpiece.ptype == "bishop":
                            print("white is checked!")
                            return 0
                        else:
                            cx -= 1
                            cy -= 1
                    else:
                        break
        cx = cxx
        cy = cyy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cx += 1
                cy -= 1
                continue
            else:
                checkpiece = searchpiece(cx, cy)
                if cx == cxx + 1 and cy == cyy - 1:
                    if checkpiece.color == "black":
                        if checkpiece.ptype == "pawn" or checkpiece.ptype == "queen" or checkpiece.ptype == "bishop":
                            print("white is checked!")
                            return 0
                        else:
                            cx += 1
                            cy -= 1
                    else:
                        break
                else:
                    if checkpiece.color == "black":
                        if checkpiece.ptype == "queen" or checkpiece.ptype == "bishop":
                            print("white is checked!")
                            return 0
                        else:
                            cx += 1
                            cy -= 1
                    else:
                        break
        cx = cxx
        cy = cyy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cx -= 1
                cy += 1
                continue
            else:
                checkpiece = searchpiece(cx, cy)
                if checkpiece.color == "black":
                    if checkpiece.ptype == "queen" or checkpiece.ptype == "bishop":
                        print("white is checked!")
                        return 0
                    else:
                        cx -= 1
                        cy += 1
                else:
                    break
        cx = cxx
        cy = cyy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cx += 1
                cy += 1
                continue
            else:
                checkpiece = searchpiece(cx, cy)
                if checkpiece.color == "black":
                    if checkpiece.ptype == "queen" or checkpiece.ptype == "bishop":
                        print("white is checked!")
                        return 0
                    else:
                        cx += 1
                        cy += 1
                else:
                    break
        cx = cxx
        cy = cyy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cy -= 1
                continue
            else:
                checkpiece = searchpiece(cx, cy)
                if checkpiece.color == "black":
                    if checkpiece.ptype == "queen" or checkpiece.ptype == "rook":
                        print("white is checked")
                        return 0
                    else:
                        cy -= 1
                else:
                    break
        cx = cxx
        cy = cyy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cy += 1
                continue
            else:
                checkpiece = searchpiece(cx, cy)
                if checkpiece.color == "black":
                    if checkpiece.ptype == "queen" or checkpiece.ptype == "rook":
                        print("white is checked")
                        return 0
                    else:
                        cy += 1
                else:
                    break
        cx = cxx
        cy = cyy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cx -= 1
                continue
            else:
                checkpiece = searchpiece(cx, cy)
                if checkpiece.color == "black":
                    if checkpiece.ptype == "queen" or checkpiece.ptype == "rook":
                        print("white is checked")
                        return 0
                    else:
                        cx -= 1
                else:
                    break
        cx = cxx
        cy = cyy
        while 1 <= cx <= 8 and 1 <= cy <= 8:
            if (cyy == cy and cxx == cx)  or (searchsquare(cx, cy).state == "empty"):
                cx += 1
                continue
            else:
                checkpiece = searchpiece(cx, cy)
                if checkpiece.color == "black":
                    if checkpiece.ptype == "queen" or checkpiece.ptype == "rook":
                        print("white is checked")
                        return 0
                    else:
                        cx += 1
                else:
                    break
        return 1

                    
