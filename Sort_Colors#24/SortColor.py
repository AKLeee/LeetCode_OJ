# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
    	redCount, whiteCount, blueCount = 0, 0, 0
    	for num in nums:
    		if num == 0:
    			redCount += 1
    		if num == 1:
    			whiteCount += 1
    		if num == 2:
    			blueCount += 1
    	index = 0
    	for idx in range(redCount):
    		nums[idx] = 0
    		index += 1
    	widx = index
    	for idx in range(whiteCount):
    		nums[widx+idx] = 1
    		index += 1
    	bidx = index
    	for idx in range(blueCount):
    		nums[bidx+idx] = 2