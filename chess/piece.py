class piece:
    def __init__(self,color, currentx, currenty, ptype, x = 0, y = 0):
        self.color = color
        self.currentx = currentx
        self.currenty = currenty
        self.x = x
        self.y = y
        self.ptype = ptype
    def movement(self):
        if self.ptype == "king" and ((abs(self.x) == abs(self.y)) or (self.x == 0 and abs(self.y) == 1) or (self.y == 0 and abs(self.x) == 1)):
            self.currentx += self.x
            self.currenty += self.y
        elif self.ptype == "queen" and ((self.x == 0) or (self.y == 0) or (abs(self.x) == abs(self.y))):
            self.currentx += self.x
            self.currenty += self.y
        elif self.ptype == "knight" and ((abs(self.x) == 1 and abs(self.y) == 2) or (abs(self.y) == 1 and abs(self.x) == 2)):
            self.currentx += self.x
            self.currenty += self.y
        elif self.ptype == "rook" and (self.x == 0 or self.y == 0):
            self.currentx += self.x
            self.currenty += self.y
        elif self.ptype == "bishop" and (abs(self.x) == abs(self.y)):
            self.currentx += self.x
            self.currenty += self.y
        elif (self.ptype == "pawn") and (self.x == 0) and (((self.y == 1 and self.color == "black") or (self.y == -1 and self.color == "white")) or (abs(self.y) == 2 and ((self.currenty == 2 and self.color == "black") or (self.currenty == 7 and self.color == "white")))):
            self.currentx += self.x
            self.currenty += self.y
        else:
            return False


kingw =piece("white", 5, 8, "king" )
queenw = piece("white", 4, 8, "queen")
rookw1 = piece("white", 1, 8, "rook")
rookw2 = piece("white", 8, 8, "rook")
knightw1 = piece("white", 2, 8, "knight")
knightw2 = piece("white", 7, 8, "knight")
bishopw1 = piece("white", 3, 8, "bishop")
bishopw2 = piece("white", 6, 8, "bishop")
pawnw1 = piece("white", 1, 7, "pawn")
pawnw2 = piece("white", 2, 7, "pawn")
pawnw3 = piece("white", 3, 7, "pawn")
pawnw4 = piece("white", 4, 7, "pawn")
pawnw5 = piece("white", 5, 7, "pawn")
pawnw6 = piece("white", 6, 7, "pawn")
pawnw7 = piece("white", 7, 7, "pawn")
pawnw8 = piece("white", 8, 7, "pawn")
kingb = piece("black", 5, 1, "king")
queenb = piece("black", 4, 1, "queen")
rookb1 = piece("black", 1, 1, "rook")
rookb2 = piece("black", 8, 1, "rook")
knightb1 = piece("black", 2, 1, "knight")
knightb2 = piece("black", 7, 1, "knight")
bishopb1 = piece("black", 3, 1, "bishop")
bishopb2 = piece("black", 6, 1, "bishop")
pawnb1 = piece("black", 1, 2, "pawn")
pawnb2 = piece("black", 2, 2, "pawn")
pawnb3 = piece("black", 3, 2, "pawn")
pawnb4 = piece("black", 4, 2, "pawn")
pawnb5 = piece("black", 5, 2, "pawn")
pawnb6 = piece("black", 6, 2, "pawn")
pawnb7 = piece("black", 7, 2, "pawn")
pawnb8 = piece("black", 8, 2, "pawn")
pieceslist = [kingw, kingb, queenb, queenw, rookb1, rookb2, rookw1, rookw2, knightb1, knightb2, knightw1, knightw2
, bishopb1, bishopb2, bishopw1, bishopw2, pawnb1, pawnb2, pawnb3, pawnb4, pawnb5, pawnb6, pawnb7, pawnb8, pawnw1, pawnw2
, pawnw3, pawnw4, pawnw5, pawnw6, pawnw7, pawnw8]
