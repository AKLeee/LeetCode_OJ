# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
    	if len(nums) == 0:
    		return 0
    	newIdx = 0
    	first = nums[0]
    	flag = 0
    	for idx in range(len(nums)):
    		#print newIdx
    		if idx+1 == len(nums):
    			if first == nums[idx]:
    				if flag >= 2:
    					return newIdx
    				else:
    					nums[newIdx] = nums[idx]
    					return newIdx+1
    			else:
    				nums[newIdx] = nums[idx]
    				return newIdx+1
    		if first == nums[idx]:
    			if flag >= 2:
    				continue
    			else:
    				flag += 1
    				nums[newIdx] = nums[idx]
    				newIdx += 1
    				first = nums[idx]
    		else:
    			nums[newIdx] = nums[idx]
    			first = nums[idx]
    			newIdx += 1
    			flag = 1