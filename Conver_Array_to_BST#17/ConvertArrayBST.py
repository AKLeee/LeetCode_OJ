# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import TreeNode

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
    	if len(nums) == 0:
    		return None
    	root = TreeNode(0)
    	left = 0
    	right = len(nums)-1
    	root = self.convert(nums,left,right,root)
    	return root

    def convert(self,nums,left,right,node):
    	if left > right:
    		return
    	mid = (left+right)/2
    	node = TreeNode(nums[mid])
    	leftNode = TreeNode(0)
    	rightNode = TreeNode(0)
    	node.left = self.convert(nums,left,mid-1,leftNode)
    	node.right = self.convert(nums,mid+1,right,rightNode)
    	return node