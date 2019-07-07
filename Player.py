import Board, Pieces


class Player:
    """
    Players have a board and color. p1(board1, white), p2(board1, black) = two players playing
    """
    def __init__(self, board, color):
        self.board = board
        self.color = color

    def make_move(self):
        piece_not_selected = True
        while piece_not_selected:
            coordinate = input("Enter the coordinates of the piece you want to move")
            for piece in self.board.get_set_of_pieces(self.color):
                if piece.position == coordinate:
                    piece_not_selected = False
                    break

        piece_not_placed = True
        while piece_not_placed:
            coordinate = input("Enter the coordinates of the where to move the piece")
            for pos in self.board.legal_moves(self.board.squares[coordinate]):
                if pos == coordinate.strip():
                    piece_not_placed = False
                    break

p1 = Player(Board.Board(), Pieces.Color.white)
p1.make_move()
