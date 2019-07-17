import pygame as p
from Game.Board import Board
from Game.Move import Move
from Engine.BoardEvaluator import evalBoard
import math
import copy
import time
from Pieces.Pawn import Pawn
from Pieces.NullPiece import NullPiece
from Game.Tile import Tile

p.init()
game = p.display.set_mode((1000, 800))

p.display.set_caption("Chess!")
clock = p.time.Clock()


selectedPiece = None
prevBoard = None
chessBoard = Board()


allTiles = []
allPieces = []
checkmate = p.USEREVENT + 1
stalemate = p.USEREVENT + 2
checkmateOccured = p.event.Event(checkmate)
stalemateOccured = p.event.Event(stalemate)



font = p.font.Font('freesansbold.ttf', 24)




def drawPieces():
    xPos = 0
    yPos = 700
    white = (238, 238, 210)
    black = (117, 149 ,86)
    highlight = (0, 255, 0)
    width = 100
    height = 100
    number = 0
    for x in range(8):
        for y in range(8):
            if y % 2 != x % 2:
                drawSquares(xPos, yPos, width, height, white)
            else:
                drawSquares(xPos, yPos, width, height, black)

            if not chessBoard.tiles[number].pieceOnTile.toString() == "-":
                image = p.image.load("./Images/" + chessBoard.tiles[number].pieceOnTile.color[0] +
                                     chessBoard.tiles[number].pieceOnTile.toString().upper() + ".png")
                image = p.transform.scale(image, (100, 100))
                allPieces.append([image, [xPos, yPos], chessBoard.tiles[number].pieceOnTile])

            xPos += 100
            number += 1
        yPos -= 100
        xPos = 0

def drawSquares(x, y, w, h, color):
    p.draw.rect(game, color, [x, y, w, h])
    allTiles.append([color, [x, y, w, h]])


def updateChessPieces():
    xPos = 0
    yPos = 700
    number = 0
    newPieces = []

    for _ in range(8):
        for _ in range(8):
            if not chessBoard.tiles[number].pieceOnTile.toString() == "-":
                img = p.image.load(
                    "./Images/" + chessBoard.tiles[number].pieceOnTile.color[0].upper() + chessBoard.tiles[
                        number].pieceOnTile.toString().upper() + ".png")
                img = p.transform.scale(img, (100, 100))
                newPieces.append([img, [xPos, yPos], chessBoard.tiles[number].pieceOnTile])
            xPos += 100
            number += 1
        xPos = 0
        yPos -= 100
    return newPieces





gameOver = False
px, py = 0, 0
drawPieces()

while not gameOver:

    for event in p.event.get():
        if event.type == p.QUIT:
            gameOver = True
            p.quit()
            quit()



        if event.type == checkmate:
            checkmateText1 = font.render(("Checkmate!"), True, (143, 32, 67))
            checkmateText2 = font.render((str(chessBoard.previousPlayer) + " Wins!"), True, (143, 32, 67))
            checkmateRect1 = checkmateText1.get_rect()
            checkmateRect2 = checkmateText2.get_rect()
            checkmateRect1.center = (900, 100)
            checkmateRect2.center = (900, 120)
            game.blit(checkmateText1, checkmateRect1)
            game.blit(checkmateText2, checkmateRect2)
            #p.display.update()
            #p.time.wait(1000)
            #p.quit()
            #quit()


        if event.type == stalemate:
            stalemateText = font.render(("Stalemate!"), True, (143, 32, 67))
            stalemateRect = stalemateText.get_rect()
            stalemateRect.center = (900, 100)
            game.blit(stalemateText, stalemateRect)



        if event.type == p.MOUSEBUTTONDOWN:
            if not selectedPiece:
                mx, my = p.mouse.get_pos()
                for piece in allPieces:
                    if piece[1][0] < mx < (piece[1][0] + 100) and piece[1][1] < my < (piece[1][1] + 100):
                        if piece[2].color == chessBoard.currentPlayer:
                            selectedPiece = piece
                            px = piece[1][0]
                            py = piece[1][1]
                            break




        if event.type == p.MOUSEMOTION and selectedPiece:
            mx, my = event.pos
            if mx < 770:
                selectedPiece[1][0] = mx - 50
            selectedPiece[1][1] = my - 50



        if event.type == p.MOUSEBUTTONUP and selectedPiece:
            theMove = None
            if selectedPiece:
                legal = False
                xCoor = int(math.floor((selectedPiece[1][0] + 50) / 100.0) * 100)
                yCoor = 700 - int(math.floor((selectedPiece[1][1] + 50) / 100.0) * 100)
                for desiredMove in selectedPiece[2].legalMoves(chessBoard, prevBoard):
                    if desiredMove == xCoor / 100 + 8 * yCoor /100:
                        theMove = desiredMove
                        legal = True
                        selectedPiece[1][0] = xCoor
                        selectedPiece[1][1] = 700 - yCoor
                        break


                # drawPieces()

                hold = selectedPiece[2].position
                if legal:
                    move = Move(chessBoard, selectedPiece[2], theMove)
                    newBoard = move.makeMove()
                    selectedPiece[2].position = theMove

                friendlyKing = None
                for tile in chessBoard.tiles.values():
                    if (tile.pieceOnTile.toString() == "K" and chessBoard.currentPlayer == "Black") or (
                            tile.pieceOnTile.toString() == "k" and chessBoard.currentPlayer == "White"):
                        friendlyKing = tile.pieceOnTile
                        break
                # print("Current Turn:",chessBoard.currentPlayer)
                # print("Move is Legal:", legal)
                # print("Move results in friendly king being in check:", friendlyKing.inCheck(newBoard, chessBoard))
                # newBoard.printBoard()
                if not legal or (friendlyKing.inCheck(newBoard, chessBoard)):
                    selectedPiece[1][0] = px
                    selectedPiece[1][1] = py
                    selectedPiece[2].position = hold
                else:
                    prevBoard = copy.deepcopy(chessBoard)
                    chessBoard = copy.deepcopy(newBoard)
                    allPieces = updateChessPieces()
                    print(evalBoard(chessBoard))
                    print(chessBoard.moveCounter)


                    #post selection
                    if chessBoard.currentPlayer == "White":
                        chessBoard.currentPlayer = "Black"
                        chessBoard.previousPlayer = "White"
                    else:
                        chessBoard.currentPlayer = "White"
                        chessBoard.previousPlayer = "Black"
                        chessBoard.moveCounter += 1

                    for piece in allPieces:
                        if piece[2].color == chessBoard.currentPlayer and piece[2].toString().lower() == "k":
                            if piece[2].inCheck(chessBoard, prevBoard):
                                print("Check")
                                if piece[2].inCheckmate(chessBoard, prevBoard):
                                    p.event.post(checkmateOccured)
                                    break

                            elif piece[2].inStalemate(chessBoard, prevBoard):
                                p.event.post(stalemateOccured)
                                break
                            break

                selectedPiece = None

    for tile in allTiles:
        p.draw.rect(game, tile[0], tile[1])
    for img in allPieces:
        game.blit(img[0], img[1])
    p.display.update()
    clock.tick(60)


