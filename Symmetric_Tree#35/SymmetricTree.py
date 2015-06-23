# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {boolean}
	def isSymmetric(self, root):
		if not root:
			return True

		if not root.left and not root.right:
			return True
					
		if not root.left or not root.right:
			return False

		level = []
		levelNum = []
		level.append(root.left)
		level.append(root.right)
		levelNum = [root.left.val, root.right.val]
		while len(level) > 0:
			if not self.checkMirror(levelNum):
				return False
			levelNum = []
			lenOfLevel = len(level)
			for idx in range(lenOfLevel):
				node = level.pop(0)
				if node.left:
					level.append(node.left)
					levelNum.append(node.left.val)
				else:
					levelNum.append('#')
				if node.right:
					level.append(node.right)
					levelNum.append(node.right.val)
				else:
					levelNum.append('#')
		return True

	def checkMirror(self,array):
		leftIdx, rightIdx = 0, len(array)-1

		while leftIdx < rightIdx:
			left = array[leftIdx]
			right = array[rightIdx]
			if left != right:
				return False
			else:
				leftIdx += 1
				rightIdx -= 1
		return True

