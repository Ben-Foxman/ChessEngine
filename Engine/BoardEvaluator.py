from Game.Board import Board

b = Board()

def evalBoard(board):
    evaluation = 0
    for tile in board.tiles.values():
        if tile.pieceOnTile.toString() != "-":
            if tile.pieceOnTile.color == "White":
                evaluation += tile.pieceOnTile.value
            else:
                evaluation -= tile.pieceOnTile.value
    evaluation += applyHeuristics(board)
    return evaluation

#heuristics

def applyHeuristics(board):
    eval = 0
    # methods
    eval += kingIsSafe(board)
    eval += prematureQueenMove(board)
    eval += bishopPair(board)
    eval += squaresCovered(board)
    eval += enemyPiecesAttacked(board)
    eval += friendlyPiecesDefended(board)

    return eval

def kingIsSafe(board):
    eval = 0
    kings = getKings(board)
    for king in kings:
        if isOpening(board) or isMiddlegame(board):
            if king.color == "White":
                pos = king.position
                if pos // 8 in [0, 1] and posToPiece(board, pos + 8) == "p":
                    eval += .05
                if pos // 8 in [0, 1] and posToPiece(board, pos + 9) == "p":
                    eval += .05
                if pos // 8 in [0, 1] and posToPiece(board, pos + 7) == "p":
                    eval += .05
                if pos in [0, 1, 2, 6, 7]:
                    eval += .15
            if king.color == "Black":
                pos = king.position
                if pos // 8 in [6, 7] and posToPiece(board, pos - 8) == "P":
                    eval -= .05
                if pos // 8 in [6, 7] and posToPiece(board, pos - 9) == "P":
                    eval -= .05
                if pos // 8 in [6, 7] and posToPiece(board, pos - 7) == "P":
                    eval -= .05
                if pos in [56, 57, 58, 62, 63]:
                    eval -= .15
    return eval





def bishopPair(board):
    eval = 0
    bishops = getBishops(board)
    whiteCount = blackCount = 0
    for bishop in bishops:
        if bishop.color == "White":
            whiteCount += 1
        else:
            blackCount += 1
    if whiteCount == 2:
        eval += .2
    if blackCount == 2:
        eval -= .2
    return eval


def adjustMinorPiecesPC(board):
    pass

def doubledPawnCount(board):
    pass

def prematureQueenMove(board):
    eval = 0
    if isOpening(board):
        queens = getQueens(board)
        for queen in queens:
            if queen.color == "White" and queen.position % 8 not in [0, 1]:
                eval -= .4
            elif queen.color == "Black" and queen.position % 8 not in [6, 7]:
                eval += .4
    return eval


def squaresCovered(board):
    eval = 0
    if board.currentPlayer == "White":
        blackCovers = board.allEnemyAttacks(b.prevBoard)
        whiteCovers = board.allFriendlyAttacks(b.prevBoard)
    else:
        whiteCovers = board.allEnemyAttacks(b.prevBoard)
        blackCovers = board.allFriendlyAttacks(b.prevBoard)
    importance = {x :((31.5 - abs(31.5 - x)) / 8 + (3.5 - abs(3.5 - x)) % 7)** 2 * .002 for x in range(0, 64)}
    for val in whiteCovers:
        eval += importance[val]
    for val in blackCovers:
        eval -= importance[val]
    return eval



def enemyPiecesAttacked(board):
    eval = 0
    if board.currentPlayer == "White":
        blackCovers = board.allEnemyAttacks(b.prevBoard)
        whiteCovers = board.allFriendlyAttacks(b.prevBoard)
    else:
        whiteCovers = board.allEnemyAttacks(b.prevBoard)
        blackCovers = board.allFriendlyAttacks(b.prevBoard)
    for val in whiteCovers:
        if board.tiles[val].pieceOnTile.color == "Black":
            eval += .1 * board.tiles[val].pieceOnTile.value
    for val in blackCovers:
        if board.tiles[val].pieceOnTile.color == "Black":
            eval -= .1 * board.tiles[val].pieceOnTile.value
    return eval

def friendlyPiecesDefended(board):
    eval = 0
    if board.currentPlayer == "White":
        blackCovers = board.allEnemyAttacks(b.prevBoard)
        whiteCovers = board.allFriendlyAttacks(b.prevBoard)
    else:
        whiteCovers = board.allEnemyAttacks(b.prevBoard)
        blackCovers = board.allFriendlyAttacks(b.prevBoard)
    for val in whiteCovers:
        if board.tiles[val].pieceOnTile.color == "White":
            eval += .025 * board.tiles[val].pieceOnTile.value
    for val in blackCovers:
        if board.tiles[val].pieceOnTile.color == "Black":
            eval -= .025 * board.tiles[val].pieceOnTile.value
    return eval


def kingActivity(board):
    pass

def goodBishops(board):
    pass

def rooksDoubled(board):
    pass


# helper methods
def posToPiece(board, position):
    return board.tiles[position].pieceOnTile.toString()

def getKings(board):
    kings = []
    for tile in board.tiles.values():
        if tile.pieceOnTile.toString().lower() == "k":
            kings.append(tile.pieceOnTile)
    return kings

def getQueens(board):
    queens = []
    for tile in board.tiles.values():
        if tile.pieceOnTile.toString().lower() == "q":
            queens.append(tile.pieceOnTile)
    return queens

def getRooks(board):
    rooks = []
    for tile in board.tiles.values():
        if tile.pieceOnTile.toString().lower() == "r":
            rooks.append(tile.pieceOnTile)
    return rooks

def getBishops(board):
    bishops = []
    for tile in board.tiles.values():
        if tile.pieceOnTile.toString().lower() == "b":
            bishops.append(tile.pieceOnTile)
    return bishops

def getKnights(board):
    knights = []
    for tile in board.tiles.values():
        if tile.pieceOnTile.toString().lower() == "n":
            knights.append(tile.pieceOnTile)
    return knights

def getPawns(board):
    pawns = []
    for tile in board.tiles.values():
        if tile.pieceOnTile.toString().lower() == "p":
            pawns.append(tile.pieceOnTile)
    return pawns

def isOpening(board):
    return board.moveCounter < 12

def isMiddlegame(board):
    return 12 <= board.moveCounter < 30

def isEndgame(board):
    return 30 <= board.moveCounter



