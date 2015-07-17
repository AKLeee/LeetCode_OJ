# Given a sorted array of integers, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n)'
# If the target is not found in the array, return [-1, -1].

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
    	#what if there are more than 2 targets
    	#we should choose the smallest and largest index
    	result = []

    	result.append(self.searchLeftMost(nums,target))
    	result.append(self.searchRightMost(nums,target))

    	return result

    def searchLeftMost(self, nums, target):
    	left = 0
    	right = len(nums)-1
    	while left <= right:
    		mid = (left+right)/2
    		if nums[mid] < target:
    			left = mid+1
    		elif nums[mid] > target:
    			right = mid-1
    		else:
    			right = mid-1
    	if left >= 0 and left < len(nums) and nums[left] == target:
    		return left
    	return -1

    def searchRightMost(self, nums, target):
    	left = 0
    	right = len(nums)-1
    	while left <= right:
    		mid = (left+right)/2
    		if nums[mid] < target:
    			left = mid+1
    		elif nums[mid] > target:
    			right = mid-1
    		else:
    			left = mid+1
    	if right >= 0 and right < len(nums) and nums[right] == target:
    		return right
    	return -1

if __name__ == '__main__':
	print Solution().searchRange([1,1,2,2,2,3,4,4,5], 2)

