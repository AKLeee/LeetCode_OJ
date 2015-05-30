# Given an array of size n, find the majority element. The majority element is the element that appears more than [n/2] times.

# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
    	if(len(nums) == 1):
    		return nums[0]
    	hashTable = {}
    	for num in nums:
    		if hashTable.get(num):
    			count = hashTable.get(num)
    			hashTable.update({num:count+1})
    			if hashTable.get(num) > len(nums)/2:
    				return num
    		else:   			
    			hashTable.update({num:1})
