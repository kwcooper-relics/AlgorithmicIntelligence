#8Puzzle Solution Search
#Keiland Cooper
#Q351

import copy
import time
import random
from operator import itemgetter
import matplotlib.pyplot as plt
import heuristics as h
import matTools as mt

#makes the puzzle
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


#displays arrays in an appealing way
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


#finds the space where the space is
def findSpace(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == " ":
                return [i, j]
    return False

#swaps the space with the index
#this is hardcoded for speed
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
    return newPuzzle

#generates random moves of size
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


#node data structure
def makeNode(state, parent, depth, pathCost):
    return [state, parent, depth, pathCost]

#makes all possible children of a state
def makeChildren(state, rmvSme=True):
    mvs = ["u", "d", "l","r"]
    childs = []
    for i in mvs:
        childs.append(swapSpce(state, i))
    #could make it a set for more concise code
    if rmvSme == True:
        for i in childs:
            if i == state:
                childs.remove(i)
    return childs

#checks if an array object is in a list
def inLstOLst(obj, lst):
    for i in lst:
        if cmpr(obj, i[0]):
            return True
    return False

#compares two array objects
def cmpr(m1, m2):
    for i,j in zip(m1,m2):
        if i != j:
            return False
    return True


#searches the parent nodes for a path
def getParents(crnt, goal):
    path = []
    while crnt != None:
        path.append(copy.deepcopy(crnt[0]))
        crnt = crnt[1]
    path = list(reversed(path))
    #path.append(goal)
    return path



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
            if not ((inLstOLst(child, exp)) or (inLstOLst(child, frnt))):
                if cmpr(child, goal):
                    print("Found the solution!", end=" ")
                    print("iteration: ", it)
                    child = makeNode(child, parent, 0, (parent[3] + 1))
                    return parent, child, exp, times
                it += 1
                child = makeNode(child, parent, (parent[2] + 1), 0)
                frnt.append(child)

        if it % 5000 == 0:
            print("Stil looking, I've seen", it, "nodes.", end="\n")
            print("I'm on level", parent[2])
        if it > l:
            print("Limit Reached! breaking...")
            break
    print("Frontier is empty!")

#INFORMED SEARCH                    

def informedHeuristic(strt, goal, heur, l):
    strt = makeNode(strt, None, 0, 0)
    frnt = [strt] #could make this a fifo queue
    exp = [] #need checking function now.
    times = []
    it = 0
    tic = time.time()
    while frnt:
        
        frnt = sorted(frnt, key=itemgetter(3))
        parent = frnt.pop(0)
  

        exp.append(parent)
        children = makeChildren(parent[0])
        toc = time.time() - tic
        times.append(toc)
        for child in children:
            if not (inLstOLst(child, exp) or inLstOLst(child, frnt)):
                it += 1
                if cmpr(child, goal):
                    print("Found the solution!", end=" ")
                    print("iteration: ", it)
                    child = makeNode(child, parent, 0, 0)
                    return parent, child, exp, times
                
                if heur == "l":
                    s = lenFrmGoal(child, goal)
                    s = s + parent[3]
                elif heur == "m":
                    s = h.manhattan(child, goal)
                    s = s + parent[3]
                elif heur == "cr":
                    s = h.outRowCol(child, goal)
                    s = s + parent[3]
                elif heur == "pt":
                    s = h.pattern(child, goal)
                    s = (s * 2) + parent[3]
        
                child = makeNode(child, parent, (parent[2] + 1), s)
                frnt.append(child)
                
        if it % 5000 == 0:
            print("Stil looking, I've seen", it, "nodes.", end="\n")
            print("I'm on level", parent[2])
        if it > l:
            print("Limit Reached! breaking...")
            break
    print("Frontier is empty!")    


#this function runs both of the 
def bothInformedHeuristics(strt, goal, l):
    strt = makeNode(strt, None, 0, 0)
    frnt = [strt] #could make this a fifo queue
    exp = [] #need checking function now.
    times = []
    it = 0
    tic = time.time()
    while frnt:
        #let's resort the frontier based on the value
        #let's not use this...
        frnt = sorted(frnt, key=itemgetter(3))
        parent = frnt.pop(0)
    
        
        exp.append(parent)
        children = makeChildren(parent[0])
        toc = time.time() - tic
        times.append(toc)
        for child in children:
            if not (inLstOLst(child, exp) or inLstOLst(child, frnt)):
                it += 1
                if cmpr(child, goal):
                    print("Found the solution!", end=" ")
                    print("iteration: ", it)
                    child = makeNode(child, parent, 0, 0)
                    return parent, child, exp, times

                #now let's grab the heuristic info
                #lg = lenFrmGoal(child, goal)                
                mh = h.manhattan(child, goal)
                rc = h.outRowCol(child, goal)
                pt = h.pattern(child, goal)
                sw = h.spceWeight(child)
                
                h = mh - (pt * 3) - (sw * 2)
                h = h + parent[3] #sum the past heuristic value for branch cost
                child = makeNode(child, parent, 0, h)
                frnt.append(child)
        if it % 5000 == 0:
            print("Stil looking, I've seen", it, "nodes.", end="\n")
        if it > l:
            print("Limit Reached! breaking...")
            break
    print("Frontier is empty!")


#Testing function
def testUninformedSearch(init, goal, limit):
    print("Running Uninformed search...")
    b = time.time()
    p, c, e, ts = bfs(init, goal, limit)
    pth = getParents(c, goal)

    a = time.time()
    print("time:", a-b)

    for i in pth:
        print()
        disp(i)

    plot = False
    if plot:
        plt.plot(ts)
        plt.suptitle("Time of Breath First Search")
        #plt.title(mt.reMat(init))
        plt.xlabel("Iteration")
        plt.ylabel("Times (s)")
        plt.show()
    return ts


#testing function
def testInformedSearch(init, goal, limit):
    
    b = time.time()
    h = "m" #choose m for h.manhattan, l for distance
    if h == "m":
        typ = "manhattan"
    elif h == "l":
        typ = "Distance"
    print("Running Informed search... (", typ, ")")
    
    p, c, e, ts = informedHeuristic(init, goal, h, limit) #run search
    pth = getParents(c, goal) #backtrace through nodes to get parents
    a = time.time()
    print("time:", a-b)

    for i in pth:
        print()
        disp(i)

    plot = False
    if plot:
        plt.plot(ts)
        t = "Time of Heuristic Search (" + typ + ")"
        plt.suptitle(t)
        #plt.title(mt.reMat(init))
        plt.xlabel("Iteration")
        plt.ylabel("Times (s)")
        plt.show()
    return ts


def testInformedSearchToo(init, goal, limit):
    
    b = time.time()
    print("Running Informed search too... ")
    
    p, c, e, ts = bothInformedHeuristics(init, goal, limit) #run search
    pth = getParents(c, goal) #backtrace through nodes to get parents
    a = time.time()
    print("time:", a-b)

    for i in pth:
        print()
        disp(i)

    plot = False
    if plot:
        plt.plot(ts)
        t = "Time of Heuristic Search"
        plt.suptitle(t)
        #plt.title(mt.reMat(init))
        plt.xlabel("Iteration")
        plt.ylabel("Times (s)")
        plt.show()
    return ts



initialState = makeState(1, 2, 3, 4, 5, 6, 7, " ", 8)
goalState = makeState(1, 2, 3, 4, 5, 6, 7, 8, " ")

testUninformedSearch(initialState, goalState, 2000000)
testInformedSearch(initialState, goalState, 2000000)
#testInformedSearchToo(initialState, goalState, 2000000)


#-----------------------------------------------------------
#All of this code below was used to generate plots, and to
#run the algorhithms over the 


##arrays = [[[1,2,3],[4,5,6],[7," ",8]],
##          [[" ",2,3],[1,4,6],[7,5,8]],
##          [[2,3,6],[1,4,8],[7,5," "]],
##          [[" ",3,6],[2,1,8],[7,4,5]],
##          [[3,6,8],[2," ",1],[7,4,5]]]

#This data was collected from running each of the functions.
#I just wrote it down to save time for the plotting
##uIter = [1,16,164,1253,13276]
##iIter = [2,10,35,144,667]
##bIter = [2,8,14,67,247]

##utl = []
##print("Uninformed Search running...")
##for init in arrays:
##    goal = [[1,2,3],[4,5,6],[7,8," "]]
##    p, c, e, ts = bfs(init, goal, 2000000)
##    utl.append(ts)
##
##itl = []
##print("Informed Search running...")
##for init in arrays:
##    goal = [[1,2,3],[4,5,6],[7,8," "]]
##    p, c, e, ts = informedHeuristic(init, goal, "m", 2000000)
##    itl.append(ts)

##btl = []
##print("Informed Search running (two heuristics)...")
##for init in arrays:
##    goal = [[1,2,3],[4,5,6],[7,8," "]]
##    p, c, e, ts = bothInformedHeuristics(init, goal, 2000000)
##    btl.append(ts)


##xAxis = range(0, 5)
##plt.title("Algorithmic Complexity per Algorithm")
##plt.plot(xAxis, uIter)
##plt.plot(xAxis, iIter)
##plt.plot(xAxis, bIter)
##plt.legend(["Uninformed", "Informed", "Informed (new heuristic)"], loc='upper left')
##plt.xlabel("puzzle (least to most complex)")
##plt.ylabel("number of nodes searched")
##plt.show()


#time plotting
##
##for i in itl:
##    plt.plot(i)
##    plt.title("Uninformed Search")
##    plt.xlabel("Time")
##    plt.ylabel("Iteration")
##    plt.show()
    
