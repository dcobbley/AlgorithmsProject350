def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
    """ calculates a shortest path tree routed in src
    """
    # a few sanity checks
    if src not in graph:
        raise TypeError('the root of the shortest path tree cannot be found in the graph')
    if dest not in graph:
        raise TypeError('the target of the shortest path cannot be found in the graph')
    # ending condition
    if src == dest:
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        print('shortest path: '+str(path)+" cost="+str(distances[dest]))
    else :
        # if it is the initial  run, initializes the cost
        if not visited:
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,dest,visited,distances,predecessors)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    graph = {'1': {'2': 66, '5': 66, '6': 66},
            '2': {'3': 50, '7': 66, '11': 50},
            '3': {'4': 66, '8': 66},
            '4': {'9': 100},
            '5': {'10': 66},
            '6': {'10': 66, '11': 50},
            '7': {'8': 66, '12': 50},
            '8': {'9': 66},
            '10': {'11': 66},
            '11': {'12': 66, '13': 50},
            '12': {'14': 50, '18': 50},
            '13': {'15': 66, '17': 66},
            '14': {'22': 66, '24': 66},
            '15': {'16': 100, '18': 100},
            '16': {'18': 100},
            '17': {'18': 66, '19': 100, '21': 66},
            '18': {'21': 100},
            '19': {'20': 100},
            '20': {'22': 66},
            '21': {'22': 66},
            '22': {'23': 45},
            '23': {'25': 58},
            '24': {'25': 66, '26': 100},
            '25': {'26': 100}}
dijkstra(graph,'1','19')
