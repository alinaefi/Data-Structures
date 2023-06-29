# python3

import sys
import threading


def compute_height(n, parents):
    # Create an empty list of nodes, where each index corresponds to a node
    nodes = [[] for _ in range(n)]

    # Fill the nodes list with children for each parent
    for child_index, parent_index in enumerate(parents):
        if parent_index == -1: # A parent index of -1 indicates the root node
            root = child_index
        else:
            nodes[parent_index].append(child_index)
    
    # Define a recursive function to compute the height of a given node
    def compute_node_height(node_index):
        # The height of a node is the maximum height of its children + 1
        children = nodes[node_index]
        if len(children) == 0: # The node is a leaf (it has no children)
            return 1
        else:
            return 1 + max(compute_node_height(child) for child in children)
    
    # Compute and return the height of the tree
    return compute_node_height(root)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
