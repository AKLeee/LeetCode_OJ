#Given two binary trees, write a function to check if they are equal or not.
#Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param {TreeNode} p
	# @param {TreeNode} q
	# @return {boolean}
	def isSameTree(self, p, q):
		if not p and not q:
			return True
		if not p and q:
			return False
		if p and not q:
			return False
		if p.val != q.val:
			return False

		queueOne = []
		queueTwo = []

		queueOne.append(p)
		queueTwo.append(q)

		while len(queueOne)>0 or len(queueTwo)>0:
			if len(queueOne) != len(queueTwo):
				return False
			currentNodeOne = queueOne.pop(0)
			currentNodeTwo = queueTwo.pop(0)
			if currentNodeOne.val != currentNodeTwo.val:
				return False
			if currentNodeOne.left and currentNodeTwo.left:
				queueOne.append(currentNodeOne.left)
				queueTwo.append(currentNodeTwo.left)
			elif not currentNodeOne.left and not currentNodeTwo.left:
				pass
			else:
				return False
			if currentNodeOne.right and currentNodeTwo.right:
				queueOne.append(currentNodeOne.right)
				queueTwo.append(currentNodeTwo.right)
			elif not currentNodeOne.right and not currentNodeTwo.right:
				pass
			else:
				return False
		return True

