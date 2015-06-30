# Given an index k, return the kth row of the Pascal's triangle.
# For example, given k = 3,

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
    	result = [1]
    	pre = 1
    	if rowIndex == 0:
    		return result
    	for idx in range(1,rowIndex+1):
    		#print result
    		for index in range(len(result)+1):
    			if index >= len(result):
    				result.append(1)
    				break
    			elif index-1 < 0:
    				result[index] = result[index]
    			else:
    				cache = result[index]
    				#print result[index]
    				result[index] = pre + result[index]
    				pre = cache
    	return result