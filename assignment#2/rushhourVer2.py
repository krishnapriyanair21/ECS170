class Node(object):
    #base class for all boards
    def __init__(self, board, prev, f):
        self.board = board
        self.prev = prev
        self.f = f

    def goalStateFound(self):
        row3 = list(self.board[2])
        if (row3[4] == row3[5]):
            if (row3[4] == 'X'):
                return True
        else:
            return false

def rushhour(heuristic, rawInput):
    printBoard(rawInput)
    generateNewStates(rawInput, heuristic,0)
    # AStarSearch(heuristic, rawInput)
    #print result here

def AStarSearch(heuristic, board):
    stateExploredCounter = 0
    currLevel = 0
    f = caculateFn(heuristic, board, currLevel)
    currExploring = Node(board, None, f)
    open = [currExploring]
    closed = []
    while(open != []):
        print(currLevel, "level counter")
        currExploring = open.pop(0)
        # put currExploring in closed
        closed.append(currExploring)
        if(currExploring.goalStateFound()):
            print("GOOOOOOOOOOOOOOOOOOOOAAAAAAAAAAALLLLLLLLLLLLL")
            #create new var path[]
            # reverse from current to start via prev
        else:
            newStates = generateNewStates(currExploring,heurisitic,currLevel)
        # loop next states
            for i in range(len(newStates)):
                if (newStates[i] in closed):
                    continue
                else:

            # expand all possible states from currExploring (IN NEW VARS)
            # if in closed continue
            # ELSE
                # generate heuristic
                # place next states from currExploring in open
            #increment stateExploredCounter
        #sort open by f(n)
        currLevel += 1
    return 

#counts the number of different chars != X in row 3 starting from first X
# heuristic == 0
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
# this heuristic must be admissable as well
# heuristic == 1
def selfMadeHeuristic(board):
    traverseXRow = list(board[2])
    blocksInRow = []
    blocksCounter = 0
    whereIsX = 0
    XToGoal = 0

    #blocking heuristic
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

    #define return value with added X movements
    XToGoal = (6 - j - 2) # 6-j is first X and there are 2 extra spots
    h = XToGoal + blocksCounter + 1 ## one plus the number of cars plus how many moves until exit
    if (blocksCounter == 0):
        return 0 ## h(n) = 0
    else:
        return h

# uses the heuristic and g to find what f(n) is 
def caculateFn(heuristic, currBoard, g):
    f = 0
    if (heuristic == 0):
        f = blockingHeuristic(currBoard) + g
    if (heuristic == 1):
        f = selfMadeHeuristic(currBoard) + g
    return f

# prints board in correct format
def printBoard(board):
        for i in board:
            print(i)

#swap two elements in a list
def swap(curr, pos1, pos2):
    curr = list(curr)
    curr[pos1], curr[pos2] = curr[pos2], curr[pos1]
    return ''.join(curr)

#finds all the cars and trucks on the board and returns a list of lists with the char and coordinates
def findAllCarsAndTrucks(board):
    allObstacles = []
    visitedEle = []
    currEle = []
    obstaclesWithCoordinates = []
    
    # find all instances in board != 'X' or '-' and add to list with coordinate
    for i in range(6):
        currRow = board[i]
        for j in range(6):
            if (currRow[j] != 'X' and currRow[j] != '-'):
                if (currRow[j] not in allObstacles):
                    allObstacles.append([currRow[j],(j,i)]) #add each instance w/ (x,y) coordinate
                    if(currRow[j] not in visitedEle):
                        visitedEle.append(currRow[j])
    allObstacles.sort()
    visitedEle.sort()    
    # create new list with ('CHAR', (set of coordinates)) 
    for i in range(len(visitedEle)):
        currEle = []
        currEle.append(visitedEle[i])
        for j in range(len(allObstacles)):
            if (visitedEle[i] == allObstacles[j][0]):
                currEle.append(allObstacles[j][1])
        obstaclesWithCoordinates.append(currEle)
    print(obstaclesWithCoordinates)
    return obstaclesWithCoordinates
    
#default generate all states with game board (will use horizontal and vertical state generators)
def generateNewStates(board,heurisitic,g):
    newStates = []
    verticalStates = []
    horizontalStates = []
    obstaclesWithCoordinates = findAllCarsAndTrucks(board)
    for i in range(len(obstaclesWithCoordinates)):
        x1 = obstaclesWithCoordinates[i][1][0] # xcoordinate of first instance
        x2 = obstaclesWithCoordinates[i][2][0] # x coordinate of second instance
        if (x1 ==  x2): # vertical
            verticalStatesTemp = generateVerticalStates(board, obstaclesWithCoordinates[i])
            for j in range(len(verticalStatesTemp)):
                verticalStates.append(verticalStatesTemp[j])
        else: #horizontal
            horizontalStatesTemp = generateHorizontalStates(board,obstaclesWithCoordinates[i])
            for j in range(len(horizontalStatesTemp)):
                horizontalStates.append(horizontalStatesTemp[j])
    
    # make each new state into correct format for A* search
    allStates = horizontalStates + verticalStates
    for i in range(len(allStates)):
        newStates.append(createNode(allStates[i],heurisitic,g,board)) 
    return newStates

#formating for open and closed in AStar
def createNode(state, heuristic, g, prev):
    f = caculateFn(heuristic, state, g)
    valToReturn = Node(state,prev,f)
    return valToReturn

#generate new states for a specific horizontal car or truck; returns all possible states moving that obstacle
def generateHorizontalStates(board, obstacle):
    possibleStates = []
    rightX = obstacle[-1][0]
    rightY = obstacle[-1][1] 
    if(slideRight(rightX,rightY,board) != None):
        possibleStates.append(slideRight(rightX,rightY,board))
    leftX = obstacle[1][0]
    leftY = obstacle[1][1]
    if(slideLeft(leftX,leftY,board) != None):
        possibleStates.append(slideLeft(leftX,leftY,board))
    return possibleStates

#generate new states for a specific vertical car or truck; returns all possible states moving that specific obstacle
def generateVerticalStates(board, obstacle):
    possibleStates = []
    downX = obstacle[-1][0]
    downY = obstacle[-1][1] 
    if(slideDown(downX,downY,board) != None):
        possibleStates.append(slideDown(downX,downY,board))
    upX = obstacle[1][0]
    upY = obstacle[1][1]
    if(slideUp(upX,upY,board) != None):
        possibleStates.append(slideUp(upX,upY,board))
    return possibleStates

# returns slide one step to the right with the X and Y position of rightmost element
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

# returns slide one step to the left with the X and Y position of leftmost element
def slideLeft(posX, posY, board):
    currBoard = board.copy()
    if (posX == 5):
        return None
    rowToChange = currBoard[posY] 
    charLabel = rowToChange[posX]
    if(rowToChange[posX + 1] != charLabel):
        return None
    for i in range(len(rowToChange)):
        if (rowToChange[i] == charLabel):
            rowToChange = swap(rowToChange, i - 1, i)
    currBoard[posY] = rowToChange
    return currBoard


# returns slide up one step with the X and Y position of uppermost element
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

# returns slide down one step with the X and Y position of lowermost element
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