# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
    	for idx, num in enumerate(nums):
    		if target <= num:
    			return idx
    		if idx+1 >= len(nums):
    			return idx+1
