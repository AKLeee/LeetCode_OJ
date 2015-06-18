# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
	# @param {string} s
	# @return {integer}
	def romanToInt(self, s):
		if s == None:
			return 0
		if len(s) == 1:
			return self.getNum(s)
		if self.getNum(s[0]) >= self.getNum(s[1]):
			pre = s[0]
			for idx,c in enumerate(s):
				if c != pre:
					return self.getNum(pre)*(idx) + self.romanToInt(s[idx:])
			return self.getNum(pre)*len(s)
		else:
			if len(s)>2:
				return self.getNum(s[1]) - self.getNum(s[0]) + self.romanToInt(s[2:])
			else:
				return self.getNum(s[1]) - self.getNum(s[0])

	def getNum(self, s):
		if s == 'I':
			return 1
		if s == 'V':
			return 5
		if s == 'X':
			return 10
		if s == 'L':
			return 50
		if s == 'C':
			return 100
		if s == 'D':
			return 500
		if s == 'M':
			return 1000