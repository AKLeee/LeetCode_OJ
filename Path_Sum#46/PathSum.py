# # Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
class Solution:

	def hasPathSum(self, root, sum):
		n = 0
		return self.dfs(root, n, sum)

	def dfs(self, root, n, sum):
		if root is None:
			return False
		n += root.val
		if not root.left and not root.right:
			print n
			if n == sum:
				return True
			return False
		return self.dfs(root.left, n, sum) or self.dfs(root.right, n, sum)

# class Solution:
#     # @param {TreeNode} root
#     # @param {integer} sum
#     # @return {boolean}

#     allPathSum = []

#     def hasPathSum(self, root, sum):
#     	cache =[]
#     	self.dfs(root, cache)
#     	print self.allPathSum
#     	return self.hasNum(sum)


#     def dfs(self, root, array):
#     	if root is None:
#     		return
#     	array.append(root.val)
#     	if not root.left and not root.right:
#     		num = 0
#     		for n in array:
#     			num += n
#     		self.allPathSum.append(num)
#     		array.pop()
#     		return
#     	self.dfs(root.left, array)
#     	self.dfs(root.right, array)
#     	array.pop()

#     def hasNum(self, num):
#     	for n in self.allPathSum:
#     		if n == num:
#     			return True
#     	return False