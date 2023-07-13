# python3
# Task. You are given a description of a rooted tree. Your task is to compute and output its height. Recall
# that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a
# leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.

import sys
import threading
from collections import deque


def compute_height(n, parents):
    # Create list of lists. each list contains children indexes for corresponding parent node
    nodes = [[] for _ in range(n)]
    for child_index, parent_index in enumerate(parents):
        # By the way find and store root
        if parent_index == -1:
            root = child_index
        else:
            nodes[parent_index].append(child_index)


    # Implement BFS to calculate height
    queue = deque([(root, 1)])  # Tuple of node index and its level. Store root tree first
    max_height = 0
    # While queue is not empty
    while queue:
        # Remove last queue item
        node, height = queue.popleft()
        max_height = max(max_height, height)
        # Add other children to the queue
        for child in nodes[node]:
            queue.append((child, height + 1))
    return max_height

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
