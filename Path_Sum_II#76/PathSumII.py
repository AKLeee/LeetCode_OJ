# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import TreeNode

class Solution:
	# @param {TreeNode} root
	# @param {integer} sum
	# @return {integer[][]}

	result = []

	def pathSum(self, root, sum):
		n = 0
		temp = []
		self.dfs(root, sum, n, temp)
		return self.result

	def dfs(self, root, sum, n, temp):
		if root is None:
			return
		n += root.val
		temp.append(root.val)
		if root.left is None and root.right is None:
			if n == sum:
				self.result.append(list(temp))
		else:
			self.dfs(root.left, sum, n, temp)
			self.dfs(root.right, sum, n, temp)
		# remember to reset the temp array
		temp.pop()

if __name__ == '__main__':
	root = TreeNode(1)
	node02 = TreeNode(2)
	node03 = TreeNode(6)
	node04 = TreeNode(4)

	#root.left = node02
	#root.right = node03

	node02.left = node04
	print Solution().pathSum(root, 0)