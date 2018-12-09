#!/usr/bin/env python3
# gonna make a stupid algorithm 
import json
import sys

num_colors = int(sys.argv[1])
graph = json.loads(input())
num_nodes = len(graph)
def new_colorstack():
    return [i for i in range(0, num_colors)]

class Node():
    def __init__(self):
        self.stack = [i for i in range(0, num_colors)]
        self.neighbors = set()
        self.visited = False
nodes = {int(i): Node() for i, val in graph.items()}

# determine largest start index

# add edges
for k, val in graph.items():
    nodes[int(k)].neighbors = set(val)
# add inbound edges
for k, adj_list in graph.items():
    for endpoint in adj_list:
        nodes[endpoint].neighbors |= {int(k)}

def recursive_color(graph, start_index):
    'determines the color of interconnected nodes'
    node = graph[start_index]
    if node.visited:
        return True
    node.visited = True 
    if node.stack == []:
        'failed because there are no more colors to assign'
        # replenish stack and visited
        node.stack = new_colorstack()
        node.visited = False 
        return False
    # check if visited nodes have same color
    selected_color = False
    while not selected_color:
        selected_color = True
        for neighbor in node.neighbors:
            if graph[neighbor].visited:
                if node.stack == []:
                    "we have a bad assumption"
                    node.stack = new_colorstack()
                    node.visited = False 
                    return False
                if node.stack[0] == graph[neighbor].stack[0]:
                    # contradiction
                    selected_color = False
                    node.stack.pop(0)

    while node.stack != []:
        # top of the stack is the color
        success = True
        for neighbor_index in node.neighbors:
            if not recursive_color(graph, neighbor_index):
                success = False
        if success:
            return True
        node.stack.pop()

    # exhausted all possible colors given current configuration
    node.stack = new_colorstack()
    node.visited = False 
    
    return False

# make a stack of unvisited nodes
graph = {int(k): v for k, v in graph.items()}
unvisited = {k for k, v in graph.items()}
while unvisited != set():
    start_index = max(unvisited)
    # maim start location
    nodes[start_index].stack = [0] #TODO hardcoded
    if not recursive_color(nodes, start_index):
        print('unsatisfiable')
        exit()
    unvisited = unvisited - {k for k, node in nodes.items() if node.visited}

print('satisfiable with %d colors' % num_colors)
for k, node in nodes.items():
    print((k, node.stack[0]))
