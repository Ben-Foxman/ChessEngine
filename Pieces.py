from enum import Enum


class Color(Enum):
    # Enum for the two colors
    white = 'White'
    black = 'Black'

class Piece:
    # color= white or black, value= piece value, position= current position on board as a tuple
    # captured= boolean to determine if a piece is on the board
    def __init__(self, color, position, value, captured=False):
        self.color = color
        self.value = value
        self.position = position
        self.captured = captured

    # a string representation of a attempted move + array of all the intermediate squares which must be checked
    def evaluate_move(self, destination):
        if destination == self.position:
            return "No Move was Made"


class Pawn(Piece):
    # Class representing a pawn
    def __init__(self, color, position, moved=False):
        super().__init__(color, position, value=1, captured=False)
        self.moved = moved

    def evaluate_move(self, destination):
        if super().evaluate_move(destination) == "No Move was Made":
            return "No Move was Made"
        if self.color == Color.white:
            # if the pawn hasn't moved yet
            if not self.moved:

                # option to move two squares up
                if destination[1] - self.position[1] == 2 and destination[0] == self.position[0]:
                    moves = [(self.position[0], self.position[1] + 1)]
                    return "Attempted to Move Two Squares Up", moves

            # option to only move one square up
            if destination[1] - self.position[1] == 1 and destination[0] == self.position[0]:
                return "Attempted To Move One Square Up", []

            # option to capture
            if destination[1] - self.position[1] == 1 and abs(destination[0] - self.position[0]) == 1:
                return "Attempted to Capture", []

        else:
            if not self.moved:

                # option to move two squares up
                if self.position[1] - destination[1] == 2 and destination[0] == self.position[0]:
                    moves = [(self.position[0], self.position[1] - 1)]
                    return "Attempted to Move Two Squares Up", moves

            # option to only move one square up
            if self.position[1] - destination[1] == 1 and destination[0] == self.position[0]:
                return "Attempted To Move One Square Up", []

            # option to capture
            if self.position[1] - destination[1] == 1 and abs(destination[0] - self.position[0]) == 1:
                return "Attempted to Capture", []


        # finally, an illegal move is being attempted
        return "Illegal Move Attempted"


class Knight(Piece):
    # Class representing a knight
    def __init__(self, color, position):
        super().__init__(color, position, value=3, captured=False)

    def evaluate_move(self, destination):
        if super().evaluate_move(destination) == "No Move was Made":
            return "No Move was Made"

        # Knights Move in L's
        if abs(destination[1] - self.position[1]) + abs(destination[0] - self.position[0]) == 3:
            if abs(destination[1] - self.position[1]) > 0 < abs(destination[0] - self.position[0]):
                return "Legal Move Attempted", []
        return "Illegal Move Attempted"


class Bishop(Piece):
    # Class representing a bishop
    def __init__(self, color, position):
        super().__init__(color, position, value=3.25, captured=False)

    def evaluate_move(self, destination):
        if super().evaluate_move(destination) == "No Move was Made":
            return "No Move was Made"

        # bishops move diagonally
        if abs(destination[1] - self.position[1]) == abs(destination[0] - self.position[0]):
            if destination[1] > self.position[1] and destination[0] > self.position[0]:
                moves = [(self.position[0] + x, self.position[1] + x) for x in range(1, destination[0] - self.position[0])]
            elif destination[0] > self.position[0]:
                moves = [(self.position[0] + x, self.position[1] - x) for x in range(1, destination[0] - self.position[0])]
            elif destination[1] > self.position[1]:
                moves = [(self.position[0] - x, self.position[1] + x) for x in range(1, self.position[0] - destination[0])]
            else:
                moves = [(self.position[0] - x, self.position[1] - x) for x in range(1, self.position[0] - destination[0])]
            return "Legal Move Attempted", moves
        return "Illegal Move Attempted"


class Rook(Piece):
    # Class representing a rook
    def __init__(self, color, position):
        super().__init__(color, position, value=5, captured=False)

    def evaluate_move(self, destination):
        if super().evaluate_move(destination) == "No Move was Made":
            return "No Move was Made"

        # rooks move is straight lines
        if destination[1] == self.position[1]:
            if destination[0] > self.position[0]:
                moves = [(self.position[0] + x, self.position[1]) for x in range(1, destination[0] - self.position[0])]
            else:
                moves = [(self.position[0] - x, self.position[1]) for x in range(1, self.position[0] - destination[0])]
            return "Legal Move Attempted", moves
        elif destination[0] == self.position[0]:
            if destination[1] > self.position[1]:
                moves = [(self.position[0], self.position[1] + x) for x in range(1, destination[1] - self.position[1])]
            else:
                moves = [(self.position[0], self.position[1] - x) for x in range(1, self.position[1] - destination[1])]
            return "Legal Move Attempted", moves
        return "Illegal Move Attempted"


class Queen(Piece):
    # Class representing a queen
    def __init__(self, color, position):
        super().__init__(color, position, value=9, captured=False)

    def evaluate_move(self, destination):
        if super().evaluate_move(destination) == "No Move was Made":
            return "No Move was Made"

        # queen = rook + bishop
        if destination[1] == self.position[1]:
            if destination[0] > self.position[0]:
                moves = [(self.position[0] + x, self.position[1]) for x in range(1, destination[0] - self.position[0])]
            else:
                moves = [(self.position[0] - x, self.position[1]) for x in range(1, self.position[0] - destination[0])]
            return "Legal Move Attempted", moves
        elif destination[0] == self.position[0]:
            if destination[1] > self.position[1]:
                moves = [(self.position[0], self.position[1] + x) for x in range(1, destination[1] - self.position[1])]
            else:
                moves = [(self.position[0], self.position[1] - x) for x in range(1, self.position[1] - destination[1])]
            return "Legal Move Attempted", moves
        if abs(destination[1] - self.position[1]) == abs(destination[0] - self.position[0]):
            moves = []
            if destination[1] > self.position[1] and destination[0] > self.position[0]:
                moves = [(self.position[0] + x, self.position[1] + x) for x in
                         range(1, destination[0] - self.position[0])]
            elif destination[0] > self.position[0]:
                moves = [(self.position[0] + x, self.position[1] - x) for x in
                         range(1, destination[0] - self.position[0])]
            elif destination[1] > self.position[1]:
                moves = [(self.position[0] - x, self.position[1] + x) for x in
                         range(1, self.position[0] - destination[0])]
            else:
                moves = [(self.position[0] - x, self.position[1] - x) for x in
                         range(1, self.position[0] - destination[0])]
            return "Legal Move Attempted", moves
        return "Illegal Move Attempted"


class King(Piece):
    # Class representing a king
    def __init__(self, color, position):
        super().__init__(color, position, value=50, captured=False)

    def evaluate_move(self, destination):
        super().evaluate_move(destination)

        # king = all adjacent squares
        if abs(destination[1] - self.position[1]) < 2 > abs(destination[0] - self.position[0]):
            return "Legal Move Attempted", []
        return "Illegal Move Attempted"
