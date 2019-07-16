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
        allEnemyAttacks = []
        for tile in board.tiles.values():
            if tile.pieceOnTile.toString() != "-" and tile.pieceOnTile.color != self.color and tile.pieceOnTile.toString().lower() != "k":
                if tile.pieceOnTile.legalMoves(board, prevBoard) is not None:
                    allEnemyAttacks = allEnemyAttacks + tile.pieceOnTile.legalMoves(board, prevBoard)

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
            allEnemyAttacks = []
            copyBoard.tiles[move] = Tile(move, NullPiece())
            for tile in copyBoard.tiles.values():
                if tile.pieceOnTile.toString() != "-" and tile.pieceOnTile.color != self.color and tile.pieceOnTile.toString().lower() != "k":
                    if tile.pieceOnTile.legalMoves(copyBoard, prevBoard) is not None:
                        allEnemyAttacks = allEnemyAttacks + tile.pieceOnTile.legalMoves(copyBoard, prevBoard)
            if move in allEnemyAttacks:
                moves.remove(move)
        return moves

    def inCheck(self, board, prevBoard):
        allEnemyAttacks = []
        for tile in board.tiles.values():
            if tile.pieceOnTile.toString() != "-" and tile.pieceOnTile.color != self.color and tile.pieceOnTile.toString().lower() != "k":
                if tile.pieceOnTile.legalMoves(board, prevBoard) is not None:
                    allEnemyAttacks = allEnemyAttacks + tile.pieceOnTile.legalMoves(board, prevBoard)
        return self.position in allEnemyAttacks

    def inCheckmate(self, board, prevBoard):
        moves = self.legalMoves(board, prevBoard)
        for move in moves:
            copyBoard = copy.deepcopy(board)
            allEnemyAttacks = []
            copyBoard.tiles[move] = Tile(move, NullPiece())
            for tile in copyBoard.tiles.values():
                if tile.pieceOnTile.toString() != "-" and tile.pieceOnTile.color != self.color and tile.pieceOnTile.toString().lower() != "k":
                    if tile.pieceOnTile.legalMoves(copyBoard, prevBoard) is not None:
                        allEnemyAttacks = allEnemyAttacks + tile.pieceOnTile.legalMoves(copyBoard, prevBoard)
            if move in allEnemyAttacks:
                moves.remove(move)

        allFriendlyMoves = []
        for tile in board.tiles.values():
            if tile.pieceOnTile.toString() != "-" and tile.pieceOnTile.color == self.color and tile.pieceOnTile.toString().lower() != "k":
                if tile.pieceOnTile.legalMoves(board, prevBoard) is not None:
                    allFriendlyMoves = allFriendlyMoves + tile.pieceOnTile.legalMoves(board, prevBoard)
        copyBoard = copy.deepcopy(board)
        for number in allFriendlyMoves:
            if copyBoard.tiles[number].pieceOnTile.toString() != "-" and copyBoard.tiles[number].pieceOnTile.color != self.color:
                copyBoard.tiles[number] = Tile(number, NullPiece())


        return not moves and self.inCheck(board, prevBoard) and self.inCheck(copyBoard, prevBoard)



    def inStalemate(self, board, prevBoard):
        allFriendlyMoves = []
        for tile in board.tiles.values():
            if tile.pieceOnTile.toString() != "-" and tile.pieceOnTile.color == self.color:
                if tile.pieceOnTile.legalMoves(board, prevBoard) is not None:
                    allFriendlyMoves = allFriendlyMoves + tile.pieceOnTile.legalMoves(board, prevBoard)
        return not allFriendlyMoves and not self.inCheck(board, prevBoard)

