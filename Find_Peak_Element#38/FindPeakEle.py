# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
    	left, right = 0, len(nums)-1
    	if right == 0:
    		return right
    	if right == 1:
    		return left if nums[left] >= nums[right] else right

    	while left < right:
    		mid = (left+right)/2
    		if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
    			return mid
    		#Because there are multiple peaks, so order is not important
    		if nums[mid] < nums[mid-1]:
    			right = mid-1
    		else:
    			left = mid+1

    	#For last step, if peak is at boundary 
    	if nums[left] > nums[right]:
    		return left
    	else: return right