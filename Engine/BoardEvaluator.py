from Game.Board import Board
import math
import time

class BoardEvaluator:
    def __init__(self, board):
        self.board = board
        self.pawns = self.getPawns()
        self.knights = self.getKnights()
        self.bishops = self.getBishops()
        self.rooks = self.getRooks()
        self.queens = self.getQueens()
        self.kings = self.getKings()
        if self.board.currentPlayer == "White":
            self.blackCovers = self.board.allEnemyAttacks()
            self.whiteCovers = self.board.allFriendlyAttacks()
        else:
            self.whiteCovers = self.board.allEnemyAttacks()
            self.blackCovers = self.board.allFriendlyAttacks()

    def evalBoard(self):
        evaluation = 0
        for tile in self.board.tiles.values():
            if tile.pieceOnTile.toString() != "-":
                if tile.pieceOnTile.color == "White":
                    evaluation += tile.pieceOnTile.value
                else:
                    evaluation -= tile.pieceOnTile.value
        evaluation += self.applyHeuristics()
        return evaluation
    
    #heuristics
    def applyHeuristics(self):
        eval = 0
        # methods
        eval += self.kingInCheckmate()
        if eval in [math.inf, -math.inf]:
            return eval
        eval += self.kingIsSafe()
        eval += self.prematureQueenMove()
        eval += self.bishopPair()
        eval += self.squaresCovered()
        eval += self.enemyPiecesAttacked()
        eval += self.friendlyPiecesDefended()
        eval += self.pawnsSixthAndSeventh()
        eval += self.adjustMinorPiecesPC()
        eval += self.knightOnTheRim()
    
        return eval
    
    #common variables

    def kingInCheckmate(self):
        hold = self.board.currentPlayer
        for king in self.kings:
            if self.board.currentPlayer == "White":
                    self.board.currentPlayer = "Black"
                    if king.color == "Black" and king.inCheckmate(self.board):
                        self.board.currentPlayer = hold
                        return math.inf
            if self.board.currentPlayer == "Black":
                    self.board.currentPlayer = "White"
                    if king.color == "White" and king.inCheckmate(self.board):
                        self.board.currentPlayer = hold
                        return -math.inf
        self.board.currentPlayer = hold
        return 0
    
    
    
    
    def kingIsSafe(self):
        eval = 0
        for king in self.kings:
            if self.isOpening() or self.isMiddlegame():
                if king.color == "White":
                    pos = king.position
                    if pos // 8 in [0, 1] and self.posToPiece(pos + 8) == "p":
                        eval += .05
                    if pos // 8 in [0, 1] and self.posToPiece(pos + 9) == "p":
                        eval += .05
                    if pos // 8 in [0, 1] and self.posToPiece(pos + 7) == "p":
                        eval += .05
                    if pos in [0, 1, 2, 6, 7]:
                        eval += .15
                if king.color == "Black":
                    pos = king.position
                    if pos // 8 in [6, 7] and self.posToPiece(pos - 8) == "P":
                        eval -= .05
                    if pos // 8 in [6, 7] and self.posToPiece(pos - 9) == "P":
                        eval -= .05
                    if pos // 8 in [6, 7] and self.posToPiece(pos - 7) == "P":
                        eval -= .05
                    if pos in [56, 57, 58, 62, 63]:
                        eval -= .15
        return eval
    
    def bishopPair(self):
        eval = 0
        whiteCount = blackCount = 0
        for bishop in self.bishops:
            if bishop.color == "White":
                whiteCount += 1
            else:
                blackCount += 1
        if whiteCount == 2:
            eval += .2
        if blackCount == 2:
            eval -= .2
        return eval
    
    
    def adjustMinorPiecesPC(self):
        eval = 0
        pawnCount = len(self.pawns)
        if 0 <= pawnCount < 8:
            for bishop in self.bishops:
                if bishop.color == "White":
                    eval += .25
                else:
                    eval -= .25
            for knight in self.knights:
                if knight.color == "White":
                    eval -= .25
                else:
                    eval += .25
        if 12 <= pawnCount < 16:
            for bishop in self.bishops:
                if bishop.color == "White":
                    eval -= .25
                else:
                    eval += .25
            for knight in self.knights:
                if knight.color == "White":
                    eval += .25
                else:
                    eval -= .25
        return eval
    
    
    
    def doubledPawnCount(self):
        pass
    
    def pawnsSixthAndSeventh(self):
        eval = 0
        for pawn in self.pawns:
            if pawn.color == "White":
                if pawn.position // 8 == 5:
                    eval += .25
                if pawn.position // 8 == 6:
                    eval += 1.25
            if pawn.color == "Black":
                if pawn.position // 8 == 2:
                    eval += .25
                if pawn.position // 8 == 1:
                    eval += 1.25
        return eval
    
    
    
    
    def prematureQueenMove(self):
        eval = 0
        if self.isOpening():
            for queen in self.queens:
                if queen.color == "White" and queen.position % 8 not in [0, 1]:
                    eval -= 1.3
                elif queen.color == "Black" and queen.position % 8 not in [6, 7]:
                    eval += 1.3
        return eval
    
    
    def squaresCovered(self):
        eval = 0
        importance = {x :((31.5 - abs(31.5 - x)) / 8 + (3.5 - abs(3.5 - x)) % 7)** 1.5 * .002 for x in range(0, 64)}
        for val in self.whiteCovers:
            eval += importance[val]
        for val in self.blackCovers:
            eval -= importance[val]
        return eval
    
    
    
    def enemyPiecesAttacked(self):
        eval = 0
        for val in self.whiteCovers:
            if self.board.tiles[val].pieceOnTile.color == "Black":
                eval += .1 * self.board.tiles[val].pieceOnTile.value ** .3
        for val in self.blackCovers:
            if self.board.tiles[val].pieceOnTile.color == "Black":
                eval -= .1 * self.board.tiles[val].pieceOnTile.value ** .3
        return eval
    
    def friendlyPiecesDefended(self):
        eval = 0
        for val in self.whiteCovers:
            if self.board.tiles[val].pieceOnTile.color == "White":
                eval += .3 * self.board.tiles[val].pieceOnTile.value ** .3
        for val in self.blackCovers:
            if self.board.tiles[val].pieceOnTile.color == "Black":
                eval -= .3 * self.board.tiles[val].pieceOnTile.value ** .3
        return eval
    
    
    def kingActivity(self):
        importance = {x: ((31.5 - abs(31.5 - x)) / 8 + (3.5 - abs(3.5 - x)) % 7) ** 2 * .002 for x in range(0, 64)}
        for king in self.kings:
            if king.color == "White":
                if self.isEndgame():
                    pass
    
    def knightOnTheRim(self):
        eval = 0
        for knight in self.knights:
            pos = knight.position
            if knight.color == "White" and (pos % 8 in [0, 7] or pos // 8 in [0, 7]):
                eval += .2
            if knight.color == "Black" and (pos % 8 in [0, 7] or pos // 8 in [0, 7]):
                eval -= .2
        return eval

    
    
    def goodBishops(self):
        pass
    
    def rooksDoubled(self):
        pass
    
    
    # helper methods
    def posToPiece(self, position):
        return self.board.tiles[position].pieceOnTile.toString()
    
    def getKings(self):
        kings = []
        for tile in self.board.tiles.values():
            if tile.pieceOnTile.toString().lower() == "k":
                kings.append(tile.pieceOnTile)
        return kings
    
    def getQueens(self):
        queens = []
        for tile in self.board.tiles.values():
            if tile.pieceOnTile.toString().lower() == "q":
                queens.append(tile.pieceOnTile)
        return queens
    
    def getRooks(self):
        rooks = []
        for tile in self.board.tiles.values():
            if tile.pieceOnTile.toString().lower() == "r":
                rooks.append(tile.pieceOnTile)
        return rooks
    
    def getBishops(self):
        bishops = []
        for tile in self.board.tiles.values():
            if tile.pieceOnTile.toString().lower() == "b":
                bishops.append(tile.pieceOnTile)
        return bishops
    
    def getKnights(self):
        knights = []
        for tile in self.board.tiles.values():
            if tile.pieceOnTile.toString().lower() == "n":
                knights.append(tile.pieceOnTile)
        return knights
    
    def getPawns(self):
        pawns = []
        for tile in self.board.tiles.values():
            if tile.pieceOnTile.toString().lower() == "p":
                pawns.append(tile.pieceOnTile)
        return pawns
    
    def isOpening(self):
        return self.board.moveCounter < 12
    
    def isMiddlegame(self):
        return 12 <= self.board.moveCounter < 35
    
    def isEndgame(self):
        return 35 <= self.board.moveCounter


def newEvaluation(board):
    x = BoardEvaluator(board)
    return x.evalBoard()

