from Pieces.Piece import *
import copy
from Game.Tile import Tile
from Pieces.NullPiece import NullPiece

class Knight(Piece):
    # Class representing a pawn
    def __init__(self, color, position):
        super().__init__(color, position, value=3)

    def toString(self):
        return "N" if self.color == "Black" else "n"

    def legalMoves(self, board):
        destinations = []
        startingCoordinate = self.position
        # NNE move
        while 0 <= startingCoordinate < 47:
            if startingCoordinate % 8 == 7:
                break
            else:
                startingCoordinate += 17
                if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                    destinations.append(startingCoordinate)
                    break
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break
        startingCoordinate = self.position
        # NNW move
        while 1 <= startingCoordinate < 48:
            if startingCoordinate % 8 == 0:
                break
            else:
                startingCoordinate += 15
                if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                    destinations.append(startingCoordinate)
                    break
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break
        startingCoordinate = self.position
        # NEE move
        while 0 <= startingCoordinate < 54:
            if startingCoordinate % 8 in [6, 7]:
                break
            else:
                startingCoordinate += 10
                if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                    destinations.append(startingCoordinate)
                    break
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break

        startingCoordinate = self.position
        # NWW move
        while 2 <= startingCoordinate < 56:
            if startingCoordinate % 8 in [0, 1]:
                break
            else:
                startingCoordinate += 6
                if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                    destinations.append(startingCoordinate)
                    break
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break
        startingCoordinate = self.position
        # SSE move
        while 16 <= startingCoordinate < 63:
            if startingCoordinate % 8 == 7:
                break
            else:
                startingCoordinate -= 15
                if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                    destinations.append(startingCoordinate)
                    break
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break
        startingCoordinate = self.position
        # SSW move
        while 17 <= startingCoordinate < 64:
            if startingCoordinate % 8 == 0:
                break
            else:
                startingCoordinate -= 17
                if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                    destinations.append(startingCoordinate)
                    break
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break
        startingCoordinate = self.position
        # SWW move
        while 10 <= startingCoordinate < 64:
            if startingCoordinate % 8 in [0, 1]:
                break
            else:
                startingCoordinate -= 10
                if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                    destinations.append(startingCoordinate)
                    break
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break
        startingCoordinate = self.position
        # SEE move
        while 8 <= startingCoordinate < 62:
            if startingCoordinate % 8 in [6, 7]:
                break
            else:
                startingCoordinate -= 6
                if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                    destinations.append(startingCoordinate)
                    break
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break

        startingCoordinate = self.position
        destinations = list(filter(lambda x: x != startingCoordinate, destinations))

        return destinations

