



def evalBoard(board):
    evaluation = 0
    for tile in board.tiles.values():
        if tile.pieceOnTile.toString() != "-":
            if tile.pieceOnTile.color == "White":
                evaluation += tile.pieceOnTile.value
            else:
                evaluation -= tile.pieceOnTile.value
    return evaluation

#heuristics

def applyHeuristics(board):
    pass

def kingIsSafe(board):
    pass

def bishopPair(board):
    pass

def totalPawnCount(board):
    pass

def doubledPawnCount(board):
    pass

def prematureQueenMove(board):
    pass

def squaresCovered(board):
    pass

def enemyPiecesAttacked(board):
    pass

def kingActivity(board):
    pass

def goodBishops(board):
    pass

def rooksDoubled(board):
    pass


