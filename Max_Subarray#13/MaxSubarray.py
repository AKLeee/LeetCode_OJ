# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
    	#only ask for max number, don't care details of subarray
    	#so each step we compare 3 things: 
    	#	current num; 
    	#	global max; 
    	#	'what current num affects this contiguous' max.
    	maxResult = nums[0]
    	maxNow = 0

    	for idx,num in enumerate(nums):
    		maxNow = max(nums[idx],maxNow+nums[idx])
    		maxResult = max(maxResult, maxNow)
    	return maxResult