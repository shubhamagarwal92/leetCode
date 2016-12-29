from Node import *

def printInorder(root):
	"""
	(Left, Root, Right)
	"""
	if root is None:
		return
	printInorder(root.left)
	print "%d" %(root.data),
	printInorder(root.right)

def printPreorder(root):
	"""
	(Root, Left , Right)
	"""

	if root is None:
		return
	print "%d" %(root.data),
	printInorder(root.left)
	printInorder(root.right)

def printPostorder(root):
	"""
	(Left, Right , Root)
	"""

	if root is None:
		return
	printInorder(root.left)
	printInorder(root.right)
	print "%d" %(root.data),


print "Pre-order traversal of binary tree is -" 
printPreorder(root)
print '\n'
print "In-order traversal of binary tree is -" 
printInorder(root)
print '\n'
print "Post-order traversal of binary tree is -" 
printPostorder(root)
