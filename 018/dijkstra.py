# Using NetworkX objects calculate shortest path using Dijkstra's algorithm

# Current testing shows this implementation is 10-20% slower than the one provided by NetworkX
# ie: nx.dijkstra_path(graph, start, finish)

import networkx as nx

# given a set of unvisited nodes find node with the shortest distance
def shortestDistance(nodes, distances):
  dis = float("inf")
  node = None
  for n in nodes:
    if distances[n] < dis or node == None:
      node = n
      dis = distances[n]
  return node

# given a start, finish, and shortest previous node map find the shortest path
def get_path(start, finish, previous):
  path = [finish]
  current = finish
  while current != start:
      path.append(previous[current])
      current = previous[current]
  path.reverse()
  return path

# for given graph, start node, and finish node, return shortest path
def shortest_path(graph, start, finish):
  visited = [start]
  
  distances = {}
  previous = {}
  nodes = graph.nodes()

  # initialize distance and previous map
  for v in graph.nodes():
    distances[v] = float("inf")
    previous[v] = None

  # distance to start node is 0
  distances[start] = 0

  while len(nodes) > 0:
    unvisited = shortestDistance(nodes, distances)
    nodes.remove(unvisited)
    
    # remaining nodes are unreachable  
    if distances[unvisited] == float("inf"):
      break

    # if we have reached the final node we are done
    if unvisited == finish:
      break
    
    # check each connected node
    for n in graph[unvisited]:
      # calculate distance to node from unvisited node
      alt_dist = distances[unvisited] + graph[unvisited][n]['weight']
      # if new distance is shorter than exist min update distance value and previous value map
      if alt_dist < distances[n]:
        distances[n] = alt_dist
        previous[n] = unvisited
  
  return get_path(start, finish, previous)

