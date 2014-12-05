import sys

test = 0
use = []
countForPat = 0
totalDelay = 0
linkLength = []
linkCap = []
costToTarget = 0

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None
        #Link length
        self.length = sys.maxint

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def ver_reset(self):
        self.__init__(self)

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def set_length(self, len):
        self.length = len

    def rset_visited(self):
        self.visited = False

    def get_length(self):
        return self.length

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
        #self.vert_dict

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    global test
    global costToTarget
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


def delayLink():
    global totalDelay
    global linkLength


    Ti = 1500
    Dpq = 0.78
    delta = (1/((26*(26-1))*Dpq))
    #Fij = 1000000
    counter = 0
    while counter < 38:
        Cij = float(linkCap[counter])
        Fij = use[counter] * Dpq * (1500*8)
        Pij = float(linkLength[counter]) * 0.000005
        stdDiv = Fij/L
        dlink = 1/((Fij / (Cij - Fij)) + ((Pij + Ti)*(Fij / L)))
        totalDelay += dlink
        #print "Link delay for link " + str(counter) + ": " + str(dlink) + "secs"

        if dlink > 0:
            print "Link delay for link " + str(counter) + ": " + str(dlink) + "secs"
        else:
            print "Infinite Capcity"

        if Cij <= Fij:
            print "Link Capacity greater than flow for link"
        counter += 1
    #return dlink

import heapq

def dijkstra(aGraph, start):
    print '''Dijkstra's shortest path for node ''' + start.get_id()
    # Set the distance for the start node to zero
    start.set_distance(0)
    cost = 100000000

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()


        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip

            if next.visited:
                continue

            new_dist = current.get_distance() + (cost/current.get_weight(next))

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                #print 'updated : current = %s next = %s new_dist = %s' \
                        #%(current.get_id(), next.get_id(), next.get_distance())
            #else:
                  #print 'not updated : current = %s next = %s new_dist = %s' \
                        #%(current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)

        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
    return next.get_distance()


def readFile():
    global linkLength
    global linkCap
    f = open('USA.txt')
    lines = f.readlines()
    f.close()

    current = 1
    while current < len(lines):
        line = lines[current].split("\\s")
        line = " ".join(line[0].split())
        line = line.split(" ")
        linkCap.append(line[2])
        linkLength.append(line[3])
        current += 1


def gINIT():
    Matrix = [[0 for q in range(5)] for q in range(5)]
    g = Graph()
    for xx in xrange(1, 27):
        g.add_vertex(str(xx))
    g.add_edge('1', '2', 1500000)
    g.add_edge('1', '5', 1500000)
    g.add_edge('1', '6', 1500000)
    g.add_edge('2', '3', 2000000)
    g.add_edge('2', '7', 1500000)
    g.add_edge('2', '11', 2000000)
    g.add_edge('3', '4', 1500000)
    g.add_edge('3', '8', 1500000)
    g.add_edge('4', '9', 1000000)
    g.add_edge('5', '10', 1500000)
    g.add_edge('6', '10', 1500000)
    g.add_edge('6', '11', 2000000)
    g.add_edge('7', '8',  1500000)
    g.add_edge('7', '12', 2000000)
    g.add_edge('8', '9',  1500000)
    g.add_edge('10', '11', 1500000)
    g.add_edge('11', '12', 1500000)
    g.add_edge('11', '13', 2000000)
    g.add_edge('12', '14', 2000000)
    g.add_edge('12', '18', 2000000)
    g.add_edge('13', '15', 1500000)
    g.add_edge('13', '17', 1500000)
    g.add_edge('14', '22', 1500000)
    g.add_edge('14', '24', 1500000)
    g.add_edge('15', '16', 1000000)
    g.add_edge('15', '18', 1000000)
    g.add_edge('16', '18', 1000000)
    g.add_edge('17', '18', 1500000)
    g.add_edge('17', '19', 1000000)
    g.add_edge('17', '21', 1500000)
    g.add_edge('18', '21', 1000000)
    g.add_edge('19', '20', 1000000)
    g.add_edge('20', '22', 1500000)
    g.add_edge('21', '22', 1500000)
    g.add_edge('22', '23', 2200000)
    g.add_edge('23', '25', 1700000)
    g.add_edge('24', '25', 1500000)
    g.add_edge('24', '26', 1000000)
    g.add_edge('25', '26', 1000000)
    return g

