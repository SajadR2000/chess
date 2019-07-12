class piece:
    def __init__(self,color, currentx, currenty, x = 0, y = 0):
        self.color = color
        self.currentx = currentx
        self.currenty = currenty
        self.x = x
        self.y = y
    def movement(self):
        self.currentx += self.x
        self.currenty += self.y


class king(piece):
    def movecheck(self):
        if (abs(self.x) == abs(self.y)) or (self.x == 0 and abs(self.y) == 1) or (self.y == 0 and abs(self.x) == 1):
            super().movement()


class queen(piece):
    def movecheck(self):
        if (self.x == 0) or (self.y == 0) or (abs(self.x) == abs(self.y)):
            super().movement()


class knight(piece):
    def movecheck(self):
        if (abs(self.x) == 1 and abs(self.y) == 2) or (abs(self.y) == 1 and abs(self.x) == 2):
            super().movement()


class rook(piece):
    def movecheck(self):
        if self.x == 0 or self.y == 0:
            super().movement()


class bishop(piece):
    def movecheck(self):
        if abs(self.x) == abs(self.y):
            super().movement()


class pawn(piece):     
    def movecheck(self):
        if self.x == 0: 
            super().movement()


kingw =king("white", 5, 8 )
queenw = queen("white", 4, 8)
rookw1 = rook("white", 1, 8)
rookw2 = rook("white", 8, 8)
knightw1 = knight("white", 2, 8)
knightw2 = knight("white", 7, 8)
bishopw1 = bishop("white", 3, 8)
bishopw2 = bishop("white", 6, 8)
pawnw1 = pawn("white", 1, 7)
pawnw2 = pawn("white", 2, 7)
pawnw3 = pawn("white", 3, 7)
pawnw4 = pawn("white", 4, 7)
pawnw5 = pawn("white", 5, 7)
pawnw6 = pawn("white", 6, 7)
pawnw7 = pawn("white", 7, 7)
pawnw8 = pawn("white", 8, 7)
kingb = king("black", 5, 1 )
queenb = queen("black", 4, 1)
rookb1 = rook("black", 1, 1)
rookb2 = rook("black", 8, 1)
knightb1 = knight("black", 2, 1)
knightb2 = knight("black", 7, 1)
bishopb1 = bishop("black", 3, 1)
bishopb2 = bishop("black", 6, 1)
pawnb1 = pawn("black", 1, 2)
pawnb2 = pawn("black", 2, 2)
pawnb3 = pawn("black", 3, 2)
pawnb4 = pawn("black", 4, 2)
pawnb5 = pawn("black", 5, 2)
pawnb6 = pawn("black", 6, 2)
pawnb7 = pawn("black", 7, 2)
pawnb8 = pawn("black", 8, 2)
