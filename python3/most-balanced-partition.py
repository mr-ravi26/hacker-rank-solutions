#!/bin/python3
# Author: Ravi Bhushan Tripathi
# Date: 10/21/2020

import math
import os
import random
import re
import sys



#
# Complete the 'mostBalancedPartition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY files_size
#

def calculate_weight(node, adj, files_size):
	queue = [node]
	weight = 0
	while queue:
		index = queue.pop()
		weight += files_size[index]
		if index in adj:
		  queue.extend(adj[index])
	return weight

def mostBalancedPartition(parent, files_size):
    # Write your code here
    # Write your code here


    adj = {}
    edges = []
    for index, p in enumerate(parent):
        edges.append((p, index))
        if p in adj:
            adj[p].append(index)
        else:
            adj[p] = [index]
    
    total_weight = sum(files_size);
    min_diff = sum(files_size);
	
    for e in edges:
        p,c = e
        adj[p].remove(c)
        w1 = calculate_weight(c, adj, files_size)
        min_diff = min(min_diff, abs(total_weight - 2*w1))
        adj[p].append(c)

    return min_diff

if __name__ == '__main__':