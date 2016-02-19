class Solution(object):
	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if len(s) == 0 or s[0]<'1' or s[0]>'9': return 0
		dp = [0] * (len(s)+1)
		dp[0] = dp[1] = 1

		for i in range(1, len(s)):
			if not s[i].isdigit(): return 0
			v = (int(s[i-1]) - 0)*10 + (int(s[i]) - 0)
			if v <= 26 and v > 9:
				dp[i+1] += dp[i-1]
			if s[i] != '0':
				dp[i+1] += dp[i]
			if dp[i+1] == 0: return 0

		return dp[len(s)]