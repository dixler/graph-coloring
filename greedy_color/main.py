#!/usr/bin/env python3
# gonna make a stupid algorithm 
import json
import sys

num_colors = 0
graph = json.loads(input())
num_nodes = len(graph)

class Node():
    def __init__(self):
        self.color = None
        self.neighbors = set()
nodes = {int(i): Node() for i, val in graph.items()}

# add edges to graph
for k, val in graph.items():
    nodes[int(k)].neighbors = set(val)
# add inbound edges
for k, adj_list in graph.items():
    for endpoint in adj_list:
        nodes[endpoint].neighbors |= {int(k)}

def recursive_color(graph, start_index):
    'determines the color of interconnected nodes'
    global num_colors

    node = graph[start_index]
    if node.color != None:
        'we already colored it'
        return
    else:
        neighbor_colors = {graph[neighbor_id].color for neighbor_id in node.neighbors}
        new_color_id = 0
        while new_color_id in neighbor_colors:
            new_color_id += 1
        node.color = new_color_id
        num_colors = max(num_colors, new_color_id+1)
        for neighbor_id in node.neighbors:
            recursive_color(graph, neighbor_id)
        return

# make a stack of unvisited nodes
graph = {int(k): v for k, v in graph.items()}
unvisited = {k for k, v in graph.items()}

while unvisited != set():
    start_index = max(unvisited)
    recursive_color(nodes, start_index)
    unvisited = unvisited - {k for k, node in nodes.items() if node.color != None}

print('satisfiable with %d colors' % num_colors)
for k, node in nodes.items():
    print((k, node.color), end=',  ')
