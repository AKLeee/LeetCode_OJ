# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
    	cache = []
    	for xidx in range(len(matrix)):
    		for yidx in range(len(matrix[0][:])):
    			if matrix[xidx][yidx] == 0:
    				point = [xidx,yidx]
    				cache.append(point)
    	for point in cache:
    		for y in range(len(matrix[0][:])):
    		   	matrix[point[0]][y] = 0
    		for x in range(len(matrix)):
				matrix[x][point[1]] = 0