class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1: return s
        start, maxLen, n = 0, 1, len(s)
        isPal = [[False]*len(s) for x in range(len(s))]

        for i in range(n-1,-1,-1):
        	for j in range(i, n):
        		if (i+1 > j-1 or isPal[i+1][j-1]) and s[i] == s[j]:
        			isPal[i][j] = True
        			if j-i+1 > maxLen:
        				maxLen = j-i+1
        				start = i
        return s[start: start + maxLen]

if __name__ == '__main__':
	print(Solution().longestPalindrome('abcba'))