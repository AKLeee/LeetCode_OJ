class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		dic = {}
		maxLen, curLen, start = 0, 0, 0
		for i in range(len(s)):
			#seen = dic.get(s[i])
			if s[i] in dic:
				for j in range(start, dic[s[i]]):
					del dic[s[j]]
				start = dic[s[i]] + 1
				curLen = i - dic[s[i]]
			else:
				curLen += 1

			dic[s[i]] = i
			maxLen = max(maxLen, curLen)

		return maxLen

if __name__ == '__main__':
	print (Solution().lengthOfLongestSubstring('aaa'))