visited = [] # recursion for DFS

def tilePuzzle (start, goal):
    startList = unList(start)
    goalList = unList(goal)

    # What the output should look like
    result = reverse(statesearch([startList], goalList, []))
    final = []
    
    for i in range(len(result)):
        new = createList(result[i])
        final.append(new)
    print(final)

#find space element
def findZero(curr):
    for i in range(len(curr)):
        if curr[i] == '0':
            return i
    return -1

#syntax for input
def unList(start):
    tempList = ""
    startLen = len(start)
    for i in range(startLen):
        if (start[i] >= '0' and start[i] < '9'):
            tempList += start[i]
            #tempList.extend(start[i])
    return tempList

#syntax for output
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
    # print(swapPositions(start, pos, (pos + 1)), " right" )
    return swapPositions(start, pos, (pos + 1)) 
def slideLeft(start, pos):
    if (pos % 3 == 0):
        return 
    # print(swapPositions(start, pos, (pos - 1)), " left" )
    return swapPositions(start, pos, (pos - 1)) 
def slideUp(start, pos):
    if (pos < 3):
        return 
    # print(swapPositions(start, pos, (pos - 3)), " up")
    return swapPositions(start, pos, (pos - 3)) 
def slideDown(start, pos):
    if (pos > 5): 
        return
    # print(swapPositions(start, pos, (pos + 3)), " down" )
    return swapPositions(start, pos, (pos + 3)) 

def statesearch(unexplored, goal, path, count = 0):
    global visited
    if (count > 15):
        return [] #what to return
    if unexplored == []:
        print("unexplored empty")
        return []
    elif goal == head(unexplored):
        print (head(unexplored), " is goal and found")
        return cons(goal,path)
    else:
        newStates = generateNewStates(head(unexplored)) 
        
        print(newStates, " are new states before cut")
        #check for repeating states
        for i in newStates:
            if i in visited:
                newStates.remove(i)
        print(newStates, " are new states after cut")
        print(path, " is path")
        visited.append(head(newStates))
        result = statesearch(newStates, goal, cons(head(unexplored), path), count + 1)
        if result != []:
            print(count, " before decrement")
            print (path, " path in result != []")
            count -= 1 #
            return result
        else:
            print(unexplored, " is uneplxored")
            print(path, " = path in else")
            count -= 1
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
    if (slideRight(currState, posZero) is not None):
        temp.append(slideRight(currState, posZero))
    if (slideLeft(currState, posZero) is not None):
        temp.append(slideLeft(currState, posZero))
    if (slideUp(currState, posZero) is not None):
        temp.append(slideUp(currState, posZero))
    if (slideDown(currState, posZero) is not None):
        temp.append(slideDown(currState, posZero))
    return temp



if __name__ == '__main__':
    import sys
    start = sys.argv[1]
    goal = sys.argv[2]
    answer = tilePuzzle(start, goal)

#to run in terminal:
#start in folder with executable

#py tilepuzzle.py [[0,1,2][3,4,5],[6,7,8]] [[1,2,0][3,4,5],[6,7,8]]

#replace first list with start and second list with goal

#test cases from discord (@Lahral) and self

## start = [[0,1,2],[3,4,5],[6,7,8]]
## goal = [[1,0,2],[3,4,5],[6,7,8]]
## returns a result in: <1 sec

## start=[[1,2,3],[4,0,5],[6,7,8]]
## goal=[[4,1,3],[0,2,5],[6,7,8]]
## returns a result in: takes time

## start=[[1,2,3],[4,0,5],[6,7,8]]
## goal=[[1,0,3],[4,2,5],[6,7,8]]
## returns a result in: <1 sec

## start=[[1,2,3],[4,0,5],[6,7,8]]
## goal=[[1,0,3],[4,7,5],[2,6,8]]
## returns a result in: takes time

## start=[[2,8,3],[1,0,4],[7,6,5]]
## goal=[[1,2,3],[8,0,4],[7,6,5]]
## returns a result in: takes time

## start = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
## goal = [[1, 4, 2], [0, 3, 5], [6, 7, 8]]
## returns but takes times?

## start=[[0,1,2],[3,4,5],[6,7,8]]
## goal=[[8,7,6],[5,4,3],[2,1,0]]
## returns a result in: 