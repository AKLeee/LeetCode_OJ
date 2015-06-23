# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
    	if matrix is None:
    		return False
    	lowM, highM = 0, len(matrix)-1
    	lowR, highR = 0, len(matrix[0][:])-1
    	row = self.helperM(matrix, lowM, highM, target)
    	return self.helperR(row, lowR, highR, target)

    def helperM(self, matrix, lowIdx, highIdx, target):
    	if lowIdx > highIdx:
    		return None
    	midIdx = (lowIdx+highIdx)/2
    	length = len(matrix[0][:])
    	if target < matrix[midIdx][length-1] and target > matrix[midIdx][0]:
    		return matrix[midIdx][:]
    	if target == matrix[midIdx][length-1] or target == matrix[midIdx][0]:
    		return matrix[midIdx][:]
    	if target > matrix[midIdx][length-1]:
    		return self.helperM(matrix, midIdx+1, highIdx, target)
    	if target < matrix[midIdx][0]:
    		return self.helperM(matrix, lowIdx, midIdx-1, target)

    def helperR(self, array, lowIdx, highIdx, target):
    	if lowIdx > highIdx or not array:
    		return False
    	midIdx = (lowIdx+highIdx)/2
    	if array[midIdx] == target:
    		return True
    	length = len(array)
    	if target > array[midIdx]:
    		return self.helperR(array, midIdx+1, highIdx, target)
    	else:
    		return self.helperR(array, lowIdx, midIdx-1, target)