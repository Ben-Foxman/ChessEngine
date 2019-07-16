from Pieces.Piece import *


class Rook(Piece):
    # Class representing a pawn
    def __init__(self, color, position):
        super().__init__(color, position, value=5)
        self.moved = False

    def toString(self):
        return "R" if self.color == "Black" else "r"

    def legalMoves(self, board, prevBoard):
        destinations = []
        startingCoordinate = self.position
        # Up
        while 0 <= startingCoordinate < 56:
            startingCoordinate += 8
            if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                destinations.append(startingCoordinate)
            elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                destinations.append(startingCoordinate)
                break
            else:
                break

        startingCoordinate = self.position
        # Down
        while 8 <= startingCoordinate < 64:
            startingCoordinate -= 8
            if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                destinations.append(startingCoordinate)
            elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                destinations.append(startingCoordinate)
                break
            else:
                break

        startingCoordinate = self.position
        # Right
        while 0 <= startingCoordinate < 63:
            if startingCoordinate % 8 == 7:
                break
            else:
                startingCoordinate += 1
                if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                    destinations.append(startingCoordinate)
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break

        startingCoordinate = self.position
        # Left
        while 1 <= startingCoordinate < 64:
            if startingCoordinate % 8 == 0:
                break
            else:
                startingCoordinate -= 1
                if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                    destinations.append(startingCoordinate)
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break

        startingCoordinate = self.position
        destinations = list(filter(lambda x: x != startingCoordinate, destinations))
        return destinations