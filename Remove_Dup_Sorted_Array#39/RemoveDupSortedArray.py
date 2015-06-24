# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
    	if len(nums) == 0:
    		return 0
    	newIdx = 0
    	first = nums[0]
    	for idx in range(len(nums)):
    		if idx+1 == len(nums):
    			if first == nums[idx]:
    				return newIdx+1
    			else:
    				newIdx += 1
    				nums[newIdx] = nums[idx]
    				return newIdx+1
    		if first == nums[idx]:
    			continue
    		else:
    			newIdx += 1
    			nums[newIdx] = nums[idx]
    			first = nums[idx]