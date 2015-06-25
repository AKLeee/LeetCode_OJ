# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
    	for idx in reversed(range(len(digits))):
    		print idx   		
    		if digits[idx]+1 == 10:
    			if idx == 0:
    				digits[idx] = 0
    				digits.insert(0,1)
    			else:
    				digits[idx] = 0
    		else:
    			digits[idx] = digits[idx] + 1
    			return digits
    	return digits