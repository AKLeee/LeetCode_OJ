# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
    	if not root:
    		return 0
    	if not root.left and not root.right:
    		return 1
    	minValue = sys.maxint
    	depth = 0
    	return self.dfs(root, minValue, depth)

    def dfs(self, root, minNum, depth):
    	if root is None:
    		return minNum
    	depth += 1
    	if not root.left and not root.right:
    		return min(minNum, depth)
    	return min(self.dfs(root.left, minNum, depth), self.dfs(root.right, minNum, depth))