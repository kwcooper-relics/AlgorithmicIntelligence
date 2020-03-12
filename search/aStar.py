from math import sqrt
from copy import deepcopy
from operator import attrgetter


class Node(object):
    # constructor for Node objects
    def __init__(self, name, posx, posy):
        self.name = name
        self.x = posx
        self.y = posy
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.parents = []

    # method to print Node objects
    def str(self):
        return "Name: " + self.name + " Cost: " + str(self.f)

# AI City Graph representation

# make the nodes
AI_nodeA = Node('A', -6, -2)
AI_nodeB = Node('B', -3, 2)
AI_nodeC = Node('C', -4, -3)
AI_nodeD = Node('D', 2, 4)
AI_nodeE = Node('E', 1, 0)
AI_nodeF = Node('F', 6, 5)

# node list
AI_CITY_NODE_LIST = [AI_nodeA, AI_nodeB, AI_nodeC, AI_nodeD, AI_nodeE, AI_nodeF]

# adjacency list
# These are directed graphs, thus can only move in one direction
AI_CITY_ADJ_LIST = [[AI_nodeA, AI_nodeB, 5],
          [AI_nodeA, AI_nodeC, 4],
          [AI_nodeA, AI_nodeD, 11],
          [AI_nodeB, AI_nodeC, 6],
          [AI_nodeB, AI_nodeD, 5],
          [AI_nodeB, AI_nodeE, 5],
          [AI_nodeC, AI_nodeD, 10],
          [AI_nodeC, AI_nodeE, 5],
          [AI_nodeD, AI_nodeE, 5],
          [AI_nodeD, AI_nodeF, 5],
          [AI_nodeE, AI_nodeD, 5],
          [AI_nodeC, AI_nodeF, 16]]

AI_CITY_ADJ_LIST_V2 = [[AI_nodeA, AI_nodeB, 5],
          [AI_nodeA, AI_nodeC, 4],
          [AI_nodeA, AI_nodeD, 11],
          [AI_nodeB, AI_nodeC, 6],
          [AI_nodeB, AI_nodeD, 5],
          [AI_nodeB, AI_nodeF, 3],
          [AI_nodeC, AI_nodeD, 10],
          [AI_nodeC, AI_nodeE, 5],
          [AI_nodeD, AI_nodeE, 5],
          [AI_nodeD, AI_nodeF, 5],
          [AI_nodeE, AI_nodeD, 5],
          [AI_nodeC, AI_nodeF, 16]]

AI_CITY_ADJ_LIST_V3 = [[AI_nodeA, AI_nodeB, 5],
          [AI_nodeA, AI_nodeC, 4],
          [AI_nodeA, AI_nodeD, 11],
          [AI_nodeB, AI_nodeC, 6],
          [AI_nodeB, AI_nodeD, 5],
          [AI_nodeC, AI_nodeD, 10],
          [AI_nodeC, AI_nodeE, 5],
          [AI_nodeD, AI_nodeE, 5],
          [AI_nodeE, AI_nodeD, 5]]

# Heuristic function -- takes two nodes, returns a number: the Euclidean distance 
# between aNode and bNode
def euclideanDistance(aNode, bNode):
    return sqrt(((aNode.x - bNode.x)**2) + ((aNode.y - bNode.y)**2))

# find_node_to_explore -- takes a list of nodes, returns a node:
# the lowest-cost node in the frontier
def find_node_to_explore(frontier):
    minNode = min(frontier, key=attrgetter('f'))
    return minNode

