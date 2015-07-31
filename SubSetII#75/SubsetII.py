# Given a collection of integers that might contain duplicates, nums, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
    	result = [[]]
    	if nums is None or len(nums) == 0:
    		return result

    	nums.sort()
    	start = 0
    	for i in range(len(nums)):
    		size = len(result)
    		print size
    		for j in range(start,size):
    			# if use temp = result[j], it will pass the ref to temp
    			# temp.append() will change the result[j] as well
    			temp = []
    			temp.extend(result[j])
    			temp.append(nums[i]) 			
    			result.append(list(temp))

    		# if next number is duplicate, start from last added
    		# in order to skip the same append process again
    		if i<len(nums)-1 and nums[i] == nums[i+1]:
    			start = size
    		else:
    			start = 0

    	return result

if __name__ == '__main__':
	print Solution().subsetsWithDup([1,2,2])