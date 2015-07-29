# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
    	if len(nums) < 3:
    		return None
    	minDiff = sys.maxint
    	nums.sort()
    	for index in range(len(nums)-2):
    		left = index+1
    		right = len(nums)-1
    		while left<right:
    			diff = nums[index]+nums[left]+nums[right]-target
    			if abs(minDiff) > abs(diff):
    				minDiff = diff
    			if diff == 0:
    				break
    			elif diff < 0:
    				left += 1
    			else:
    				right -= 1

    	return target+minDiff