import os
import copy


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


#file io
file = open(os.path.dirname(os.path.realpath(__file__)) + "/large.txt")
vertices, edges = map(lambda x: int(x), file.readline().replace("\n", "").split(" "))


#data structure creation
s=0
cache = [[] for j in xrange(vertices+1)]
cache[s] = 0

adjacency_list = [[] for k in xrange(vertices)]


#construction for a given set
for line in file.readlines():
    tail, head, weight = line.split(" ")
    if int(weight) < 0:
        weightTempInt = int(weight) * -1
    else:
	weightTempInt = int(weight)
    adjacency_list[int(head)-1].append({"from" : int(tail), "weight" : weightTempInt})

'''
Start of the Bellman Ford

'''
for v in range(0, vertices):
  if v != s:
    cache[v] = float("inf")

for i in range(1, vertices):
  print(cache)
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


