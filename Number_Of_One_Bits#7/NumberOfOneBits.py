class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
    	s = bin(n)[2:]
    	count = 0
    	for c in s:
    		if c == '1':
    			count += 1
    	return count