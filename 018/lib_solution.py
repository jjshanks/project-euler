# http://projecteuler.net/problem=18

import networkx as nx

# populate "tree"
tree = []
tree.append([75])
tree.append([95,64])
tree.append([17,47,82])
tree.append([18,35,87,10])
tree.append([20,4,82,47,65])
tree.append([19,1,23,75,3,34])
tree.append([88,2,77,73,7,63,67])
tree.append([99,65,4,28,6,16,70,92])
tree.append([41,41,26,56,83,40,80,70,33])
tree.append([41,48,72,33,47,32,37,16,94,29])
tree.append([53,71,44,65,25,43,91,52,97,51,14])
tree.append([70,11,33,28,77,73,17,78,39,68,17,57])
tree.append([91,71,52,38,17,14,91,43,58,50,27,29,48])
tree.append([63,66,4,68,89,53,67,30,73,16,69,87,40,31])
tree.append([4,62,98,27,23,9,70,98,73,93,38,53,60,4,23])

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
        graph.add_edge(node, node + i + 1, weight=100-bottom_row[pointer])
        graph.add_edge(node, node + i + 2, weight=100-bottom_row[pointer+1])
        node += 1

# add length of last row to node coun since we don't go over it
node += len(tree[-1]) - 1
biggest = 0

# find the shortest path for each "leaf"
for x in tree[-1]:
    path = nx.dijkstra_path(graph, 1, node)
    total = 0
    # for path find total
    for y in path:
        total += graph.node[y]['value']
    if total > biggest:
        biggest = total
    node -= 1

print biggest
