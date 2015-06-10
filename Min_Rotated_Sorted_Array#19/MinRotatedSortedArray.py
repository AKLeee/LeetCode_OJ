# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# Find the minimum element.

# You may assume no duplicate exists in the array.

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
    	ac = False
    	dc = False
    	if len(nums) == 0:
    		return None

    	if len(nums)<=3:
    		if len(nums) == 1:
    			return nums[0]
    		if len(nums) == 2 and nums[0] > nums[1]:
    			return nums[1]
    		if len(nums) == 2 and nums[0] < nums[1]:
    			return nums[0]
    		if nums[0] < nums[1] and nums[1] < nums[2]:
    			return nums[0]
    		if nums[0] > nums[1] and nums[1] > nums[2]:
    			return nums[2]

    	if nums[0] < nums[1] and nums[1] < nums[2]:
    		ac = True
    	if nums[0] > nums[1] and nums[1] > nums[2]:
    		dc = True
    	if nums[0] > nums[1] and nums[1] < nums[2]:
    		return nums[1]
    	if nums[0] < nums[1] and nums[1] > nums[2]:
    		return nums[2]

    	if ac is True:
    		first = nums[0]
    		before = nums[0]
    		for num in nums:
    			if num < before:
    				return num
    			before = num
    		return first
    	if dc is True:
    		before = num[0]
    		for num in nums:
    			if num > before:
    				return before
    			before = num
    		return num