#the explored state removed
#All nodes directly reachable by the explored node added
#Only the lowest-cost version of any duplicate nodes preserved
def expand_frontier(to_explore, frontier, explored, adjacencyMatrix, goal_state):
    toAdd = [] #list of nodes to be added
    for vertex in adjacencyMatrix:
        if vertex[0].name == to_explore.name: #check for the current node
            #update the heuristics
            vertex[1].h = euclideanDistance(vertex[1], goal_state)
            vertex[1].g = vertex[2]
            #could also take max, however, adding based on hint below
            #vertex[1].f = vertex[0].f + max(vertex[1].h, vertex[1].g) 
            vertex[1].f = vertex[0].f + vertex[1].h + vertex[1].g 
            vertex[1].parents = [vertex[1], vertex[0].parents]
            toAdd.append(vertex[1]) #append what the current node is connected to

    #run checks in toAdd to make sure the nodes are novel
    #if not, the lowest cost is maintained
    toBoot = []
    idx = 0
    for n in toAdd:
        if not frontier: 
            print("empty")
        else:
            for front in frontier:
                if front.name == n.name:
                    if n.f < front.f:
                        print("n is lower than f!!!")
                        frontier.remove(front)
                    else:
                        toBoot.append(idx)
            for exp in explored:
                if exp.name == n.name:
                    toBoot.append(idx)
                    
        idx+=1
    for i in sorted(toBoot, reverse=True):
        del toAdd[i]

    for n in toAdd:
        frontier.append(n)
        
    idx = 0
    for i in range(0, len(frontier)):
        if frontier[i].name == to_explore.name:
            popped = frontier.pop(i)
            if popped.name == to_explore.name:                        
                break
            else:
                print("Error: ", popped.name, to_explore.name)                   
    
    return frontier

def get_Parents(lon):
    pList = []
    while lon:
        if lon[0] == False:
            return list(reversed(pList))
        else:
            pList.append(lon[0])
            lon = lon[1]
    
    
# aStar -- full A* function: takes a list of nodes, an adjacency matrix, a start node, and a goal node
# feel free to turn debugging (printing) on/off as you wish
def aStar(nodeList, adjacencyMatrix, startNode, goalNode, debug=False):
    startNode.h = euclideanDistance(startNode, goalNode)
    startNode.g = 0
    startNode.f = startNode.g + startNode.h
    startNode.parents = [startNode, [False]]
    
    frontier = [startNode] # a list of nodes
    explored = []
    parents = []
    found = False

    it = 0
    while(frontier):
        #printing procedure to see your progress
        if (debug):
            print("frontier:")
            for node in frontier:
                print(node.str())
                pass
            print("explored:")
            for node in explored:
                print(node.str())
                
        currentNode = find_node_to_explore(frontier)
        explored.append(currentNode)
        if currentNode.name == goalNode.name:
            found == True
            print("We found the goal!")
            print()
            print("frontier:")
            for node in frontier:
                print(node.str())
            print("explored:")
            for node in explored:
                print(node.str())
            
            p = get_Parents(currentNode.parents)
            
            #list, cost
            return (p,currentNode.f)
        else:
            frontier = expand_frontier(currentNode, frontier, explored, adjacencyMatrix, goalNode)
            #add the heuristic info to the exp frontier
            
        it += 1
    print("frontier", frontier)
    print("iterations:", it)                            

    # Once search is finished, show results        
    print("Goal not found :(")

    
# Main method. Add more tests!
def main():
    #Test for AI City Graph, starting at A with goal node F
    print("TEST 1: Given Problem -----------------------------------------")
    result = aStar(AI_CITY_NODE_LIST, AI_CITY_ADJ_LIST, AI_nodeA, AI_nodeF)
    print()
    print("Path: ", end=" ")
    if result is None:
        print("No goal, No path!")
    else:
        for i in result[0]:
            print(i.name, end=" ")
        print()
        print("Total Path Cost: %d" % result[1])
    #add your own tests below!
    #return result

    print()
    print("TEST 2: New Graph ---------------------------------------------")
    result = aStar(AI_CITY_NODE_LIST, AI_CITY_ADJ_LIST_V2, AI_nodeA, AI_nodeE)
    print()
    print("Path: ", end=" ")
    if result is None:
        print("No goal, No path!")
    else:
        for i in result[0]:
            print(i.name, end=" ")
        print()
        print("Total Path Cost: %d" % result[1])
    #add your own tests below!
    #return result

    print()
    print("TEST 3: Unreachable Node --------------------------------------")
    result = aStar(AI_CITY_NODE_LIST, AI_CITY_ADJ_LIST_V3, AI_nodeA, AI_nodeF)
    print()
    print("Path: ", end=" ")
    if result is None:
        print("No goal, No path!")
    else:
        for i in result[0]:
            print(i.name, end=" ")
        print()
        print("Total Path Cost: %d" % result[1])
    #add your own tests below!
    #return result

if __name__ == "__main__":
    main()


    
