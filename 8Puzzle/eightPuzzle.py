#8Puzzle Solution Search
import copy
import time
import random
from operator import itemgetter
import matplotlib.pyplot as plt

#to do:
#   fix is solveable
#   better print disp
#   add more heuristics
#   make classes
#   redo parent search structure (speedup?)

def makeState(nw, n, ne, w, c, e, sw, s, se):
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    matrix[0][0] = nw
    matrix[0][1] = n
    matrix[0][2] = ne
    matrix[1][0] = w
    matrix[1][1] = c
    matrix[1][2] = e
    matrix[2][0] = sw
    matrix[2][1] = s
    matrix[2][2] = se
    return matrix

def dispPuz(puzzle):
# to print the current puzzle state, from list. 
    c = -1
    for i in puzzle:
        if c < 2:
            print(i, end= " ")
            c +=1
        else:
            c = 0
            print()
            print(i, end=" ")

def printState(puzzle):
    for i in puzzle:
        print(i)
        
def findSpace(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == " ":
                return [i, j]
    return False

def swapSpce(puzzle, drctn):
    # hardcoded space to avoid temp var
    spc = findSpace(puzzle)
    if spc == False:
        print("bool error")
    newPuzzle = copy.deepcopy(puzzle)
    if drctn == "d" and spc[0] != 0:
        newPuzzle[spc[0]][spc[1]] = puzzle[spc[0]-1][spc[1]]
        newPuzzle[spc[0]-1][spc[1]] = " "
        
    elif drctn =="u" and spc[0] != 2:
        newPuzzle[spc[0]][spc[1]] = puzzle[spc[0]+1][spc[1]]
        newPuzzle[spc[0]+1][spc[1]] = " "
        
    elif drctn =="r" and spc[1] != 0:
        newPuzzle[spc[0]][spc[1]] = puzzle[spc[0]][spc[1]-1]
        newPuzzle[spc[0]][spc[1]-1] = " "
        
    elif drctn =="l" and spc[1] != 2:
        newPuzzle[spc[0]][spc[1]] = puzzle[spc[0]][spc[1]+1]
        newPuzzle[spc[0]][spc[1]+1] = " "
        
    else:
        pass
        #print("invalid movement!!!")
    return newPuzzle
    
def randMoveLst(sze):
    mvs = ["u", "d", "l","r"]
    rndMvs = []
    for i in range(sze):
        rndMvs.append(random.choice(mvs))
    return rndMvs

#take a list of directions, and apply each one     
def randomize(puzz, lod):
    for d in lod:
        swapSpce(puzz, d)


#flatten array
def flatten(arry):
    return [num for row in arry for num in row]

#convert string space to 0
def oSpce(lst):
    return [0 if i==" " else i for i in lst]

#makes string of numbers
def dence(lst):
    return ''.join(map(str,lst))

#combine these functions
def reMat(arryLst):
    out = []
    for arry in arryLst:
        arry = flatten(arry)
        arry = oSpce(arry)
        arry = dence(arry)
        out.append(arry)
    return out

    
     
#checks IF a puzzle can be solved (returns True)
#Johnson & Story (1879)
#convert to 2d array,
#convert "" to 0
def isSolvable(puzz):
    count = 0
    for i in range(len(puzz)-1):
        for j in range(i+1):
            #print(i)
            if puzz[i] and puzz[j] and puzz[i] > puzz[j]:
                count +=1

    return count % 2 == 0
    

#--      


def makeChildren(state, rmvSme=True):
    mvs = ["u", "d", "l","r"]
    childs = []
    for i in mvs:
        #print("State: ")
        #print(state)
        childs.append(swapSpce(state, i))
    #could make it a set for more concise code
    if rmvSme == True:
        for i in childs:
            if i == state:
                childs.remove(i)
    return childs


def makeNode(state, parent, depth, pathCost):
    return [state, parent, depth, pathCost]


def inLstOLst(obj, lst):
    for i in lst:
        #print("lst: ")
        #print(obj, i[0])
        if cmpr(obj, lst[0]):
            #print("returned true")
            return True
    return False

def cmpr(m1, m2):
    for i,j in zip(m1,m2):
        if i != j:
            return False
    return True


def getParents(crnt):
    path = []

    while crnt != None:
        path.append(copy.deepcopy(crnt[0]))
        crnt = crnt[1]
    path = list(reversed(path))
    return path
        

    
    
#needs work but should be faster
def backtrace2(crnt, goal, strt, exp):
    path = [goal]
    while crnt[0] != strt[0] or crnt == None:
        cnt = 0
        for e in exp:
            if crnt[1] == e[0]:
                cnt += 1
                path.append(crnt[1])
                crnt = e
                
        #path.append(strt)
        path = list(reversed(path))
        return path
        

def disp(a):
    string = " "
    if len(a) == 2:
        col1 = len(a[0][0])
        row1 = len(a[0])
        for i in range(0, col1):
            for j in range(0, row1):
                string = string + " " + str(a[0][i][j])
            print(string)
            string = " "
    else:
        col = len(a[0])
        row = len(a)
        for i in range(0, col):
            for j in range(0, row):
                string = string + " " + str(a[i][j])
            print( string)
            string = " "



#Breath first search though the possible state space
#   what if strt == goal... (add exp after the if's?)
def bfs(strt, goal, l):
    strt = makeNode(strt, None, 0, 0)
    times = []
    frnt = [strt] #could make this a fifo queue
    exp = [] #need checking function now. 
    it = 0
    tic = time.time()
    while frnt:
        parent = frnt.pop(0)
        exp.append(parent)
        children = makeChildren(parent[0])
        for child in children:
            toc = time.time() - tic
            times.append(toc)
            if not ((inLstOLst(child, exp)) and (inLstOLst(child, frnt))):
                if cmpr(child, goal):
                    print("Found the solution!", end=" ")
                    print("iteration: ", it)
                    child = makeNode(child, parent, 0, 0)
                    return parent, child, exp, times
                it += 1
                child = makeNode(child, parent, 0, 0)
                frnt.append(child)
        if it % 5000 == 0:
            print("Stil looking, I've seen", it, "nodes.", end="\n")
        if it > l:
            print("Limit Reached! breaking...")
            break
    print("Frontier is empty!")


#-------------------------------------------------------------------


#manhattan distance
#distance += abs(x_value - x_goal) + abs(y_value - y_goal)
def manhattan(state, goal):
    state = oSpce(flatten(state))
    goal = oSpce(flatten(goal))
    
    s = sum(abs(s%3 - g%3) + abs(s//3 - g//3)
        for s, g in ((state.index(i), goal.index(i)) for i in range(1, 9)))
    return s

#looks at current state and goal and then
#decides how far you are from the goal state
def lenFrmGoal(state, goal):
    sm = 0
    for i in range(0, len(goal)):
        for j in range(0, len(goal)):
            tile = goal[i][j]
            for k in range(0, len(state)):
                for l in range(0, len(state)):
                    if state[k][l] == tile:
                        sm += (k - i)*(k - i)+(j - l)*(j - l)
    return sm

def informedHeuristic(strt, goal, h, l):
    strt = makeNode(strt, None, 0, 0)
    frnt = [strt] #could make this a fifo queue
    exp = [] #need checking function now.
    times = []
    it = 0
    tic = time.time()
    while frnt:
        if h == "l":
            #let's resort the frontier based on the value 
            frnt = sorted(frnt, key=itemgetter(3))
            parent = frnt.pop(0)
        elif h == "m":
            frnt = sorted(frnt, key=itemgetter(3))
            parent = frnt.pop(0)
        
        exp.append(parent)
        children = makeChildren(parent[0])
        toc = time.time() - tic
        times.append(toc)
        for child in children:
            if not ((inLstOLst(child, exp)) and (inLstOLst(child, frnt))):
                it += 1
                if cmpr(child, goal):
                    print("Found the solution!", end=" ")
                    print("iteration: ", it)
                    child = makeNode(child, parent, 0, 0)
                    return parent, child, exp, times
                
                if h == "l":
                    s = lenFrmGoal(child, goal)
                    s = s + parent[3]
                elif h == "m":
                    s = manhattan(child, goal)
                    s = s + parent[3]
                child = makeNode(child, parent, 0, s)
                frnt.append(child)
                
        if it % 5000 == 0:
            print("Stil looking, I've seen", it, "nodes.", end="\n")
        if it > l:
            print("Limit Reached! breaking...")
            break
    print("Frontier is empty!")


#########################################################
#strt = [["",1,2],[4,5,3],[7,8,6]]

#hardest 8 puzzle configs (31 moves)
#http://w01fe.com/blog/2009/01/the-hardest-eight-puzzle-instances-take-31-moves-to-solve/
#strt = [[8,6,7],[2,5,4],[3," ",1]] #took 32741 iterations bfs
#strt = [[6,4,7],[8,5," "],[3,2,1]] #took 73830 iterations bfs; 348.5s (5 minutes)

#strt = [[1,2,3],[4,5,6],[8,7," "]] #this is unsolveable
strt = [[" ",3,5],[1,4,6],[7,2,8]] #71191 iterations, 515s
#strt = [[" ",1,3],[4,2,6],[7,5,8]] #39014 iterations, 94s
#strt = [[1,2,3],[4," ",6],[7,5,8]]  #32013 iterations, 71s
#strt = [[1,2,3],[4,5,6],[" ",7,8]]   #3 iterations, 0s
#strt = [[1,2,3],[4,5,6],[7," ",8]]  #1 iteration, 0s
#strt = [[1,2,3],[4," ", 5],[7,8,6]] #4 iterations, .2s
goal = [[1,2,3],[4,5,6],[7,8," "]]






def testUninformedSearch(init, goal, limit):
    print("Running Uninformed search...")
    b = time.time()
    p, c, e, ts = bfs(init, goal, limit)
    pth = getParents(c)

    a = time.time()
    print("time:", a-b)

    for i in pth:
        print()
        disp(i)

    plot = True
    if plot:
        plt.plot(ts)
        plt.suptitle("Time of Breath First Search")
        #plt.title(reMat(init))
        plt.xlabel("Iteration")
        plt.ylabel("Times (s)")
        plt.show()
        
        
    
    
    
def testInformedSearch(init, goal, limit):
    print("Running Informed search... (manhattan)")
    b = time.time()
    h = "m" #choose m for manhattan, l for distance
    
    p, c, e, ts = informedHeuristic(init, goal, h, limit) #run search
    pth = getParents(c) #backtrace through nodes to get parents
    a = time.time()
    print("time:", a-b)

    for i in pth:
        print()
        disp(i)

    plot = True
    if plot:
        plt.plot(ts)
        plt.suptitle("Time of Heuristic Search (man)")
        #plt.title(reMat(init))
        plt.xlabel("Iteration")
        plt.ylabel("Times (s)")
        plt.show()

initialState = strt   
#initialState = makeState(1, 2, 3, 4, 5, 6, 7, 8, " ")
goalState = makeState(1, 2, 3, 4, 5, 6, 7, " ", 8)
testUninformedSearch(initialState, goalState, 2000000)
#testInformedSearch(initialState, goalState, 2000000)
