# Given an array and a value, remove all instances of that value in place and return the new length.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution:
	# @param {integer[]} nums
	# @param {integer} val
	# @return {integer}
	def removeElement(self, nums, val):
		i = 0
		for num in nums:
			if num != val:
				nums[i] = num
				i += 1
		return i