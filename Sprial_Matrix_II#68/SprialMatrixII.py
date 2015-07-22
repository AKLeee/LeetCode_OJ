# # Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# # For example,
# # Given n = 3

# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
    	result = [[0] * n for i in range(n)]
    	levelNum = n/2
    	val = 1

    	for lvl in range(levelNum):
    		last = n-1-lvl
    		for index in range(lvl, last):
    			result[lvl][index] = val
    			val += 1
    		for index in range(lvl, last):
    			result[index][last] = val
    			val += 1
    		for index in range(last,lvl,-1):
    			result[last][index] = val
    			val += 1
    		for index in range(last,lvl,-1):
    			result[index][lvl] = val
    			val += 1

    	if n%2 == 1:
    		result[n/2][n/2] = val

    	return result

if __name__ == '__main__':
	print Solution().generateMatrix(2)
