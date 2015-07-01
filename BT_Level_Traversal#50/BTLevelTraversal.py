# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
    	result = []
    	if not root:
    		return result
    	queue = []
    	array = []
    	queue.append(root)
    	array.append(root.val)
    	while len(queue) > 0:
    		result.append(array)
    		array = []
    		for idx in range(len(queue)):
    			node = queue.pop(0)
    			if node.left:
    				queue.append(node.left)
    				array.append(node.left.val)
    			if node.right:
    				queue.append(node.right)
    				array.append(node.right.val)
    	return result