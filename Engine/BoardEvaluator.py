def evalBoard(board):
    evaluation = 0
    for tile in board.tiles.values():
        if tile.pieceOnTile.toString() != "-":
            if tile.pieceOnTile.color == "White":
                evaluation += tile.pieceOnTile.value
            else:
                evaluation -= tile.pieceOnTile.value
    return evaluation