def linkUsage(p):
    global use
    global countForPat
    lengthOfP = int(len(p))
    o = 0
    while o < len(p)-1:
        if len(p) != 1:
            countForPat += 1
            if (p[o] == '1' and p[o+1] == '2') or (p[o] == '2' and p[o+1] == '1'):
                use[0] += 1
            elif (p[o] == '1' and p[o+1] == '5') or (p[o] == '5' and p[o+1] == '1'):
                use[1] += 1
            elif (p[o] == '1' and p[o+1] == '6') or (p[o] == '6' and p[o+1] == '1'):
                use[2] += 1
            elif (p[o] == '2' and p[o+1] == '3') or (p[o] == '3' and p[o+1] == '2'):
                use[3] += 1
            elif (p[o] == '2' and p[o+1] == '7') or (p[o] == '7' and p[o+1] == '2'):
                use[4] += 1
            elif (p[o] == '2' and p[o+1] == '11') or (p[o] == '11' and p[o+1] == '2'):
                use[5] += 1
            elif (p[o] == '3' and p[o+1] == '4') or (p[o] == '4' and p[o+1] == '3'):
                use[6] += 1
            elif (p[o] == '3' and p[o+1] == '8') or (p[o] == '8' and p[o+1] == '3'):
                use[7] += 1
            elif (p[o] == '4' and p[o+1] == '9') or (p[o] == '9' and p[o+1] == '4'):
                use[8] += 1
            elif (p[o] == '5' and p[o+1] == '10') or (p[o] == '10' and p[o+1] == '5'):
                use[9] += 1
            elif (p[o] == '6' and p[o+1] == '10') or (p[o] == '10' and p[o+1] == '6'):
                use[10] += 1
            elif (p[o] == '6' and p[o+1] == '11') or (p[o] == '11' and p[o+1] == '4'):
                use[11] += 1
            elif (p[o] == '7' and p[o+1] == '8') or (p[o] == '8' and p[o+1] == '7'):
                use[12] += 1
            elif (p[o] == '7' and p[o+1] == '12') or (p[o] == '12' and p[o+1] == '7'):
                use[13] += 1
            elif (p[o] == '8' and p[o+1] == '9') or (p[o] == '9' and p[o+1] == '8'):
                use[14] += 1
            elif (p[o] == '10' and p[o+1] == '11') or (p[o] == '4' and p[o+1] == '3'):
                use[15] += 1
            elif (p[o] == '11' and p[o+1] == '12') or (p[o] == '12' and p[o+1] == '11'):
                use[16] += 1
            elif (p[o] == '11' and p[o+1] == '13') or (p[o] == '13' and p[o+1] == '11'):
                use[17] += 1
            elif (p[o] == '12' and p[o+1] == '14') or (p[o] == '14' and p[o+1] == '12'):
                use[18] += 1
            elif (p[o] == '12' and p[o+1] == '18') or (p[o] == '18' and p[o+1] == '12'):
                use[19] += 1
            elif (p[o] == '13' and p[o+1] == '15') or (p[o] == '15' and p[o+1] == '13'):
                use[20] += 1
            elif (p[o] == '13' and p[o+1] == '17') or (p[o] == '17' and p[o+1] == '13'):
                use[21] += 1
            elif (p[o] == '14' and p[o+1] == '22') or (p[o] == '14' and p[o+1] == '22'):
                use[22] += 1
            elif (p[o] == '14' and p[o+1] == '24') or (p[o] == '24' and p[o+1] == '14'):
                use[23] += 1
            elif (p[o] == '15' and p[o+1] == '16') or (p[o] == '16' and p[o+1] == '15'):
                use[24] += 1
            elif (p[o] == '15' and p[o+1] == '18') or (p[o] == '18' and p[o+1] == '15'):
                use[25] += 1
            elif (p[o] == '16' and p[o+1] == '18') or (p[o] == '18' and p[o+1] == '16'):
                use[26] += 1
            elif (p[o] == '17' and p[o+1] == '18') or (p[o] == '18' and p[o+1] == '17'):
                use[27] += 1
            elif (p[o] == '17' and p[o+1] == '21') or (p[o] == '21' and p[o+1] == '17'):
                use[28] += 1
            elif (p[o] == '18' and p[o+1] == '21') or (p[o] == '21' and p[o+1] == '18'):
                use[29] += 1
            elif (p[o] == '19' and p[o+1] == '20') or (p[o] == '20' and p[o+1] == '19'):
                use[30] += 1
            elif (p[o] == '20' and p[o+1] == '22') or (p[o] == '22' and p[o+1] == '20'):
                use[31] += 1
            elif (p[o] == '21' and p[o+1] == '22') or (p[o] == '22' and p[o+1] == '21'):
                use[32] += 1
            elif (p[o] == '22' and p[o+1] == '23') or (p[o] == '23' and p[o+1] == '22'):
                use[33] += 1
            elif (p[o] == '23' and p[o+1] == '25') or (p[o] == '25' and p[o+1] == '23'):
                use[34] += 1
            elif (p[o] == '24' and p[o+1] == '25') or (p[o] == '25' and p[o+1] == '24'):
                use[35] += 1
            elif (p[o] == '24' and p[o+1] == '26') or (p[o] == '26' and p[o+1] == '24'):
                use[36] += 1
            elif (p[o] == '25' and p[o+1] == '26') or (p[o] == '26' and p[o+1] == '25'):
                use[37] += 1
        o += 1

import time

if __name__ == '__main__':
    global use
    uu = 0
    while uu < 38:
        use.append(0)
        uu += 1
    readFile()
    start = time.time()
    L = 1500  # length of packet in bytes
    processDelay = 0.0001  # processing delay 1msec
    propDelay = 0.000005  # prop delay
    dpq = 0.92  # average traffic
    cost = 100000000  # base cost
    #Cij = []

    """
    Delay equation
    D(F) = 1/o SUM ((Fij/(Cij - Fij)) + (Pij + Ti)(Fij/L))
    O = Sum pEN Sum qEN dpq
    """
    N = 26

    #dijkstra(g, g.get_vertex('9'))
    #dijkstra(g, g.get_vertex('2'))
    """
    print 'Graph data:'
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))
    """
    temp = 0
    for x in xrange(1, 27):
        gtemp = gINIT()
        temp = dijkstra(gtemp, gtemp.get_vertex(str(x)))
        for y in xrange(1, 27):
            target = gtemp.get_vertex(str(y))
            path = [target.get_id()]
            shortest(target, path)
            linkUsage(path)
            print 'The shortest path : %s with cost of %s' % (path[::-1], temp)

    """
    target = g.get_vertex('11')
    path = [target.get_id()]
    shortest(target, path)
    print 'The shortest path : %s' %(path[::-1])"""
    delta = (1/((N*(N-1))*dpq))  # n(n-1)dpq
    print "Delta = " + str(delta)
    finish = time.time() - start
    print "Time taken: " + str(finish)
    print "Total flows: " + str(countForPat)
    delayLink()
    print "Total Delay in the network " + str(totalDelay)





