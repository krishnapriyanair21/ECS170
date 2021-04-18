def tilePuzzle (start, goal):
    print(start)
    unList(start)
    unList(goal)
    createList(unList(start))
    # print(slideRight([start], 0) + " swap right")
    # print(slideLeft([start], 3) + " swap Left")
    # return statesearch([start], goal, [])

def unList(start):
    tempList = []
    startLen = len(start)
    for i in range(startLen):
        if (start[i] >= '0' and start[i] < '9'):
            tempList.extend(start[i])
    # tempList.extend(start[0][1])
    # tempList.extend(start[2])
    return tempList

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
    print(result)
            

def swapPositions(curr, pos1, pos2):
    temp = curr[pos1]
    curr[pos1] = curr[pos2]
    curr[pos2] = temp
    return curr

def slideRight(start, pos):
    return swapPositions([start], pos, (pos + 1)) 
def slideLeft(start, pos, switch):
    return swapPositions([start], pos, (pos - 1)) 
def slideUp(start, pos, switch):
    return swapPositions([start], pos, (pos - 3)) 
def slideDown(start, pos, switch):
    return swapPositions([start], pos, (pos + 3)) 

def statesearch(unexplored,goal,path):
    if unexplored == []:
        return []
    elif goal == head(unexplored):
        return cons(goal,path)
    else:       
        result = statesearch(generateNewStates(head(unexplored)),
                             goal,
                             cons(head(unexplored), path))
        if result != []:
            return result
        else:
            return statesearch(tail(unexplored),
                               goal,
                               path)


# def generateNewRedJumps(currState):
#     return generateNew(currState,0,"RB_","_BR")

# def generateNewBlueSlides(currState):
#     return reverseEach(generateNew(reverse(currState),0,"B_","_B"))

# def generateNewBlueJumps(currState):
#     return reverseEach(generateNew(reverse(currState),0,"BR_","_RB"))

def reverseEach(listOfLists):
    result = []
    for st in listOfLists:
        result.append(reverse(st))
    return result
def reverse(st):
    return st[::-1]
    
def head(lst):
    return lst[0]

def tail(lst):
    return lst[1:]

def take(n,lst):
    return lst[0:n]

def drop(n,lst):
    return lst[n:]

def cons(item,lst):
    return [item] + lst
# def generateNewStates(currState):
#     return (generateNewRedSlides(currState) + generateNewRedJumps(currState) +
#             generateNewBlueSlides(currState) + generateNewBlueJumps(currState))

if __name__ == '__main__':
    import sys
    start = sys.argv[1]
    goal = sys.argv[2]
    answer = tilePuzzle(start, goal)