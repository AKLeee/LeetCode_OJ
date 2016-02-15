# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, root.val, largerThan) and self.isValidBST(root.right, lessThan, root.val)

#Check during inorder traversal
# class Solution(object):
# 	def isValidBST(self, root):
# 		curMax = float('-inf')
# 		return self.validBST(root, curMax)

# 	def validBST(self, root, curMax):
# 		if not root: return True
# 		if not self.validBST(root.left, curMax): return False
# 		if root.val <= curMax: return False
# 		curMax = root.val
# 		return self.validBST(root.right, curMax)