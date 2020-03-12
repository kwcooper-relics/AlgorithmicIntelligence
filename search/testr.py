from operator import attrgetter
from math import sqrt

class Node(object):
    # constructor for Node objects
    def __init__(self, name, posx, posy):
        self.name = name
        self.x = posx
        self.y = posy
        self.g = 0
        self.h = 0
        self.f = self.g + self.h

    # method to print Node objects -- feel free to modify!
    def str(self):
        return "Name: " + self.name + " Cost: " + str(self.f)

# AI City Graph representation
AI_nodeA = Node('A', -6, -2)
AI_nodeB = Node('B', -3, 2)
AI_nodeC = Node('C', -4, -3)
AI_nodeD = Node('D', 2, 4)
AI_nodeE = Node('E', 1, 0)
AI_nodeF = Node('F', 6, 5)

# adjacency list
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

nList = [AI_nodeF, AI_nodeA, AI_nodeB, AI_nodeC, AI_nodeD, AI_nodeE]

def printG(nLIst):
    for i in nList:
        print(i.g)

printG(nList)

c = 10
for n in nList:
    n.g = c
    c = c -1

printG(nList)


#finds the min node in th node list
def find_node_to_explore(frontier):
    minNode = min(frontier, key=attrgetter('g'))
    return minNode
     
print("min node")
node = find_node_to_explore(nList)
print(node.g)

def euclideanDistance(aNode, bNode):
    return sqrt(((aNode.x - bNode.x)**2) + ((aNode.y - bNode.y)**2))



#the explored state removed
#All nodes directly reachable by the explored node added
#Only the lowest-cost version of any duplicate nodes preserved
def expand_frontier(to_explore, frontier, adjacencyMatrix, goal_state):
    #pop the node to explore...
##    idx = 0
##    for i in frontier:
##        if i == to_explore:
##            frontier.pop(i)
##            break
##        i += 1
    #find the next node(s), and make a list to add
    toAdd = []
    for i in adjacencyMatrix:
        if i[0] == to_explore:
            toAdd.append([i[1])
    #fetch the entire node
    for node in toAdd: #this is a list of node names
        for vertx in adjacencyMatrix: #get the whole node
            if node == vertx[0]: #if node name === vertex[0]
                for nde in frontier: #look through fronteir to find dups
                    if  vertx[0:2] == nde[0:2]: #check if nodes are the same
                        if vertex[3] < nde[3]: #new cost less than old?
                            fronteir.remove(nde)
                            fronteir.append(vertex)
                    else: #if not in frontier
                         #then add the node to the frontier
                        fronteir.append(vertex)
    #frontier.sort(key = lambda x: x.attribute)
    frontier.sort(key=lambda x: x[2])


    return frontier


    #pop the node to explore...
    
    #find the next node(s), and make a list to add
    toAdd = []
    for i in adjacencyMatrix:
        if i[0] == to_explore:
            toAdd.append([i[1]])
    #print(toAdd)
    #fetch the entire node
    for nde in toAdd: #this is a list of node names
        node = nde[0]
        for vertex in adjacencyMatrix: #get the whole node
            #print(vertex[0].name)
            vertx = vertex[0]
            vertx2 = vertex[1]
            #print("vertx", vertex[2])
            #print(node, vertx)
            if node.name == vertx.name: #if node name === vertex[0]
                #print("equal")
                print("frntttt", frontier)
                if not frontier:  #check if the frontier is empty
                    print("not front!")
                    frontier.append(vertex) 

                for node2 in frontier: #look through fronteir to find dups
                    nde = node2[0]
                    nde2 = node2[1]
                    print("nde:", nde)
                    print("node2", node2)
                    print("compare nodes", vertx.name , nde.name)
                    print("compare second nodes", nde2.name, nde2.name)
                    if vertx.name == nde.name and nde2.name == nde2.name: #check if nodes are the same
                        print("compp", vertex[2], node2[2])
                        if vertex[2] < node2[2]: #new cost less than old?
                            print()
                            print("frontier", len(frontier))
                            print()
                            #remove the node from the frontier
                            idx = 0
                            for node3 in frontier:
                                print("NODE3", node3)
                                node3a = node3[0]
                                node3b = node3[1]
                                if node3a.name == vertx.name and node3b.name == vertx2.name and node3[2] == vertex[2]:
                                    pass
                                    
                            frontier.pop(idx)
                            frontier.append(vertex)
                            #print("", frontier)
                    else: #if not in frontier
                         #then add the node to the frontier
                        frontier.append(vertex)
                    
                        print("after appended", frontier)
    #frontier.sort(key=lambda x: x[2])
    print()
    return frontier



#the explored state removed
#All nodes directly reachable by the explored node added
#Only the lowest-cost version of any duplicate nodes preserved
def expand_frontier(to_explore, frontier, explored, adjacencyMatrix, goal_state):
    #pop the node to explore...
    idx = 0
    for i in range(0, len(frontier)):
        if i == to_explore:
            popped = frontier.pop(i)
            print("names:", popped.name, to_explore.name)
            if popped.name == to_explore.name:                        
                break
            else:
                print("Error: ", popped.name, to_explore.name)
                         
    
    return frontier

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
