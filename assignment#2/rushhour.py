# input is a list of strings
def rushhour(heuristic, board):
    printBoard(board)

    ## Slide Tests
    print("right slide:")
    
    newBoard = slideRight(3,4,board)
    if (newBoard):
        printBoard(newBoard)
    else:
        print("none")
    print("above is returned board")
    printBoard(board)
    print("above is raw input")
    print("left slide:")
    newBoard = slideLeft(2,4,board)
    if (newBoard):
        printBoard(newBoard)
    else:
        print("none")
    print("above is returned board")
    # print("slide up")
    # slideUp(3,1,board)
    # printBoard(board)
    # print("slide down")
    # slideDown(2,2,board)

    ## Heuristic tests
    blockingHeuristic(board)
    selfMadeHeuristic(board)

def printBoard(board):
    for i in board:
        print(i)

def swap(curr, pos1, pos2):
    curr = list(curr)
    curr[pos1], curr[pos2] = curr[pos2], curr[pos1]
    print(curr)
    return ''.join(curr)

#slide one step to the right with the X and Y position of rightmost element
def slideRight(posX, posY, board):
    currBoard = board.copy()
    if (posX == 0):
        return None
    rowToChange = currBoard[posY] 
    charLabel = rowToChange[posX]
    if(rowToChange[posX - 1] != charLabel):
        return None
    for i in range(len(rowToChange) - 2, -1, -1): # decrementing loop
        if (rowToChange[i] == charLabel):
            rowToChange = swap(rowToChange, i, i + 1)
    currBoard[posY] = rowToChange
    return currBoard

#slide one step to the left with the X and Y position of leftmost element
def slideLeft(posX, posY, board):
    currBoard = board.copy()
    if (posX == 5):
        return None
    rowToChange = currBoard[posY] 
    charLabel = rowToChange[posX]
    print(charLabel, " is label")
    if(rowToChange[posX + 1] != charLabel):
        return None
    for i in range(len(rowToChange)):
        if (rowToChange[i] == charLabel):
            rowToChange = swap(rowToChange, i - 1, i)
    currBoard[posY] = rowToChange
    return currBoard


#slide up one step with the X and Y position of uppermost element
def slideUp(posX, posY, board):
    currBoard = board.copy()
    if (posY == 0):
        return
    rowFirstEle = currBoard[posY] 
    charLabel = rowFirstEle[posX]
    #error handling
    if (currBoard[posY + 1][posX] != charLabel):
        return None
    for i in range(6):
        searchString = list(currBoard[i])
        if (searchString[posX] == charLabel):
            swapUp = list(currBoard[i - 1])
            searchString[posX] = swapUp[posX]
            swapUp[posX] = charLabel
            #revert to string to place in currBoard
            swapUpStr = ''.join(swapUp)
            searchStringtoStr = ''.join(searchString)
            currBoard[i - 1] = swapUpStr
            currBoard[i] = searchStringtoStr
    return currBoard

#slide down one step with the X and Y position of lowermost element
def slideDown(posX, posY, board):
    currBoard = board.copy()
    if (posY == 5):
        return
    rowFirstEle = currBoard[posY] 
    charLabel = rowFirstEle[posX]
    #error handling
    if (currBoard[posY - 1][posX] != charLabel):
        return None
    for i in range(5, 0, -1):
        searchString = list(currBoard[i])
        if (searchString[posX] == charLabel):
            swapDown = list(currBoard[i + 1])
            searchString[posX] = swapDown[posX]
            swapDown[posX] = charLabel
            #revert to strings to place in currBoard
            swapDownStr = ''.join(swapDown)
            searchStringtoStr = ''.join(searchString)
            currBoard[i + 1] = swapDownStr
            currBoard[i] = searchStringtoStr
    return currBoard 

#counts the number of different chars != X in row 3 starting from first X
def blockingHeuristic(board):
    traverseXRow = list(board[2])
    blocksInRow = []
    blocksCounter = 0
    whereIsX = 0

    for j in range(6):
        if (traverseXRow[j] == 'X'):
            whereIsX = j
            break
    for i in range(j , 6):
        if (traverseXRow[i] != 'X'):
            if (traverseXRow[i] != '-'):
                if (traverseXRow[i] not in blocksInRow):
                    blocksInRow.append(traverseXRow[i])
                    blocksCounter += 1
    if ('-' in blocksInRow): 
        blocksCounter -= 1
    
    if (blocksCounter == 0): # check to reach goal
        return 0 ## h(n) = 0
    else:
        return (blocksCounter + 1) ## one plus the number of cars


# counts the number of blocks in front of X and the number of steps X has to take to reach the end
# if we've reached goal state h(n) = 0
# This heuristic is similar to the blocking heuristic but also takes into account the number of final steps needed
# Because these steps would have to be taken into account for the blocking heuristic and the blocking heuristic is admissable
# this heurisitic must be admissable as well 
def selfMadeHeuristic(board):
    traverseXRow = list(board[2])
    blocksInRow = []
    blocksCounter = 0
    whereIsX = 0
    XToGoal = 0

    for j in range(6):
        if (traverseXRow[j] == 'X'):
            whereIsX = j
            break
    for i in range(j , 6):
        if (traverseXRow[i] != 'X'):
            if (traverseXRow[i] != '-'):
                if (traverseXRow[i] not in blocksInRow):
                    blocksInRow.append(traverseXRow[i])
                    blocksCounter += 1
    if ('-' in blocksInRow): 
        blocksCounter -= 1
    
    #define return value
    XToGoal = (6 - j - 2) # 6-j is first X and there are 2 extra spots
    h = XToGoal + blocksCounter + 1 ## one plus the number of cars plus how many moves until exit
    if (blocksCounter == 0):
        return 0 ## h(n) = 0
    else:
        return h 

def caculateFn(heurisitic, currBoard, g):
    f = 0
    if (heuristic == 0):
        f = blockingHeuristic(currBoard) + g 
    if (heuristic == 1):
        f = selfMadeHeuristic(currBoard) + g
    return f

def AStarSearch(heurisitic, board):
    stateExploredCounter = 0
    #make tuple with board and f(n)
    #place in open 
    open = []
    closed = []
    while(open != []):
        # currExploring = pop open
        # put currExploring in closed
        # if currExploring is goal state Return path
            # reverse from current to start
        # loop next states
            # expand all possible states from currExploring (IN NEW VARS)
            # if in closed continue
            # ELSE
                # generate heuristic
                # place next states from currExploring in open 
            #increment stateExploredCounter
        #sort open by f(n)

        if(GOAL in closed):
            break