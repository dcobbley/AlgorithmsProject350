'''
============================================================================
// Name        : Dijkstra.py
// Description : Dijkstra shortest path algorithm implementation
============================================================================
'''

import os
import copy

class Node:
    def __init__(self,index):
        self.index = index
        self.AdjacentNodes = {}

    def __str__(self):
        return "Node " + str(self.index) + " connected to nodes " + str([(x.index, self.AdjacentNodes[x]) for x in self.AdjacentNodes])

    def addAdjacentNode(self,node,distance):
        self.AdjacentNodes[node] = distance;

    def getAdjacentNodes(self):
        return self.AdjacentNodes.keys()

    def getIndex(self):
        return self.index

    def getDistance(self,index):
        return self.AdjacentNodes[index]

class Graph:
    def __init__(self):
        self.NodesList = {}
        self.numNodes = 0

    def addNode(self,index):
        newNode = Node(index)
        self.NodesList[index] = newNode
        self.numNodes = self.numNodes+1
        return newNode

    def getNode(self,index):
        if index in self.NodesList:
            return self.NodesList[index]
        else:
            return None

    def addEdge(self,findex,tindex, distance):
        if findex not in self.NodesList:
            self.addNode(findex)
        if tindex not in self.NodesList:
            self.addNode(tindex)
        self.NodesList[findex].addAdjacentNode(self.NodesList[tindex],distance)

    def getEdges(self):
        for x in self.NodesList.values():
            for y in x.AdjacentNodes:
                print "(%d, %d)  %d" % (x.index,y.index,x.AdjacentNodes[y])

    def __iter__(self):
        return iter(self.NodesList.values())

    def __str__(self):
        return str([x.index for x in self.NodesList.values()])


#def wrapper(adjacency_list):
#   for adjacent in adjacency_list:
        #first give adjacent to dijkstra
#    for tail in dictionary:
#	#get the tail pass to Dijkstra


def Dijkstra(Graph, startIndex):
    shPath = {}
    for x in Graph.NodesList.keys():
        shPath[x] = float('Inf')

    shPath[startIndex] = 0
    doneNodes = [startIndex]

    num = Graph.numNodes - 1

    while (num !=0) :
        #print "-- loop: ", num
        num = num - 1
        possiblePaths = {}
        for y in doneNodes:
            d = dict((p,q) for p,q in Graph.NodesList[y].AdjacentNodes.iteritems() if p.index not in doneNodes)
            if (len(d) != 0):
                aNode = min(d, key=d.get)
                #print "-- check Node: ", aNode.index
                possiblePaths[tuple([y,aNode.index])] = d[aNode] + shPath[y]
        selectEdge = min(possiblePaths, key=possiblePaths.get)
        nextNodeIndex = selectEdge[1]
        #print "-- select edge: ", y,"->", nextNodeIndex
        shPath[nextNodeIndex] = possiblePaths[selectEdge]
        doneNodes.append(nextNodeIndex)

    #print "shortest paths: ", shPath

'''
============================================================================
// Name        : BELLMAN FORD
// Description :
============================================================================
'''

def calculate_least_adjacent_cost(adjacency_list, i, v, cache):
    adjacent_nodes = adjacency_list[v]

    least_adjacent_cost = float("inf")
    for node in adjacent_nodes:
      adjacent_cost = cache[node["from"]-1] + node["weight"]
      if adjacent_cost < least_adjacent_cost:
        least_adjacent_cost = adjacent_cost
    return least_adjacent_cost


'''
body of the code starts here

'''

#file io
file = open(os.path.dirname(os.path.realpath(__file__)) + "/large.txt")
vertices, edges = map(lambda x: int(x), file.readline().replace("\n", "").split(" "))

#instance of the class object
g = Graph();
startindex = 1
s=0
cache = [[] for j in xrange(vertices+1)]
cache[s] = 0

adjacency_list = [[] for k in xrange(vertices)]
for line in file.readlines():
    tail, head, weight = line.split(" ")
    if int(weight) < 0:
        weightTempInt = int(weight) * -1
    else:
	weightTempInt = int(weight)
    adjacency_list[int(head)-1].append({"from" : int(tail), "weight" : weightTempInt})
    g.addEdge(int(head),int(tail),int(weight))

'''
Start of the Bellman Ford

'''
for v in range(0, vertices):
  if v != s:
    cache[v] = float("inf")

for i in range(1, vertices):
  #print(cache)
  for v in range(0, vertices):
    previous_cache = cache
    least_adjacent_cost = calculate_least_adjacent_cost(adjacency_list, i, v, previous_cache)
    cache[v] = min(previous_cache[v], least_adjacent_cost)

# detecting negative cycles
for v in range(0, vertices):
  previous_cache = copy.deepcopy(cache)
  least_adjacent_cost = calculate_least_adjacent_cost(adjacency_list, i, v, previous_cache)
  cache[v] = min(previous_cache[v], least_adjacent_cost)

if(not cache == previous_cache):
    raise Exception("negative cycle detected")

cache[0] = float("inf")
shortest_path = min(cache)
print("Shortest Path: " + str(shortest_path))
'''
Start of the Dijkstra
'''
#print "Dijkstra algorithm starting from node ", startindex, " ......"
#print g
Dijkstra(g,startindex)
