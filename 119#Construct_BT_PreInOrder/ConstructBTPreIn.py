# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
	    if inorder:
	        ind = inorder.index(preorder.pop(0))
	        root = TreeNode(inorder[ind])
	        root.left = self.buildTree(preorder, inorder[0:ind])
	        root.right = self.buildTree(preorder, inorder[ind+1:])
	        return root


#If given inorder and postorder
# class Solution(object):
#     def buildTree(self, inorder, postorder):
#         """
#         :type inorder: List[int]
#         :type postorder: List[int]
#         :rtype: TreeNode
#         """
#         if inorder:
# 	        ind = inorder.index(postorder.pop())
# 	        root = TreeNode(inorder[ind])
# 	        root.right = self.buildTree(inorder[ind+1:], postorder)
# 	        root.left = self.buildTree(inorder[0:ind], postorder)
# 	        return root
#         