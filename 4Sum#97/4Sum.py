# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

class Solution(object):
    def fourSum(self, nums, target):
    	result = []
    	if not nums or len(nums) < 4:
    		return result
    	nums = sorted(nums)
    	for i in range(len(nums)-1,1,-1):
    		if i < len(nums)-1 and nums[i] == nums[i+1]:
    			continue
    		threeSumResult = self.threeSum(nums, i-1, target-nums[i])
    		for j in range(len(threeSumResult)):
    			threeSumResult[j].append(nums[i])
    		result.extend(list(threeSumResult))
    	return result

    def threeSum(self, nums, end, target):
    	result = []
    	if not nums or len(nums) < 3:
    		return result
    	#nums = sorted(nums)
    	for i in range(end, 0, -1):
    		if i < end and nums[i] == nums[i+1]:
    			continue
    		twoSumResult = self.twoSum(nums,i-1,target-nums[i])
    		for j in range(len(twoSumResult)):
    			twoSumResult[j].append(nums[i])
    		if len(twoSumResult) != 0:
    			result.extend(list(twoSumResult))
    	return result

    def twoSum(self, nums, end, target):
    	result = []
    	if not nums or len(nums) < 2:
    		return result
    	left = 0
    	right = end
    	while left < right:
    		if nums[left]+nums[right] == target:
    			result.append(list([nums[left],nums[right]]))
    			left += 1
    			right -= 1
    			while left < right and nums[left] == nums[left-1]:
    				left += 1
    			while left < right and nums[right] == nums[right+1]:
    				right -= 1
    		elif nums[left]+nums[right] > target:
    			right -= 1
    		else:
    			left += 1
    	return result

if __name__ == '__main__':
	print Solution().fourSum([0, 0, 0, 0], 0)