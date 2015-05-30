# Given an array of size n, find the majority element. The majority element is the element that appears more than [n/2] times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# ---Using hashtable Time O(n) Space O(n)---
# class Solution:
#     # @param {integer[]} nums
#     # @return {integer}
#     def majorityElement(self, nums):
#     	if(len(nums) == 1):
#     		return nums[0]
#     	hashTable = {}
#     	for num in nums:
#     		if hashTable.get(num):
#     			count = hashTable.get(num)
#     			hashTable.update({num:count+1})
#     			if hashTable.get(num) > len(nums)/2:
#     				return num
#     		else:   			
#     			hashTable.update({num:1})

# ---Using Moore Voting algorithm O(n)---
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
    	candidate = None
    	count = 0
    	for num in nums:
    		if count == 0:
    			candidate = num
    			count = 1
    		else:
    			if num == candidate:
    				count += 1
    			else:
    				count -= 1
    	return candidate