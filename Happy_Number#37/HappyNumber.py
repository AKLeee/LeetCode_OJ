# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example: 19 is a happy number

class Solution:
	# @param {integer} n
	# @return {boolean}
	def isHappy(self, n):
		if n == 1:
			return True
		strNum = str(n)
		dic = {}
		while not dic.get(strNum):
			num = 0
			dic.update({strNum:True})
			for s in strNum:
				num += int(s)**2
			length = len(str(num))
			strNum = str(num)
			if num == 10**(length-1):
				return True
		return False