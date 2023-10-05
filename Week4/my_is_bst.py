#!/usr/bin/python3

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
