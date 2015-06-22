# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        result = []
    	self.postTra(root,result)

    	return result

    def postTra(self, node, intArray):
    	if not node:
    		return None
    	self.postTra(node.left, intArray)
    	self.postTra(node.right, intArray)
    	val = node.val
        intArray.append(val)