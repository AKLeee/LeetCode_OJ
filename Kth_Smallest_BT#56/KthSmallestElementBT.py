# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    result = 0
    count = 0
    def kthSmallest(self, root, k):
    	self.count = k
        self.inOrderHelper(root)
        return self.result

    def inOrderHelper(self, root):
    	if root.left:
    		self.inOrderHelper(root.left)
    	self.count -= 1

    	if self.count == 0:
    		self.result = root.val
    		return

    	if root.right:
    		self.inOrderHelper(root.right)