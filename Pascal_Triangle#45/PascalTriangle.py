# Given numRows, generate the first numRows of Pascal's triangle.

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
    	result = []
    	if numRows == 0:
    		return result
    	result.append([1])
    	for num in range(1,numRows):
    		array = [1]
    		if numRows == 2:
    			array = [1,1]
    			result.append(array)
    			return result
    		elif num > 1:
    			for idx in range(0,num-1):
    				array.append(result[num-1][idx] + result[num-1][idx+1])
    		array.append(1)
    		result.append(array)
    	return result