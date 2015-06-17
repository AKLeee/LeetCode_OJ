# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
    	result = []
    	self.addParentString(result, '', n, 0)
    	return result

    def addParentString(self, array, string, balance, credit):
    	if balance == 0 and credit == 0:
    		array.append(string)
    	if balance > 0:
    		self.addParentString(array, string + '(', balance-1, credit+1)
    	if credit > 0:
    		self.addParentString(array, string + ')', balance, credit-1)