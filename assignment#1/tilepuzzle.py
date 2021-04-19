visited = [] # recursion for DFS
#recursion depth is 15
#tests cases and running in terminal included at the bottom

def tilepuzzle (start, goal):
    startList = unList(start)
    goalList = unList(goal)
    
    # What the output should look like
    result = reverse(statesearch([startList], goalList, []))
    final = []
    
    for i in range(len(result)):  #make each element of path a list
        new = createList(result[i])
        final.append(new)
    print(final)

#find space element
def findZero(curr):
    for i in range(len(curr)):
        if curr[i] == '0':
            return i
    return -1

#syntax for input (list -> string)
def unList(input): 
    toStr0 = [str(int) for int in input[0]]
    toStr1 = [str(int) for int in input[1]]
    toStr2 = [str(int) for int in input[2]]
    list0 = "".join(toStr0)
    list1 = "".join(toStr1)
    list2 = "".join(toStr2)
    finalInput = list0 + list1 + list2
    return finalInput


#syntax for output (string -> list)
def createList(goal): # https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
    rows, cols = (3, 3)
    result = []
    ele = 0
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(int(goal[ele]))
            ele += 1
        result.append(col)
    return result

def swapPositions(curr, pos1, pos2):
    curr = list(curr)
    curr[pos1], curr[pos2] = curr[pos2], curr[pos1]
    return ''.join(curr)

# Slide functions with edge cases
def slideRight(start, pos):
    if ((pos + 1) % 3 == 0):
        return 
    return swapPositions(start, pos, (pos + 1)) 
def slideLeft(start, pos):
    if (pos % 3 == 0):
        return 
    return swapPositions(start, pos, (pos - 1)) 
def slideUp(start, pos):
    if (pos < 3):
        return 
    return swapPositions(start, pos, (pos - 3)) 
def slideDown(start, pos):
    if (pos > 5): 
        return
    return swapPositions(start, pos, (pos + 3)) 

def statesearch(unexplored, goal, path, count = 0):
    global visited
    if (count > 15): #recursion depth
        return [] #what to return
    if unexplored == []:
        return []
    elif goal == head(unexplored):
        return cons(goal,path)
    else:
        newStates = generateNewStates(head(unexplored))         
        #check for repeating states
        for i in newStates:
            if i in visited:
                newStates.remove(i)
        visited.append(head(newStates))
        result = statesearch(newStates, goal, cons(head(unexplored), path), count + 1)
        if result != []:
            count -= 1 # decrement recursion counter
            return result
        else:
            count -= 1 # decrement recursion counter
            return statesearch(tail(unexplored),
                               goal,
                               path, count + 1)


def reverse(st):
    return st[::-1]
    
def head(lst):
    return lst[0]

def next(lst):
    return lst[1]

def tail(lst):
    return lst[1:]

def cons(item,lst):
    return [item] + lst

def generateNewStates(currState):
    posZero = findZero(currState)
    temp = []
    # check is state is possible
    #if yes, add to list of new states
    if (slideRight(currState, posZero) is not None):
        temp.append(slideRight(currState, posZero))
    if (slideLeft(currState, posZero) is not None):
        temp.append(slideLeft(currState, posZero))
    if (slideUp(currState, posZero) is not None):
        temp.append(slideUp(currState, posZero))
    if (slideDown(currState, posZero) is not None):
        temp.append(slideDown(currState, posZero))
    return temp




#test cases from discord (@Lahral) and self

## start = [[0,1,2],[3,4,5],[6,7,8]]
## goal = [[1,0,2],[3,4,5],[6,7,8]]

## start=[[1,2,3],[4,0,5],[6,7,8]]
## goal=[[4,1,3],[0,2,5],[6,7,8]]

## start=[[1,2,3],[4,0,5],[6,7,8]]
## goal=[[1,0,3],[4,2,5],[6,7,8]]

## start=[[1,2,3],[4,0,5],[6,7,8]]
## goal=[[1,0,3],[4,7,5],[2,6,8]]

## start=[[2,8,3],[1,0,4],[7,6,5]]
## goal=[[1,2,3],[8,0,4],[7,6,5]]

## start = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
## goal = [[1, 4, 2], [0, 3, 5], [6, 7, 8]]

## start = [[2,8,3],[1,0,4],[7,6,5]] 
## goal = [[1,2,3],[8,0,4],[7,6,5]]