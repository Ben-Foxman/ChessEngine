from Pieces.Piece import *
from Pieces.NullPiece import NullPiece
from Game.Tile import Tile
import copy
class King(Piece):
    # Class representing a king
    def __init__(self, color, position):
        super().__init__(color, position,value=150)
        self.moved = False

    def toString(self):
        return "K" if self.color == "Black" else "k"

    def legalMoves(self, board):
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
                    break
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
                    break
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
                    break
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
                    break
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break

        startingCoordinate = self.position
        # Up
        while 0 <= startingCoordinate < 56:
            startingCoordinate += 8
            if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                destinations.append(startingCoordinate)
                break
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
                break
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
                    break
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
                    break
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break

        startingCoordinate = self.position
        destinations = list(filter(lambda x: x != startingCoordinate, destinations))
        allEnemyAttacks = board.allEnemyAttacks()


        # deal with castling
        if self.moved == False:
            if self.color == "White":
                if self.position == 4 and board.tiles[0].pieceOnTile.toString() == "r" and board.tiles[0].pieceOnTile.moved == False:
                    if not 2 in allEnemyAttacks and not 3 in allEnemyAttacks and not 4 in allEnemyAttacks:
                        if board.tiles[1].pieceOnTile.toString() == "-":
                            if board.tiles[2].pieceOnTile.toString() == "-":
                                if board.tiles[3].pieceOnTile.toString() == "-":
                                    destinations.append(2)
                if self.position == 4 and board.tiles[7].pieceOnTile.toString() == "r" and board.tiles[7].pieceOnTile.moved == False:
                    if not 5 in allEnemyAttacks and not 4 in allEnemyAttacks and not 6 in allEnemyAttacks:
                        if board.tiles[6].pieceOnTile.toString() == "-":
                            if board.tiles[5].pieceOnTile.toString() == "-":
                                destinations.append(6)
            if self.color == "Black":
                if self.position == 60 and board.tiles[56].pieceOnTile.toString() == "R" and board.tiles[56].pieceOnTile.moved == False:
                    if not 58 in allEnemyAttacks and not 59 in allEnemyAttacks and not 60 in allEnemyAttacks:
                        if board.tiles[58].pieceOnTile.toString() == "-":
                            if board.tiles[59].pieceOnTile.toString() == "-":
                                if board.tiles[57].pieceOnTile.toString() == "-":
                                    destinations.append(58)
                if self.position == 60 and board.tiles[63].pieceOnTile.toString() == "R" and board.tiles[63].pieceOnTile.moved == False:
                    if not 60 in allEnemyAttacks and not 61 in allEnemyAttacks and not 62 in allEnemyAttacks:
                        if board.tiles[61].pieceOnTile.toString() == "-":
                            if board.tiles[62].pieceOnTile.toString() == "-":
                                destinations.append(62)
        ######
        finalMoves = []
        for move in destinations:
            if move not in allEnemyAttacks:
                finalMoves.append(move)

        moves = finalMoves
        for move in moves:
            copyBoard = copy.deepcopy(board)
            copyBoard.tiles[move] = Tile(move, NullPiece())
            allEnemyAttacks = copyBoard.allEnemyAttacks()
            if move in allEnemyAttacks:
                moves.remove(move)
        return moves
    def rawMoves(self, board):
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
                    break
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
                    break
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
                    break
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
                    break
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break

        startingCoordinate = self.position
        # Up
        while 0 <= startingCoordinate < 56:
            startingCoordinate += 8
            if board.tiles[startingCoordinate].pieceOnTile.toString() == "-":
                destinations.append(startingCoordinate)
                break
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
                break
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
                    break
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
                    break
                elif board.tiles[startingCoordinate].pieceOnTile.color != self.color:
                    destinations.append(startingCoordinate)
                    break
                else:
                    break

        startingCoordinate = self.position
        destinations = list(filter(lambda x: x != startingCoordinate, destinations))

        return destinations
    def inCheck(self, board):
        allEnemyAttacks = board.allEnemyAttacks()
        return self.position in allEnemyAttacks

    def inCheckmate(self, board):
        moves = self.legalMoves(board)
        for move in moves:
            copyBoard = copy.deepcopy(board)
            copyBoard.tiles[move] = Tile(move, NullPiece())
            allEnemyAttacks = copyBoard.allEnemyAttacks()
            if move in allEnemyAttacks:
                moves.remove(move)

        allFriendlyMoves = []
        allFriendlyPieces = []
        for tile in board.tiles.values():
            if tile.pieceOnTile.toString() != "-" and tile.pieceOnTile.color == self.color:
                if tile.pieceOnTile.toString().lower() != "k":
                    allFriendlyPieces.append(tile.pieceOnTile)
                if tile.pieceOnTile.legalMoves(board) is not None:
                    allFriendlyMoves = allFriendlyMoves + tile.pieceOnTile.legalMoves(board)


        for piece in allFriendlyPieces:
            legalMoves = piece.legalMoves(board)
            if legalMoves is not None:
                for move in legalMoves:
                    copyBoard = copy.deepcopy(board)
                    copyBoard.tiles[piece.position] = Tile(piece.position, NullPiece())
                    copyBoard.tiles[move] = Tile(move, piece)
                    if not self.inCheck(copyBoard):
                        return False

        copyBoard = copy.deepcopy(board)

        for number in allFriendlyMoves:
            if copyBoard.tiles[number].pieceOnTile.color != self.color:
                copyBoard.tiles[number] = Tile(number, NullPiece())


        return not moves and self.inCheck(copyBoard) # and self.inCheck(copyBoard, )



    def inStalemate(self, board):
        allFriendlyMoves = []
        for tile in board.tiles.values():
            if tile.pieceOnTile.toString() != "-" and tile.pieceOnTile.color == self.color:
                if tile.pieceOnTile.legalMoves(board) is not None:
                    allFriendlyMoves = allFriendlyMoves + tile.pieceOnTile.legalMoves(board)
        return not allFriendlyMoves and not self.inCheck(board)

