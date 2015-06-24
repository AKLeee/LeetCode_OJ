# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer[][]}
	def levelOrderBottom(self, root):
		result = []
		if root == None:
			return result
		cache = []
		level = []
		array = []
		cache.append(root)
		array.append(root.val)
		result.append(array)
		while len(cache) > 0:
			level = cache
			array = []
			for idx in range(len(level)):
				node = cache.pop(0)
				if node.left:
					cache.append(node.left)
					array.append(node.left.val)
				if node.right:
					cache.append(node.right)
					array.append(node.right.val)
			if len(array) > 0:
				result.insert(0, array)

		#result = reversed(result)
		return result