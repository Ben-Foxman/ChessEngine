from Pieces.Piece import *


class Bishop(Piece):
    # Class representing a pawn
    def __init__(self, color, position):
        super().__init__(color, position,value=3)

    def toString(self):
        return "B" if self.color == "Black" else "b"

    def legalMoves(self, board, prevBoard):
        destinations = []
        startingCoordinate = self.position
        # Up Left
        while 0 <= startingCoordinate < 56:
            if startingCoordinate % 8 == 0:
                break
            else:
                startingCoordinate += 7
                if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                    destinations.append(startingCoordinate)
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break

        startingCoordinate = self.position
        # Down Left
        while 9 <= startingCoordinate < 64:
            if startingCoordinate % 8 == 0:
                break
            else:
                startingCoordinate -= 9
                if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                    destinations.append(startingCoordinate)
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break

        startingCoordinate = self.position
        # Up Right
        while 0 <= startingCoordinate < 55:
            if startingCoordinate % 8 == 7:
                break
            else:
                startingCoordinate += 9
                if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                    destinations.append(startingCoordinate)
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break

        startingCoordinate = self.position
        # Down Right
        while 8 <= startingCoordinate < 64:
            if startingCoordinate % 8 == 7:
                break
            else:
                startingCoordinate -= 7
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





