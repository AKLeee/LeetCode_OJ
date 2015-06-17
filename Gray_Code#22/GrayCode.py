# The gray code is a binary numeral system where two successive values differ in only one bit.

# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
    	result = [0]
    	for idx in range(n):
    		temp = result
    		for num in reversed(temp):
    			result.append(num + 2**idx)

    	return result