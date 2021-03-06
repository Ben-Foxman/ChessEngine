from Game.Tile import Tile
from Pieces.NullPiece import NullPiece
from Pieces.Rook import Rook
from Pieces.Queen import Queen
from Pieces.King import King
from Pieces.Pawn import Pawn
from Pieces.Bishop import Bishop
from Pieces.Knight import Knight

class Board:
    def __init__(self):
        self.currentPlayer = "White"
        self.tiles = dict()
        self.moveCounter = 1
        self.prevBoard = None
        for x in range(64):
            self.tiles[x] = (Tile(x, NullPiece()))
        for x in range(8, 16):
            pass
            self.tiles[x] = (Tile(x, Pawn("White", x)))
        for x in range(48, 56):
            self.tiles[x] = (Tile(x, Pawn("Black", x)))

        self.tiles[0] = (Tile(0, Rook("White", 0)))
        self.tiles[1] = (Tile(1, Knight("White", 1)))
        self.tiles[2] = (Tile(2, Bishop("White", 2)))
        self.tiles[3] = (Tile(3, Queen("White", 3)))
        self.tiles[4] = (Tile(4, King("White", 4)))
        self.tiles[5] = (Tile(5, Bishop("White", 5)))
        self.tiles[6] = (Tile(6, Knight("White", 6)))
        self.tiles[7] = (Tile(7, Rook("White", 7)))
        self.tiles[56] = (Tile(56, Rook("Black", 56)))
        self.tiles[57] = (Tile(57, Knight("Black", 57)))
        self.tiles[58] = (Tile(58, Bishop("Black", 58)))
        self.tiles[59] = (Tile(59, Queen("Black", 59)))
        self.tiles[60] = (Tile(60, King("Black", 60)))
        self.tiles[61] = (Tile(61, Bishop("Black", 61)))
        self.tiles[62] = (Tile(62, Knight("Black", 62)))
        self.tiles[63] = (Tile(63, Rook("Black", 63)))


    def printBoard(self):
        for x in range(8):
            for y in range(8):
                print("|", end=self.tiles[8 * (7 - x) + y].pieceOnTile.toString())
            print("|")

    def allEnemyAttacks(self):
        allEnemyAttacks = []
        for tile in self.tiles.values():
            if tile.pieceOnTile.toString() != "-" and tile.pieceOnTile.color != self.currentPlayer:
                if tile.pieceOnTile.toString().lower() == "k":
                    allEnemyAttacks = allEnemyAttacks + tile.pieceOnTile.rawMoves(self)
                elif tile.pieceOnTile.legalMoves(self) is not None:
                    if tile.pieceOnTile.toString().lower() == "p":
                        allEnemyAttacks = allEnemyAttacks + tile.pieceOnTile.possibleCaptures(self)
                    else:
                        allEnemyAttacks = allEnemyAttacks + tile.pieceOnTile.legalMoves(self)
        return allEnemyAttacks

    def allFriendlyAttacks(self):
        allFriendlyAttacks = []
        for tile in self.tiles.values():
            if tile.pieceOnTile.color == self.currentPlayer:
                if tile.pieceOnTile.toString().lower() == "k":
                    allFriendlyAttacks = allFriendlyAttacks + tile.pieceOnTile.rawMoves(self)
                elif tile.pieceOnTile.legalMoves(self) is not None:
                    if tile.pieceOnTile.toString().lower() == "p":
                        allFriendlyAttacks = allFriendlyAttacks + tile.pieceOnTile.possibleCaptures(self)
                    else:
                        allFriendlyAttacks = allFriendlyAttacks + tile.pieceOnTile.legalMoves(self)
        return allFriendlyAttacks

    def allFriendlyPieces(self):
        allFriendlyPieces = []
        for tile in self.tiles.values():
            if tile.pieceOnTile.color == self.currentPlayer:
                allFriendlyPieces.append(tile.pieceOnTile)
        return allFriendlyPieces

    def allFriendlyMoves(self):
        moves = []
        for piece in self.allFriendlyPieces():
            if piece.color == self.currentPlayer:
                if piece.legalMoves(self) is not None:
                    moves = moves + piece.legalMoves(self)
        return moves



