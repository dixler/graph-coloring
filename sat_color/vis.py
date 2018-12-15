#!/usr/bin/env python

import sys

num_colors=int(sys.argv[1])
num_nodes=int(sys.argv[2])
is_sat=input()
if is_sat == 'sat':
    print('satisfiable with %d colors' % num_colors)
    sat=[int(i) for i in input().split(' ') if i != '' and int(i) > 0]
    sat=[(i//num_colors, i%num_colors) for i in sat]
    sat[0] = (0, sat[0][1])
    for i, val in enumerate(sat):
        print(val, end=', ')
    exit(-1)
else:
    exit(0)
