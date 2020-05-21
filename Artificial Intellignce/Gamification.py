import random
import math

up    = [3 ,4 ,5 ,6 ,7 ,8]
down  = [0 ,1 ,2 ,3 ,4 ,5]
right = [0 ,1 ,3 ,4 ,6 ,7]
left  = [1 ,2 ,4 ,5 ,7 ,8]

def intialize():
    board = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]
    for i in range(9):
        board[i] = random.randrange(-1, 2)
    return board

def printBoard(board):
    print("\n "+ str(board[0])+ " | "+ str(board[1])+ " | "+ str(board[2]))
    print("_____________")
    print(" "+ str(board[3])+ " | "+ str(board[4])+ " | "+ str(board[5]))
    print("_____________")
    print(" "+ str(board[6])+ " | "+ str(board[7])+ " | "+ str(board[8])+ "\n")

def isWin(board ,goal):
    for i in board:
        if i == goal:
            return True
    return False

def minThreeBoards(board, PrePosition) :
    arr1, arr2, arr3 = list(board), list(board), list(board)
    arr1[PrePosition] = -1
    arr2[PrePosition] = 0
    arr3[PrePosition] = 1
    boards = [ arr1, arr2, arr3]
    return boards

def PrePosition(board, curPosition):
    boards = []
    #UP
    if curPosition in up:   boards.append(curPosition)
    #DOWN
    if curPosition in down: boards.append(curPosition)
    #RIGHT
    if curPosition in right:boards.append(curPosition)
    #LEFT
    if curPosition in left: boards.append(curPosition)
    return boards

def possibleMoves(board, curPosition):
    boards = []
    arr1, arr2, arr3, arr4 = list(board), list(board), list(board), list(board)
    #UP
    if curPosition in up:
        arr1[curPosition-3] = arr1[curPosition-3] + arr1[curPosition] 
        boards.append(arr1)
    #DOWN
    if curPosition in down:
        arr2[curPosition+3] = arr2[curPosition+3] + arr2[curPosition] 
        boards.append(arr2)
    #RIGHT
    if curPosition in right:
        arr3[curPosition+1] = arr3[curPosition+1] + arr3[curPosition] 
        boards.append(arr3)
    #LEFT
    if curPosition in left:
        arr4[curPosition-1] = arr4[curPosition-1] + arr4[curPosition] 
        boards.append(arr4)
    return boards


def alphabeta(board, curPosition, PrePosition, level, alpha, beta, maximizingPlayer, score) :
    if isWin(board, goal):
        return score

    if(level > moves):
        return score

    if maximizingPlayer :
        value = -1*math.inf
        boards = possibleMoves(board, curPosition)
        for i in boards:
            value = max(value, alphabeta(board, curPosition, PrePosition, level, alpha, beta, False, score))
            alpha = max(alpha, value)
            if alpha >= beta :
                break
        return value
    else :
        value = math.inf
        boards = minThreeBoards(board, PrePosition)
        for i in range(3):
            value = min(value, alphabeta(boards[i], curPosition, PrePosition, level, alpha, beta, True, score))
            beta = min(beta, value)
            if alpha >= beta :
                break
        return value

if __name__ == "__main__": 
    goal = input("Goal = ")
    moves = input("Maximum number of moves = ")
    print(intialize())
    print(goal)
    print(moves)
    print(minThreeBoards(intialize(), 6))
    print(intialize())
    printBoard(intialize())
    original = intialize()
    #alphabeta(original, 6, -1, 1, -1*math.inf, math.inf, True, original[6])
