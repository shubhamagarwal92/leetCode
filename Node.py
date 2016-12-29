class Node:
	def __init__(self,key):
		self.data = key
		self.left = None
		self.right = None

"""
Constructed Binary tree is:
	     1
       /   \
      2      3
    /  \      \
   4    5      8
 
"""


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)

