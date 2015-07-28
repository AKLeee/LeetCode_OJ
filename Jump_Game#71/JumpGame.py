# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
    	maxReach = 0
    	for index, num in enumerate(nums):
    		if index > maxReach:
    			return False
    		# index + num indicate the position we can reach from here
    		# maxReach indicate the fartest position we can reach
    		maxReach = max(maxReach, index+num)

    	return True