'''
============================================================================
// Name        : Dijkstra.py
// Author      : Jinrui Duan
// Version     :
// Copyright   :
// Description : Dijkstra shortest path algorithm implementation
============================================================================
'''
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
    
def wrapper(adjacency_list)
    for adjacent in adjacency_list:
        #first give adjacent to dijkstra
    for tail in dictionary:
	#get the tail pass to Dijkstra

def Dijkstra(Graph, startIndex):
    shPath = {}
    for x in Graph.NodesList.keys():
        shPath[x] = float('Inf')

    shPath[startIndex] = 0
    doneNodes = [startIndex]
    
    num = Graph.numNodes - 1
    
    while (num !=0) :
        print "-- loop: ", num
        num = num - 1
        possiblePaths = {}
        for y in doneNodes:
            d = dict((p,q) for p,q in Graph.NodesList[y].AdjacentNodes.iteritems() if p.index not in doneNodes)
            if (len(d) != 0):
                aNode = min(d, key=d.get)
                print "-- check Node: ", aNode.index
                possiblePaths[tuple([y,aNode.index])] = d[aNode] + shPath[y]
        selectEdge = min(possiblePaths, key=possiblePaths.get)
        nextNodeIndex = selectEdge[1]
        print "-- select edge: ", y,"->", nextNodeIndex
        shPath[nextNodeIndex] = possiblePaths[selectEdge]
        doneNodes.append(nextNodeIndex)
        
    print "shortest paths: ", shPath

g = Graph();

#f = open("data/dijkstraData.txt","r");
print "Creating graph ......"
f = open("Example2.txt","r");
for line in f:
    line = line.split()
    findex = int(line[0])
    for i in range(1,len(line)):
        edge = map(int, line[i].split(','))
        tindex = edge[0]
        distance = edge[1]
        g.addEdge(findex,tindex,distance)

f.close()
startindex = 1
print "Dijkstra algorithm starting from node ", startindex, " ......"
Dijkstra(g,startindex)

