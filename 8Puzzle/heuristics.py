import matTools as mt

#manhattan distance
#distance += abs(x_value - x_goal) + abs(y_value - y_goal)
def manhattan(state, goal):
    state = mt.oSpce(mt.flatten(state))
    goal = mt.oSpce(mt.flatten(goal))
    
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

#Checks how many tiles are out of place from the goal
def outOfPlace(state, goal):
    cnt = 0
    for i in range(0, len(goal)):
        for j in range(0, len(goal)):
            tile = goal[i][j]
            for k in range(0, len(state)):
                for l in range(0, len(state)):
                    if state[k][l] == goal[i][j]:
                        cnt += 1
    return cnt

#Checks for how many tiles are out of the row or column
def outRowCol(state, goal):
    rowCnt = 0
    for i in range(0, len(goal)):
        row = goal[i]
        for j in row:
            if j not in state[i]:
                rowCnt += 1
    colCnt = 0
    cols = []
    for i in range(0, len(goal)):
        for j in range(0, len(goal)):
            cols.append(goal[j][i])
            for k in range(0, len(state)):
                for l in range(0, len(state)):
                    if not (state[l][k] in cols):
                        colCnt += 1
            if j == len(goal):
                cols = []    
    return rowCnt + colCnt

#looks at the patterns between each of the adjecent tiles
def pattern(state, goal):
    state = mt.oSpce(mt.flatten(state))
    goal = mt.oSpce(mt.flatten(goal))
    
    pairS = []
    pairG = []

    for i in range(0,len(state) - 1):
        pairS.append([state[i], state[i+1]])

    for i in range(0,len(goal) - 1):
        pairG.append([goal[i], goal[i+1]])

    score = 0
    for x,y in zip(pairS,pairG):
        if x == y:
            score += 1
    return score

#weights the space location, making the middle
#space adversive to trim brances traveled. 
def spceWeight(state):
    if " " in state[1]:
        if " " == state[1][1]:
            return 3
        else:
            return 2
    else:
        return 1
