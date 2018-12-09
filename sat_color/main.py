#!/usr/bin/env python
import sys
import json
num_colors = int(sys.argv[1])
graph = json.loads(input())
num_nodes = len(graph)
#print(graph)

var_count = 0
def new_var():
    global var_count
    var_count += 1
    return var_count

class Node():
    def __init__(self):
        self.vars = [new_var() for i in range(0, num_colors)]
        self.constraints = []
        self.color = None

        # handle mutex constraint
        # add case where all true
        self.constraints += [[i for i in self.vars]]

        # n choose 2 permutation
        for i in range(0, len(self.vars)):
            for j in range(i+1, len(self.vars)):
                # permute
                self.constraints += [[-self.vars[i], -self.vars[j]]]
        return

    def add_constraint_edge(self, neighbor):
        for i in range(0, num_colors):
        # a neighbor cannot share the same color as the current node
            self.constraints += [[-self.vars[i], -neighbor.vars[i]]]
        return

    def num_constraints(self):
        return len(self.constraints)

    def num_vars(self):
        return len(self.vars)

    def print_constraints(self):
        for clause in self.constraints:
            for variable in clause:
                print(variable, end=' ')
            print(0)
        return

nodes = {int(i): Node() for i, val in graph.items()}
for node_id, edges in graph.items():
    for edge in edges:
        nodes[int(node_id)].add_constraint_edge(nodes[edge])

# compute the number of clauses
num_constraints = 0
for i in range(0, len(nodes)):
        num_constraints += nodes[i].num_constraints()

# compute the number of variables
num_vars = 0
for i in range(0, len(nodes)):
    num_vars += nodes[i].num_vars()
print('c %d %d' % (num_colors, num_nodes))
print('p cnf %d %d' % (num_vars, num_constraints))

# dump all constraints
for i in range(0, len(nodes)):
    nodes[i].print_constraints()
