import Pieces


class Board:
    """ Instance Variables:
            squares: dictionary of squares and the piece(or None) currently on them.
            white_to_move: starts True. alternates every turn.
            move_count: starts at 1. Increments when white_to_move is set to true.
            game_over: starts False. Goes to true if a player has no legal moves and has the turn to move. Leads
            to a determination of checkmate( +/- infinity) or stalemate(0)

        Methods:
            .get_set_of_pieces(color) - returns set of all (color) pieces on the board
            .legal_moves(piece) - returns all legal moves for piece
            .num_legal_moves(arr_piece) - returns number of legal moves for an array of pieces - not yet implemented
            """
    def __init__(self):
        self.squares = {(x, y): None for x in range(8) for y in range(8)}
        for x in range(8):
            self.squares[(x, 1)] = Pieces.Pawn(Pieces.Color.white, (x, 1))
            self.squares[(x, 6)] = Pieces.Pawn(Pieces.Color.black, (x, 6))
        self.squares[(0, 0)] = Pieces.Rook(Pieces.Color.white, (0, 0))
        self.squares[(1, 0)] = Pieces.Knight(Pieces.Color.white, (1, 0))
        self.squares[(2, 0)] = Pieces.Bishop(Pieces.Color.white, (2, 0))
        self.squares[(3, 0)] = Pieces.Queen(Pieces.Color.white, (3, 0))
        self.squares[(4, 0)] = Pieces.King(Pieces.Color.white, (4, 0))
        self.squares[(5, 0)] = Pieces.Bishop(Pieces.Color.white, (5, 0))
        self.squares[(6, 0)] = Pieces.Knight(Pieces.Color.white, (6, 0))
        self.squares[(7, 0)] = Pieces.Rook(Pieces.Color.white, (7, 0))
        self.squares[(0, 7)] = Pieces.Rook(Pieces.Color.black, (0, 7))
        self.squares[(1, 7)] = Pieces.Knight(Pieces.Color.black, (1, 7))
        self.squares[(2, 7)] = Pieces.Bishop(Pieces.Color.black, (2, 7))
        self.squares[(3, 7)] = Pieces.Queen(Pieces.Color.black, (3, 7))
        self.squares[(4, 7)] = Pieces.King(Pieces.Color.black, (4, 7))
        self.squares[(5, 7)] = Pieces.Bishop(Pieces.Color.black, (5, 7))
        self.squares[(6, 7)] = Pieces.Knight(Pieces.Color.black, (6, 7))
        self.squares[(7, 7)] = Pieces.Rook(Pieces.Color.black, (7, 7))
        self.game_over = False
        self.white_to_move = True
        self.move_count = 1

    def get_set_of_pieces(self, color):
        pieces = []
        for square in self.squares.values():
            if square and square.color == Pieces.Color.white:
                pieces.append(square)
        return pieces

    def legal_moves(self, piece):
        legal_squares = []
        for square in self.squares.keys():
            if piece.color == Pieces.Color.black:
                temp = (7 - square[0], 7 - square[1])
            else:
                temp = square
                # if the move is legal with no other pieces on the board
            if piece.evaluate_move(temp) != "Illegal Move Attempted" and piece.evaluate_move(temp) != "No Move was Made":
                if piece.__class__.__name__ == 'Pawn':
                    # special cases for pawns since they're weird
                    if piece.evaluate_move(temp)[0] == "Attempted to Capture":
                        if self.squares[temp] and self.squares[temp].color != piece.color:
                            legal_squares.append(temp)

                    else:
                        # if there are no obstructing pieces in the path of the move
                        no_obstruction = True
                        for intermediates in piece.evaluate_move(temp)[1]:
                            if self.squares[intermediates] is not None:
                                no_obstruction = False
                                break
                        # if the destination square is not occupied by a piece
                        if no_obstruction:
                            if not self.squares[temp] or self.squares[temp].color != piece.color:
                                # it's legal!
                                legal_squares.append(temp)
                else:
                    # if there are no obstructing pieces in the path of the move
                    no_obstruction = True
                    for intermediates in piece.evaluate_move(temp)[1]:
                        if self.squares[intermediates] is not None:
                            no_obstruction = False
                            break

                    # if the destination square is not occupied by a friendly piece
                    if no_obstruction:
                        if not self.squares[temp] or self.squares[temp].color != piece.color:
                            # it's legal!
                            legal_squares.append(temp)
        return legal_squares
