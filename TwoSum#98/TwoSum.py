# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution(object):
    def twoSum(self, nums, target):
    	dic = {}
    	for index, num in enumerate(nums):
    		diff = target - num
    		if diff in dic:
    			result = [dic.get(diff)+1, index+1]
    			return result
    		else:
    			dic.update({num:index})
    	return None
    	# if len(nums) < 2:
    	# 	return None
    	# sortNums = sorted(nums)
    	# start = 0
    	# end = len(nums)-1
    	# while start < end:
    	# 	add = sortNums[start] + sortNums[end]
    	# 	if add == target:

    	# 		return {nums.get, end+1}
    	# 	if add < target:
    	# 		start += 1
    	# 	if add > target:
    	# 		end -= 1
    	# return None

if __name__ == '__main__':
	print Solution().twoSum({3,2,4},6)