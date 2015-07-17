# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):

    	return self.genBST(1,n)

    def genBST(self, left, right):
    	result = []
    	if left>right:
    		result.append(None)
    		return result

    	for indexOne in range(left,right+1):
    		leftNodes = self.genBST(left,indexOne-1)
    		rightNodes = self.genBST(indexOne+1,right)
    		for indexTwo in range(len(leftNodes)):
    			for indexThree in range(len(rightNodes)):
    				node = TreeNode(indexOne)
    				node.left = leftNodes[indexTwo]
    				node.right = rightNodes[indexThree]
    				result.append(node)

    	return result