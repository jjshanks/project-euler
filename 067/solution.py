# http://projecteuler.net/problem=18

# copied from problem 18 but use NetworkX for shortest path instead which is much faster for larger graphs

import networkx as nx

tree = []

# populate tree
f = open("triangle.txt")
for line in f:
    tree.append(line.split(" "))

graph = nx.DiGraph()
node = 1

graph.add_node(1, value=tree[0][0])
# convert "tree" into graph
for i in xrange(0,len(tree)-1):
    top_row = tree[i]
    bottom_row = tree[i+1]
    for pointer in xrange(0, len(top_row)):
        graph.add_node(node + i + 1, value=bottom_row[pointer])
        graph.add_node(node + i + 2, value=bottom_row[pointer+1])
        # max value is less than 100 so weights are 100-value
        graph.add_edge(node, node + i + 1, weight=100-int(bottom_row[pointer]))
        graph.add_edge(node, node + i + 2, weight=100-int(bottom_row[pointer+1]))
        node += 1

# add length of last row to node coun since we don't go over it
node += len(tree[-1]) - 1
biggest = 0

# find the shortest path for each "leaf"
for x in tree[-1]:
    path = nx.dijkstra_path(graph, 1, node)
    # path = shortest_path(graph, 1, node)
    total = 0
    for y in path:
        total += int(graph.node[y]['value'])
    if total > biggest:
        biggest = total
    node -= 1

print biggest
