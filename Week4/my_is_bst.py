"""Is it a binary search tree?
Problem Introduction
In this problem you are going to test whether a binary search tree data structure from some programming
language library was implemented correctly. There is already a program that plays with this data structure
by inserting, removing, searching integers in the data structure and outputs the state of the internal binary
tree after each operation. Now you need to test whether the given binary tree is indeed a correct binary
search tree. In other words, you want to ensure that you can search for integers in this binary tree using
binary search through the tree, and you will always get correct result: if the integer is in the tree, you will
find it, otherwise you will not.
Problem Description
Task. You are given a binary tree with integers as its keys. You need to test whether it is a correct binary
search tree. The definition of the binary search tree is the following: for any node of the tree, if its
key is 𝑥, then for any node in its left subtree its key must be strictly less than 𝑥, and for any node in
its right subtree its key must be strictly greater than 𝑥. In other words, smaller elements are to the
left, and bigger elements are to the right. You need to check whether the given binary tree structure
satisfies this condition. You are guaranteed that the input contains a valid binary tree. That is, it is a
tree, and each node has at most two children.
Input Format. The first line contains the number of vertices 𝑛. The vertices of the tree are numbered
from 0 to 𝑛 − 1. Vertex 0 is the root.
The next 𝑛 lines contain information about vertices 0, 1, ..., 𝑛−1 in order. Each of these lines contains
three integers 𝑘𝑒𝑦𝑖, 𝑙𝑒𝑓 𝑡𝑖 and 𝑟𝑖𝑔ℎ𝑡𝑖 — 𝑘𝑒𝑦𝑖
is the key of the 𝑖-th vertex, 𝑙𝑒𝑓 𝑡𝑖
is the index of the left
child of the 𝑖-th vertex, and 𝑟𝑖𝑔ℎ𝑡𝑖
is the index of the right child of the 𝑖-th vertex. If 𝑖 doesn’t have
left or right child (or both), the corresponding 𝑙𝑒𝑓 𝑡𝑖 or 𝑟𝑖𝑔ℎ𝑡𝑖 (or both) will be equal to −1.
Constraints. 0 ≤ 𝑛 ≤ 105; −2
31 < 𝑘𝑒𝑦𝑖 < 2
31 − 1; −1 ≤ 𝑙𝑒𝑓 𝑡𝑖
, 𝑟𝑖𝑔ℎ𝑡𝑖 ≤ 𝑛 − 1. It is guaranteed that the
input represents a valid binary tree. In particular, if 𝑙𝑒𝑓 𝑡𝑖 ̸= −1 and 𝑟𝑖𝑔ℎ𝑡𝑖 ̸= −1, then 𝑙𝑒𝑓 𝑡𝑖 ̸= 𝑟𝑖𝑔ℎ𝑡𝑖.
Also, a vertex cannot be a child of two different vertices. Also, each vertex is a descendant of the root
vertex. All keys in the input will be different.
Output Format. If the given binary tree is a correct binary search tree (see the definition in the problem
description), output one word “CORRECT” (without quotes). Otherwise, output one word “INCORRECT” (without quotes)."""

import sys, threading

sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if tree == []:
    return True
  # perform in order traversal and store in result
  # if the result is sorted, it is a binary search tree
  result = []
  InOrderTraversal(tree, tree[0], result)
  c = result.copy()
  c.sort()
  if c == result:
    return True
  return False


def node_key(node):
  return node[0]

def node_left_index(node):
  if node[1] == -1:
    return None
  return node[1]

def node_right_index(node):
  if node[2] == -1:
    return None
  return node[2]

def InOrderTraversal(tree, root, result):
  # if no left child, print current node
  if node_left_index(root) == None and node_right_index(root) == None:
    result.append(node_key(root))
    return
  if node_left_index(root) != None:
    InOrderTraversal(tree, tree[node_left_index(root)], result)
  result.append(node_key(root))
  if node_right_index(root) != None:
    InOrderTraversal(tree, tree[node_right_index(root)], result)


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
