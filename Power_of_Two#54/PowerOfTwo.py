# Given an integer, write a function to determine if it is a power of two.

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
    	#Using bit manipulation 'and' to compute n and n-1
        return n > 0 and n&(n-1) == 0