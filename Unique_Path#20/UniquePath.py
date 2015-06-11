# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    cache = {}

    def uniquePaths(self, m, n):
    	return self.count(m,n)

    def count(self, m, n):
    	if (m,n) in self.cache:
    		return self.cache[(m,n)]
    	if m < 1 or n < 1:
    		return 0
    	if m == 1 and n == 1:
    		return 1
    	self.cache[(m,n)] = self.count(m-1,n) + self.count(m,n-1)
    	return self.cache[(m,n)]