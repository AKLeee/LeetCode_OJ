#Given an array of integers, every element appears twice except for one. Find that single one.
#Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
    	#Using dictionary to flag each number
    	hashTable = {}
    	for num in nums:
    		if not hashTable.get(num):
    			hashTable.update({num: True})
    		else:
    			hashTable.update({num: False})

    	for key in hashTable:
    		if hashTable.get(key) is True:
    			return key