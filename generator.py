#!/usr/bin/env python3
import sys
import json
import random

num_nodes = int(sys.argv[1])
probability = int(sys.argv[2])

def generate_graph(num_nodes, probability):
    NodeList = {i: [] for i in range(0, num_nodes) }
    # add edges
    for i in range(0, num_nodes):
        for edge_id in range(0, num_nodes):
            if edge_id != i and (random.randint(0, 100) < probability):
                # add edge between i and edge
                NodeList[i] += [edge_id]
            else:
                pass

    return NodeList
print(json.dumps(generate_graph(num_nodes, probability)))
