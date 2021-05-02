class Node(object):
    #base class for all boards
    def __init__(self, board, prev, f ,g):
        self.board = board #current game board
        self.prev = prev #index of last element in the path
        self.f = f # f value of current game board
        self.g = g

    def goalStateFound(self):
        row3 = list(self.board[2])
        if (row3[4] == row3[5]):
            if (row3[4] == 'X'):
                return True
        else:
            return False

def rushhour(heuristic, rawInput):
    path = AStarSearch(heuristic, rawInput)
    if (path != []):
        totalStatesExplored = path.pop()
        path.reverse()
        for i in range(len(path)):
            printBoard(path[i])
            print("\n")
        print("Total Moves: ", len(path) - 1) # initial state does not count 
        print("Total States Explored: ", totalStatesExplored )
    else:
        print("could not find solution")

# AStarSearch Algorithm
def AStarSearch(heuristic, board):
    #first input setup
    stateExploredCounter = 0
    currLevel = 0
    f = calculateFn(heuristic, board, currLevel)
    currExploring = Node(board, None, f, currLevel)
    open = [currExploring]
    closed = []

    while(open != []):
        # each new node set up         
        currExploring = open.pop(0)
        currLevel = currExploring.g + 1
        stateExploredCounter += 1
        closed.append(currExploring)
        
        # goal is found, traverse path via and append state explored count to return
        if(currExploring.goalStateFound()):
            path = []
            path.append(currExploring.board)
            while(currExploring.prev != None):
                currExploring = currExploring.prev
                path.append(currExploring.board) 
            path.append(stateExploredCounter)
            return path
        #goal not found search through new possible states
        else:
            newStates = generateNewStates(currExploring, heuristic, currLevel)
            for i in range(len(newStates)):
                inClosed = False
                inOpen = False
                for j in range(len(closed)):
                    if (newStates[i].board == closed[j].board):
                        inClosed = True
                for k in range(len(open)):
                    if(newStates[i].board == open[k].board):
                        inOpen = True
                if (not inClosed and not inOpen):
                    open.append(newStates[i])
        #sort open by f(n)
        for i in range(len(open)):
            open.sort(key = sendKeyToSort)
    return [] 

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

# This heuristic counts the number of blocks in front of X and the number of steps X has to take to reach the end
    # if we've reached goal state h(n) = 0
    # else  h(n) = blockingObstacles + spacesUntilXReachesGoal + 1
# This heuristic is similar to the blocking heuristic but also takes into account the number of final steps needed. 
# This is improving the blocking heuristic because a state where X is closer to the goal is objectively better than 
# a state farther from the goal. 
# This heuristic is admissable because the same steps would have to be taken into account for the blocking heuristic 
# and the blocking heuristic is admissable.
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
            whereIsX = j + 1
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

#sort with a key for open
def sendKeyToSort(board):
    return board.f

# uses the heuristic and g to find what f(n) is 
def calculateFn(heuristic, currBoard, g):
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
    # find all instances in board != '-' and add to list with coordinate
    for i in range(6):
        currRow = board[i]
        for j in range(6):
            if (currRow[j] != '-'):
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
    return obstaclesWithCoordinates
    
#default generate all states with game board (will use horizontal and vertical state generators)
def generateNewStates(board,heurisitic, g):
    newStates = []
    verticalStates = []
    horizontalStates = []
    
    obstaclesWithCoordinates = findAllCarsAndTrucks(board.board)
    for i in range(len(obstaclesWithCoordinates)):
        x1 = obstaclesWithCoordinates[i][1][0] # xcoordinate of first instance
        x2 = obstaclesWithCoordinates[i][2][0] # x coordinate of second instance
        if (x1 ==  x2): # vertical
            verticalStatesTemp = generateVerticalStates(board.board, obstaclesWithCoordinates[i])
            for j in range(len(verticalStatesTemp)):
                verticalStates.append(verticalStatesTemp[j])
        else: #horizontal
            horizontalStatesTemp = generateHorizontalStates(board.board,obstaclesWithCoordinates[i])
            for j in range(len(horizontalStatesTemp)):
                horizontalStates.append(horizontalStatesTemp[j])
    
    # make each new state into correct format for A* search
    allStates = horizontalStates + verticalStates
    for i in range(len(allStates)):
        newStates.append(createNode(allStates[i],heurisitic,g,board)) 
    return newStates

#formating for open and closed in AStar
def createNode(state, heuristic, g, prev):
    f = calculateFn(heuristic, state, g)
    valToReturn = Node(state,prev,f,g)
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
    if (posX == 5):
        return None
    rowToChange = currBoard[posY] 
    charLabel = rowToChange[posX]
    if(rowToChange[posX + 1] == '-'):
        for i in range(len(rowToChange) - 2, -1, -1): # decrementing loop
            if (rowToChange[i] == charLabel):
                rowToChange = swap(rowToChange, i, i + 1)
        currBoard[posY] = rowToChange
    else:
        return None
    return currBoard

# returns slide one step to the left with the X and Y position of leftmost element
def slideLeft(posX, posY, board):
    currBoard = board.copy()
    if (posX == 0):
        return None
    rowToChange = currBoard[posY] 
    charLabel = rowToChange[posX]
    if(rowToChange[posX - 1] == '-'):
        for i in range(len(rowToChange)):
            if (rowToChange[i] == charLabel):
                rowToChange = swap(rowToChange, i - 1, i)
        currBoard[posY] = rowToChange
    else:
        return None
    return currBoard


# returns slide up one step with the X and Y position of uppermost element
def slideUp(posX, posY, board):
    currBoard = board.copy()
    if (posY == 0):
        return
    rowFirstEle = currBoard[posY] 
    charLabel = rowFirstEle[posX]
    #error handling
    if (currBoard[posY - 1][posX] == '-'):
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
    else:
        return None
    return currBoard

# returns slide down one step with the X and Y position of lowermost element
def slideDown(posX, posY, board):
    currBoard = board.copy()
    if (posY == 5):
        return
    rowFirstEle = currBoard[posY] 
    charLabel = rowFirstEle[posX]
    #error handling
    if (currBoard[posY + 1][posX] == '-'):
        for i in range(5, -1, -1): # changed second value to -1
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
    else:
        return None
    return currBoard 