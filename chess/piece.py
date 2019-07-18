import pygame
class piece:
    def __init__(self,color, currentx, currenty, ptype, ntype, pimg, x = 0, y = 0):
        self.color = color
        self.currentx = currentx
        self.currenty = currenty
        self.x = x
        self.y = y
        self.ptype = ptype
        self.ntype = ntype
        self.pimg = pimg
    def movement(self):
        if self.ptype == "king" and ((abs(self.x) == abs(self.y)) or (self.x == 0 and abs(self.y) == 1) or (self.y == 0 and abs(self.x) == 1)):
            self.currentx += self.x
            self.currenty += self.y
            return True
        elif self.ptype == "queen" and ((self.x == 0) or (self.y == 0) or (abs(self.x) == abs(self.y))):
            self.currentx += self.x
            self.currenty += self.y
            return True
        elif self.ptype == "knight" and ((abs(self.x) == 1 and abs(self.y) == 2) or (abs(self.y) == 1 and abs(self.x) == 2)):
            self.currentx += self.x
            self.currenty += self.y
            return True
        elif self.ptype == "rook" and (self.x == 0 or self.y == 0):
            self.currentx += self.x
            self.currenty += self.y
            return True
        elif self.ptype == "bishop" and (abs(self.x) == abs(self.y)):
            self.currentx += self.x
            self.currenty += self.y
            return True
        elif (self.ptype == "pawn") and (self.x == 0) and (((self.y == 1 and self.color == "black") or (self.y == -1 and self.color == "white")) or (abs(self.y) == 2 and ((self.currenty == 2 and self.color == "black") or (self.currenty == 7 and self.color == "white")))):
            self.currentx += self.x
            self.currenty += self.y
            return True
        else:
            return False
    

    def particularpawnmove(self):
        if (self.y > 0 and self.color == "black") or (self.y < 0 and self.color == "white"):
            self.currentx += self.x
            self.currenty += self.y
            return True
        else:
            return False

wrook1img = pygame.image.load('white_rook.png')
wrook2img = pygame.image.load('white_rook.png')
wknight1img = pygame.image.load('white_knight.png')
wknight2img = pygame.image.load('white_knight.png')
wbishop1img = pygame.image.load('white_bishop.png')
wbishop2img = pygame.image.load('white_bishop.png')
wqueenimg = pygame.image.load('white_queen.png')
wkingimg = pygame.image.load('white_king.png')
wpawn1img = pygame.image.load('white_pawn.png')
wpawn2img = pygame.image.load('white_pawn.png')
wpawn3img = pygame.image.load('white_pawn.png')
wpawn4img = pygame.image.load('white_pawn.png')
wpawn5img = pygame.image.load('white_pawn.png')
wpawn6img = pygame.image.load('white_pawn.png')
wpawn7img = pygame.image.load('white_pawn.png')
wpawn8img = pygame.image.load('white_pawn.png')
brook1img = pygame.image.load('black_rook.png')
brook2img = pygame.image.load('black_rook.png')
bknight1img = pygame.image.load('black_knight.png')
bknight2img = pygame.image.load('black_knight.png')
bbishop1img = pygame.image.load('black_bishop.png')
bbishop2img = pygame.image.load('black_bishop.png')
bqueenimg = pygame.image.load('black_queen.png')
bkingimg = pygame.image.load('black_king.png')
bpawn1img = pygame.image.load('black_pawn.png')
bpawn2img = pygame.image.load('black_pawn.png')
bpawn3img = pygame.image.load('black_pawn.png')
bpawn4img = pygame.image.load('black_pawn.png')
bpawn5img = pygame.image.load('black_pawn.png')
bpawn6img = pygame.image.load('black_pawn.png')
bpawn7img = pygame.image.load('black_pawn.png')
bpawn8img = pygame.image.load('black_pawn.png')
kingw =piece("white", 5, 8, "king", "1", wkingimg)
queenw = piece("white", 4, 8, "queen", "1", wqueenimg)
rookw1 = piece("white", 1, 8, "rook", "1", wrook1img)
rookw2 = piece("white", 8, 8, "rook","2", wrook2img)
knightw1 = piece("white", 2, 8, "knight", "1", wknight1img)
knightw2 = piece("white", 7, 8, "knight", "2", wknight2img)
bishopw1 = piece("white", 3, 8, "bishop", "1", wbishop1img)
bishopw2 = piece("white", 6, 8, "bishop", "2", wbishop2img)
pawnw1 = piece("white", 1, 7, "pawn", "1", wpawn1img)
pawnw2 = piece("white", 2, 7, "pawn", "2", wpawn2img)
pawnw3 = piece("white", 3, 7, "pawn", "3", wpawn3img)
pawnw4 = piece("white", 4, 7, "pawn", "4", wpawn4img)
pawnw5 = piece("white", 5, 7, "pawn", "5", wpawn5img)
pawnw6 = piece("white", 6, 7, "pawn", "6", wpawn6img)
pawnw7 = piece("white", 7, 7, "pawn", "7", wpawn7img)
pawnw8 = piece("white", 8, 7, "pawn", "8", wpawn8img)
kingb = piece("black", 5, 1, "king", "1", bkingimg)
queenb = piece("black", 4, 1, "queen", "1", bqueenimg)
rookb1 = piece("black", 1, 1, "rook", "1", brook1img)
rookb2 = piece("black", 8, 1, "rook", "2", brook2img)
knightb1 = piece("black", 2, 1, "knight", "1", bknight1img)
knightb2 = piece("black", 7, 1, "knight", "2", bknight2img)
bishopb1 = piece("black", 3, 1, "bishop", "1", bbishop1img)
bishopb2 = piece("black", 6, 1, "bishop", "2", bbishop2img)
pawnb1 = piece("black", 1, 2, "pawn", "1", bpawn1img)
pawnb2 = piece("black", 2, 2, "pawn", "2", bpawn2img)
pawnb3 = piece("black", 3, 2, "pawn", "3", bpawn3img)
pawnb4 = piece("black", 4, 2, "pawn", "4", bpawn4img)
pawnb5 = piece("black", 5, 2, "pawn", "5", bpawn5img)
pawnb6 = piece("black", 6, 2, "pawn", "6", bpawn6img)
pawnb7 = piece("black", 7, 2, "pawn", "7", bpawn7img)
pawnb8 = piece("black", 8, 2, "pawn", "8", bpawn8img)
pieceslist = [kingw, queenw, rookw1, rookw2, knightw1, knightw2, bishopw1, bishopw2, pawnw1, pawnw2
, pawnw3, pawnw4, pawnw5, pawnw6, pawnw7, pawnw8, kingb, queenb, rookb1, rookb2, knightb1, knightb2
, bishopb1, bishopb2, pawnb1, pawnb2, pawnb3, pawnb4, pawnb5, pawnb6, pawnb7, pawnb8]
boardimg = pygame.image.load('board_alt.png')
#  useless dictionary:
piecesimgs = { "whiterook1" : wrook1img, "whiterook2" : wrook2img, "whiteknight1" : wknight1img, "whiteknight2" : wknight2img
, "wbishop1": wbishop1img, "whitebishop2" : wbishop2img, "whitequeen1" : wqueenimg, "whiteknig1":wkingimg, "whitepawn1" : wpawn1img
, "whitepawn2" : wpawn2img, "whitepawn3" : wpawn3img, "whitepawn4" : wpawn4img, "whitepawn5" : wpawn5img
, "whitepawn6" : wpawn6img, "whitepawn7" : wpawn7img, "whitepawn8" : wpawn8img }
