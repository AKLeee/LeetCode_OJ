# Implement strStr().

# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
	# @param {string} haystack
	# @param {string} needle
	# @return {integer}
	def strStr(self, haystack, needle):
		if len(haystack)<len(needle):
			return -1
		for i in range(len(haystack)-len(needle)+1):
			found=True
			for j in range(len(needle)):
				if haystack[i+j]!=needle[j]:
					found=False
					break
			if found:
				return i
		return -1
		