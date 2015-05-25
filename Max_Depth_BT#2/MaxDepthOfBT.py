#Given a binary tree, find its maximum depth.
#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer}
	def maxDepth(self, root):
		maxDep = 0
		if not root:
			return 0
		queue = []
		queue.append(root)
		
		while len(queue)>0:
			maxDep = maxDep + 1
			#using extra memory to store nodes on each levels
			level = []
			for node in queue:
				if node.left is not None:
					level.append(node.left)
				if node.right is not None:
					level.append(node.right)
			queue = level
		return maxDep