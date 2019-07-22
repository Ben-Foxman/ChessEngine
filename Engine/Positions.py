from Game.Move import Move
from Game.Board import Board
from Game.Tile import Tile
from Engine.BoardEvaluator import newEvaluation
from Pieces.Pawn import Pawn
from Pieces.NullPiece import NullPiece
from Pieces.Knight import Knight
import time
import copy


# position = position of the board
# value = evaluation of the board
# layer = half-moves from initial node
# parent = parent node
import math

class Node:
    def __init__(self, position, max):
        self.children = []
        self.max = max
        self.position = position
        self.value = None

    def addChild(self, child):
        self.children.append(child)

    def toString(self):
        self.position.printBoard()
        return self.value

def assignValues(node):
    for child in node.children:
        if node.value == None:
            assignValues(child)
    if node.children:
        if node.max: # children are members of minimize layer:
            node.value = math.inf
            for child in node.children:
                if child.value < node.value:
                    node.value = child.value
        else: # children are members of maximize layer:
            node.value = -math.inf
            for child in node.children:
                if child.value > node.value:
                    node.value = child.value
    return node.value

nodes = {}
x = 0
def generateChildren(node):
    x = 0
    pieces = node.position.allFriendlyPieces()
    for piece in pieces:
        for move in piece.legalMoves(node.position):
            m = Move(node.position, piece, move)
            newBoard = copy.deepcopy(m.makeMove())
            for tile in newBoard.tiles.values():
                if move == tile.coordinate:
                    tile.pieceOnTile.position = copy.deepcopy(piece)
                    tile.pieceOnTile.position = move

                    break
            if node.position.currentPlayer == "White":
                newBoard.currentPlayer = "Black"
                newBoard.prevBoard = node.position
                newBoard.prevBoard.currentPlayer = "White"
                newNode = Node(newBoard, False)
                node.addChild(newNode)
            else:
                newBoard.currentPlayer = "White"
                newBoard.prevBoard = node.position
                newBoard.prevBoard.currentPlayer = "Black"
                newBoard.moveCounter += 1
                newNode = Node(newBoard, True)
                node.addChild(newNode)




def generateTree(node, depth):
    if depth == 0:
        if node in nodes.keys():
            print("yes")
            node.value = nodes[node]
        else:
            node.value = newEvaluation(node.position)
            nodes[node] = node.value
        # del node.position
        return
    generateChildren(node)
    for child in node.children:
            generateTree(child, depth - 1)


def getBestMove(node, depth):
    generateTree(node, depth)
    assignValues(node)
    bestMove = [None, None]
    for child in node.children:
        if node.max:
            if not bestMove[1] or child.value > bestMove[1]:
                bestMove[0] = child.position
                bestMove[1] = child.value
        else:
            if not bestMove[1] or child.value < bestMove[1]:
                bestMove[0] = child.position
                bestMove[1] = child.value
    # print(len(nodes))
    return bestMove

def getNewBoard(board):
    if board.currentPlayer == "White":
        node = Node(board, True)
    else:
        node = Node(board, False)
    # node.toString()
    x = getBestMove(node, 1)
    newBoard = x[0]
    return newBoard

#testing

# b = BoardEvaluator(b)

b = Board()
b.tiles[28] = (Tile(28, Pawn("White", 28)))
#b.tiles[36] = (Tile(36, Pawn("Black", 36)))
#b.tiles[52] = (Tile(52, NullPiece()))
b.tiles[12] = (Tile(12, NullPiece()))
#b.tiles[21] = (Tile(21, Knight("White", 21)))
#b.tiles[6] = (Tile(6, NullPiece()))
#b.currentPlayer = "Black"

        # newBoard.printBoard()

#resultNode = Node(b, True)
#a = getBestMove(resultNode, 1)

#x = 0
#for node in nodes.keys():
    #node.position.printBoard()

#print(len(nodes))
#a[0].printBoard()
#print()