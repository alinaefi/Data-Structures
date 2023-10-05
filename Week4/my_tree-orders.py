# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Start in-order traversal from the root vertex 0
    self.inOrderTraversal(0)
    return self.result
  
  def preOrder(self):
    self.result = []
    # start pre-order traversal from the root vertex 0
    self.preOrdertraversal(0)
    return self.result

  def postOrder(self):
    self.result = []
    # start post order traversal from the root vertex 0
    self.postOrdertraversal(0)
    return self.result

  def inOrderTraversal(self, root):
    # in-order traversal recursively
    if root == -1:
        return
    self.inOrderTraversal(self.left[root])
    self.result.append(self.key[root])
    self.inOrderTraversal(self.right[root])

  def preOrdertraversal(self, root):
    # pre-order traversal recursively
    if root == -1:
      return
    self.result.append(self.key[root])
    self.preOrdertraversal(self.left[root])
    self.preOrdertraversal(self.right[root])

  def postOrdertraversal(self, root):
    # pre-order traversal recursively
    if root == -1:
      return
    self.postOrdertraversal(self.left[root])
    self.postOrdertraversal(self.right[root])
    self.result.append(self.key[root])
      

def main():
    tree = TreeOrders()
    tree.read()
    in_order = tree.inOrder()
    pre_order = tree.preOrder()
    post_order = tree.postOrder()
    print(" ".join(str(x) for x in in_order))
    print(" ".join(str(x) for x in pre_order))
    print(" ".join(str(x) for x in post_order))

threading.Thread(target=main).start()
