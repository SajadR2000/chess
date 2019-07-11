class piece:
    def __init__(self,color, currentx, currenty, x, y):
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



