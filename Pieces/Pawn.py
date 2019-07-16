from Pieces.Piece import *

class Pawn(Piece):
    # Class representing a pawn
    def __init__(self, color, position):
        super().__init__(color, position,value=1)

    def toString(self):
        return "P" if self.color == "Black" else "p"

    def legalMoves(self, board, prevBoard):
        destinations = []
        if self.color == "White":
            if 8 <= self.position < 16:
                if board.tiles[self.position + 8].pieceOnTile.toString() == "-":
                    destinations.append(self.position + 8)
                    if board.tiles[self.position + 16].pieceOnTile.toString() == "-":
                        destinations.append(self.position + 16)
                if board.tiles[self.position + 7].pieceOnTile.toString() != "-" and \
                        board.tiles[self.position + 7].pieceOnTile.color != self.color and self.position % 8 != 0:
                    destinations.append(self.position + 7)
                if board.tiles[self.position + 9].pieceOnTile.toString() != "-" and \
                        board.tiles[self.position + 9].pieceOnTile.color != self.color and self.position % 8 != 7:
                    destinations.append(self.position + 9)

            elif 16 <= self.position < 56:

                #en passant check
                if 32 <= self.position < 40:
                    if self.position % 8 == 0:
                        if board.tiles[33].pieceOnTile.toString() == "P" and prevBoard.tiles[49].pieceOnTile.toString() == "P" and \
                                prevBoard.tiles[41].pieceOnTile.toString() == "-":
                                destinations.append(41)
                    elif self.position % 8 == 7:
                        if board.tiles[38].pieceOnTile.toString() == "P" and prevBoard.tiles[54].pieceOnTile.toString() == "P" and \
                                prevBoard.tiles[46].pieceOnTile.toString() == "-":
                                destinations.append(46)
                    else:
                        if board.tiles[self.position + 1].pieceOnTile.toString() == "P" and prevBoard.tiles[self.position + 17].pieceOnTile.toString() == "P" and \
                                prevBoard.tiles[self.position + 9].pieceOnTile.toString() == "-":
                                destinations.append(self.position + 9)
                        if board.tiles[self.position - 1].pieceOnTile.toString() == "P" and prevBoard.tiles[self.position + 15].pieceOnTile.toString() == "P" and \
                                prevBoard.tiles[self.position + 7].pieceOnTile.toString() == "-":
                                destinations.append(self.position + 7)

                if board.tiles[self.position + 7].pieceOnTile.toString() != "-" and \
                        board.tiles[self.position + 7].pieceOnTile.color != self.color and self.position % 8 != 0:
                    destinations.append(self.position + 7)
                if board.tiles[self.position + 9].pieceOnTile.toString() != "-" and \
                        board.tiles[self.position + 9].pieceOnTile.color != self.color and self.position % 8 != 7:
                    destinations.append(self.position + 9)
                if board.tiles[self.position + 8].pieceOnTile.toString() == "-":
                    destinations.append(self.position + 8)
        else:
            if 48 <= self.position < 56:
                if board.tiles[self.position - 8].pieceOnTile.toString() == "-":
                    destinations.append(self.position - 8)
                    if board.tiles[self.position - 16].pieceOnTile.toString() == "-":
                        destinations.append(self.position - 16)
                if board.tiles[self.position - 7].pieceOnTile.toString() != "-" and \
                        board.tiles[self.position - 7].pieceOnTile.color != self.color and self.position % 8 != 7:
                    destinations.append(self.position - 7)
                if board.tiles[self.position - 9].pieceOnTile.toString() != "-" and \
                        board.tiles[self.position - 9].pieceOnTile.color != self.color and self.position % 8 != 0:
                    destinations.append(self.position - 9)
            elif 8 <= self.position < 48:

                # en passant check
                if 24 <= self.position < 31:
                    if self.position % 8 == 0:
                        if board.tiles[25].pieceOnTile.toString() == "p" and prevBoard.tiles[
                            9].pieceOnTile.toString() == "p" and \
                                prevBoard.tiles[17].pieceOnTile.toString() == "-":
                            destinations.append(17)
                    elif self.position % 8 == 7:
                        if board.tiles[30].pieceOnTile.toString() == "p" and prevBoard.tiles[
                            14].pieceOnTile.toString() == "p" and \
                                prevBoard.tiles[22].pieceOnTile.toString() == "-":
                            destinations.append(22)
                    else:
                        if board.tiles[self.position + 1].pieceOnTile.toString() == "p" and prevBoard.tiles[
                            self.position - 15].pieceOnTile.toString() == "p" and \
                                prevBoard.tiles[self.position - 7].pieceOnTile.toString() == "-":
                            destinations.append(self.position - 7)
                        if board.tiles[self.position - 1].pieceOnTile.toString() == "p" and prevBoard.tiles[
                            self.position - 17].pieceOnTile.toString() == "p" and \
                                prevBoard.tiles[self.position - 9].pieceOnTile.toString() == "-":
                            destinations.append(self.position - 9)



                if board.tiles[self.position - 7].pieceOnTile.toString() != "-" and \
                        board.tiles[self.position - 7].pieceOnTile.color != self.color and self.position % 8 != 7:
                    destinations.append(self.position - 7)
                if board.tiles[self.position - 9].pieceOnTile.toString() != "-" and \
                        board.tiles[self.position - 9].pieceOnTile.color != self.color and self.position % 8 != 0:
                    destinations.append(self.position - 9)
                if board.tiles[self.position - 8].pieceOnTile.toString() == "-":
                    destinations.append(self.position - 8)
        return destinations
