# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    result = 0
    def sumNumbers(self, root):
    	result = 0
    	cache = []
    	self.dfs(root, cache)
    	return self.result

    def dfs(self, root, array):
    	if root is None:
    		return
    	array.append(root.val)
    	if not root.left and not root.right:
    		s = ''
    		for n in array:
    			s += str(n)
    		self.result += int(s)
    		print int(s)
    		array.pop()
    		return
    	self.dfs(root.left, array)
    	self.dfs(root.right, array)
    	array.pop()