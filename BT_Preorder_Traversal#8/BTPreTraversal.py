# Given a binary tree, return the preorder traversal of its nodes' values.
# For example:
# Given binary tree {1,#,2,3},return [1,2,3].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
    	result = []
    	self.preTra(root,result)

    	return result

    def preTra(self, node, intArray):
    	if not node:
    		return None
    	val = node.val
    	intArray.append(val)
    	self.preTra(node.left, intArray)
    	self.preTra(node.right, intArray)