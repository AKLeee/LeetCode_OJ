# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def zigzagLevelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		result = []
		if root is None:
			return result
		curLevel = []
		nextLevel = []
		curLevel.append(root)
		leftToright = True

		while len(curLevel) != 0:
			curLevelValues = []
			while len(curLevel)!= 0:
				cur = curLevel[-1]
				curLevel.pop()
				curLevelValues.append(cur.val)

				if leftToright:
					if cur.left is not None:
						nextLevel.append(cur.left)
					if cur.right is not None: 
						nextLevel.append(cur.right)
				else:
					if cur.right is not None: nextLevel.append(cur.right)
					if cur.left is not None: nextLevel.append(cur.left)
			result.append(curLevelValues)
			curLevel, nextLevel = nextLevel, curLevel

			leftToright = not leftToright

		return result