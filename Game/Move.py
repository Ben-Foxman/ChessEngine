from Game.Board import Board
from Pieces.NullPiece import NullPiece
from Game.Tile import Tile
from Pieces.Queen import Queen
from Pieces.Rook import Rook
from Pieces.King import King
import copy
class Move:
    def __init__(self, board, piece, coordinate):
        self.board = board
        self.piece = piece
        self.coordinate = coordinate

    def makeMove(self):
        specialMove = False
        boardCopy = copy.deepcopy(self.board)
        prevPosition = self.piece.position
        boardCopy.tiles[self.piece.position] = Tile(self.piece.position, NullPiece())
        enPassantHold = self.piece.position


        #after first move, castling isn't allowed
        if self.piece.toString().lower() == "k" or self.piece.toString().lower() == "r":
            self.piece.moved = True
        # deal with a queened pawn
        if self.piece.toString().lower() == "p":
            if self.piece.color == "White" and 56 <= self.coordinate < 64:
                boardCopy.tiles[self.coordinate] = Tile(self.coordinate, Queen("White", self.coordinate))
                specialMove = True
            elif self.piece.color == "Black" and 0 <= self.coordinate < 7:
                boardCopy.tiles[self.coordinate] = Tile(self.coordinate, Queen("Black", self.coordinate))
                specialMove = True


        #deal with en passant
        if self.piece.toString().lower() == "p":
            if self.piece.color == "White" and 32 <= enPassantHold < 39:
                if self.coordinate - enPassantHold != 8:
                    if boardCopy.tiles[self.coordinate].pieceOnTile.toString() == "-":
                        boardCopy.tiles[self.coordinate - 8] = Tile(self.coordinate, NullPiece())
                        boardCopy.tiles[self.coordinate] = Tile(self.coordinate, self.piece)
                        specialMove = True
            elif self.piece.color == "Black" and 24 <= enPassantHold < 31:
                if self.coordinate - enPassantHold != -8:
                    if boardCopy.tiles[self.coordinate].pieceOnTile.toString() == "-":
                        boardCopy.tiles[self.coordinate + 8] = Tile(self.coordinate, NullPiece())
                        boardCopy.tiles[self.coordinate] = Tile(self.coordinate, self.piece)
                        specialMove = True


        #deal with castling
        if self.piece.toString() == "k":
            if prevPosition == 4 and self.coordinate == 2:
                boardCopy.tiles[self.coordinate] = Tile(self.coordinate, King("White", self.coordinate))
                boardCopy.tiles[0] = Tile(self.coordinate, NullPiece())
                boardCopy.tiles[3] = Tile(self.coordinate, Rook("White", 3))
                specialMove = True
            if prevPosition == 4 and self.coordinate == 6:
                boardCopy.tiles[self.coordinate] = Tile(self.coordinate, King("White", self.coordinate))
                boardCopy.tiles[7] = Tile(self.coordinate, NullPiece())
                boardCopy.tiles[5] = Tile(self.coordinate, Rook("White", 5))
                specialMove = True

        if self.piece.toString() == "K":
            if prevPosition == 60 and self.coordinate == 58:
                boardCopy.tiles[self.coordinate] = Tile(self.coordinate, King("Black", self.coordinate))
                boardCopy.tiles[56] = Tile(self.coordinate, NullPiece())
                boardCopy.tiles[59] = Tile(self.coordinate, Rook("Black", 59))
                specialMove = True
            if prevPosition == 60 and self.coordinate == 62:
                boardCopy.tiles[self.coordinate] = Tile(self.coordinate, King("Black", self.coordinate))
                boardCopy.tiles[63] = Tile(self.coordinate, NullPiece())
                boardCopy.tiles[61] = Tile(self.coordinate, Rook("Black", 61))
                specialMove = True

        if not specialMove:
            boardCopy.tiles[self.coordinate] = Tile(self.coordinate, self.piece)

        friendlyKing = None
        for tile in boardCopy.tiles.values():
            if (tile.pieceOnTile.toString() == "K" and boardCopy.currentPlayer == "Black") or (
                    tile.pieceOnTile.toString() == "k" and boardCopy.currentPlayer == "White"):
                friendlyKing = tile.pieceOnTile
                break
        if friendlyKing.inCheck(boardCopy):
            return False
        return boardCopy


