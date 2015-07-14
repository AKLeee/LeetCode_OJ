# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

class Solution:
	# @param {string} s
	# @return {integer}
	def lengthOfLastWord(self, s):
		index = len(s)-1
		count = 0
		flag = False
		while index >= 0:
			if s[index] != ' ':
				flag = True
				count += 1
				index -= 1
			elif flag == True:
				return count
			elif index-1 >= 0:
				if s[index-1] != ' ':
					flag = True
					index -= 1
				else:
					index -= 1
			else:
				index -= 1
		return count

if __name__ == '__main__':
	print Solution().lengthOfLastWord("abc cd")