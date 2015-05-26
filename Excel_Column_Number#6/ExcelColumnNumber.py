# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
    	result = 0
    	index = len(s)
    	asc = ord('A')-1
    	for c in s:
    		result = result + (ord(c) - asc)*26**(index - 1)
    		index -= 1
    	return result