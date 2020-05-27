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
    print(" "+ str(board[0])+ " | "+ str(board[1])+ " | "+ str(board[2]))
    print("_____________")
    print(" "+ str(board[3])+ " | "+ str(board[4])+ " | "+ str(board[5]))
    print("_____________")
    print(" "+ str(board[6])+ " | "+ str(board[7])+ " | "+ str(board[8]))

def minThreeBoards(board, PrePosition) :
    arr1, arr2, arr3 = list(board), list(board), list(board)
    arr1[PrePosition] = -1
    arr2[PrePosition] = 0
    arr3[PrePosition] = 1
    boards = [ arr1, arr2, arr3]
    return boards

def knowMove(pre,cur):
    if pre-cur == 3 :
        return "up"
    elif pre-cur == -3 :
        return "down"
    elif pre-cur == -1 :
        return "right"
    elif pre-cur == 1 :
        return "left"

def newPositions(board, curPosition):
    boards = []
    #UP
    if curPosition in up:   
        boards.append(curPosition-3)
    #DOWN
    if curPosition in down: 
        boards.append(curPosition+3)
    #RIGHT
    if curPosition in right:
        boards.append(curPosition+1)
    #LEFT
    if curPosition in left: 
        boards.append(curPosition-1)
    return boards

def move(board, curPosition, move):
    if move == 'up':
        arr = list(board)
        arr[curPosition-3] = arr[curPosition-3] + arr[curPosition]
        return arr
    elif move == 'down':
        arr = list(board)
        arr[curPosition+3] = arr[curPosition+3] + arr[curPosition] 
        return arr
    elif move == 'right':
        arr = list(board)
        arr[curPosition+1] = arr[curPosition+1] + arr[curPosition] 
        return arr
    elif move == 'left':
        arr = list(board)
        arr[curPosition-1] = arr[curPosition-1] + arr[curPosition] 
        return arr

def newPos(curPosition, move):
    if move == 'up':
        next = curPosition-3
        return next
    elif move == 'down':
        next = curPosition+3
        return next
    elif move == 'right':
        next = curPosition+1
        return next
    elif move == 'left':
        next = curPosition-1
        return next

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


def alphabeta(board, curPosition, PrePosition, level, alpha, beta, maximizingPlayer, numberMoves, move) :
    returnList = []
    #TESTING
    #printBoard(board)
    #print(str(curPosition)+" "+ str(PrePosition)+" "+ str(level)+" "+ str(alpha)+" "+ str(beta)+" "+ str(maximizingPlayer))

    if  level >= numberMoves:
        #print("Winning retuned with value of " + str(board[curPosition]) + " " + move)
        returnList = [str(board[curPosition]) , move]
        return returnList
    
    if maximizingPlayer :
        value = -1*math.inf
        new = list(newPositions(board, curPosition))
        boards = list(possibleMoves(board, curPosition))
        #print("MAX")
        bestMove = " "
        #print(boards)
        for i in range(len(boards)):
            if level == 0:
                temp = value
                newVal = alphabeta(boards[i], new[i], curPosition, level+1, alpha, beta, False, numberMoves, knowMove(curPosition, new[i]))
                value = max(value, int(newVal[0]))
                if temp != value :
                    bestMove = knowMove(curPosition, new[i])
            else :
                newVal = alphabeta(boards[i], new[i], curPosition, level+1, alpha, beta, False, numberMoves, move)
                value = max(value, int(newVal[0]))
            alpha = max(alpha, value)
            if alpha >= beta :
                break
        if level == 0:
            #print("\nbest move with value of " + str(value) + " " + bestMove) 
            returnList = [str(value) , bestMove]
            return returnList
        #return value
        else :
            returnList = [str(value) , move]
            return returnList
    else :
        value = math.inf
        boards = list(minThreeBoards(board, PrePosition))
        #print("MIN")
        #print(boards)
        for i in range(3):
            newVal = alphabeta(boards[i], curPosition, PrePosition, level, alpha, beta, True, numberMoves, move)
            value = min(value, int(newVal[0]))
            beta = min(beta, value)
            if alpha >= beta :
                break
        #return value
        returnList = [str(value) , move]
        return returnList

def game(board, numberMoves):
    print("\nYour board :")
    printBoard(board)
    pre = -1
    position = 6
    temp = numberMoves
    for i in range(temp):
        if board[position] >= goal :
            print("\nWINNING in " + str(i+1) + " moves with score of " + str(board[position]))
            print("Input :-\n   Number of moves : " + str(moves) + "\n   Goal : " + str(goal) + "\n")
            break
        arr =  alphabeta(board, position, pre, 0, -1*math.inf, math.inf, True, numberMoves, " ")
        print("\nbest move for this state to take " + arr[1] + " in move number " + str(i+1))
        newBoard = move(board, position,arr[1])
        board = newBoard
        pre = position
        position = newPos(position,arr[1])
        newBoard[pre] = random.randrange(-1, 2)
        printBoard(newBoard)
        numberMoves = numberMoves-1
        if i == temp-1 : 
            if board[position] >= goal :
                print("\nWINNING in " + str(i+1) + " moves with score of " + str(board[position]) + "\n")
                print("Input :-\n   Number of moves : " + str(moves) + "\n   Goal : " + str(goal) + "\n")
            else :
                print("\nLOSING with score of " + str(board[position]) + "\n")
                print("Input :-\n   Number of moves : " + str(moves) + "\n   Goal : " + str(goal) + "\n")
            break

if __name__ == "__main__": 
    goal = int(input("Goal = "))
    moves = int(input("Maximum number of moves = "))
    game([1,-1,0,1,0,1,0,1,-1],moves)
    #game([-1,1,1,-1,-1,1,1,1,1],moves)
    '''
    if you want to make the all the board values initialized with random values call 'intialize()' function:
    EX:
    game(intialize(),moves)
    '''
