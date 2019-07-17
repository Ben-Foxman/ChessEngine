from Pieces.Piece import *

class NullPiece(Piece):
    # Class representing a pawn
    def __init__(self):
        self.color = None
    def toString(self):
        return "-"