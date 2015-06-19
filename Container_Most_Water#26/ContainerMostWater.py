# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container.

class Solution:
	# @param {integer[]} height
	# @return {integer}
	def maxArea(self, height):
		maxResult = 0
		leftIndex = 0
		rightIndex = len(height)-1

		while leftIndex < rightIndex:
			left = height[leftIndex]
			right = height[rightIndex]
			area = (rightIndex-leftIndex)*min(left,right)
			maxResult = max(maxResult,area)
			if left > right:
				rightIndex -= 1
			else:
				leftIndex += 1

		return maxResult