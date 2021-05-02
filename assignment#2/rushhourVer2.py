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
    # numberOfCarsAndTrucks(rawInput)
    AStarSearch(heuristic, rawInput)
    #print result here
    
def caculateFn(heuristic, currBoard, g):
    f = 0
    if (heuristic == 0):
        f = blockingHeuristic(currBoard) + g 
    if (heuristic == 1):
        f = selfMadeHeuristic(currBoard) + g
    return f 

def printBoard(self):
        for i in board:
            print(i)

def swap(curr, pos1, pos2):
    curr = list(curr)
    curr[pos1], curr[pos2] = curr[pos2], curr[pos1]
    print(curr)
    return ''.join(curr)

def numberOfCarsAndTrucks(board):
    obstacles = []
    moveableObstacles = []
    for i in range(6):
        currRow = board[i]
        for j in range(6):
            print(currRow[j], " is currRow[j]")
            if (currRow[j] != 'X' and currRow[j] != '-'):
                if (currRow[j] not in obstacles):
                    obstacles.append(currRow[j]) 
    numberOfObstacles = len(obstacles)

                
    # find number of cars
    # find which cars can move
    # generate states for moveable cars

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
# this heuristic must be admissable as well 
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

def AStarSearch(heuristic, board):
    stateExploredCounter = 0
    currLevel = 0
    f = caculateFn(heuristic, board, currLevel)
    currExploring = Node(board, None, f)
    open = [currExploring]
    closed = []
    print(open[0].f)
    while(open != []):
        print(currLevel, "level counter")
        currExploring = open.pop(0)
        # put currExploring in closed
        closed.append(currExploring)
        if(currExploring.goalStateFound()):
            print("GOOOOOOOOOOOOOOOOOOOOAAAAAAAAAAALLLLLLLLLLLLL")
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
        currLevel += 1
    return ## path