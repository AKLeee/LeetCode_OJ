class Solution(object):
    def wordBreak(self, s, wordDict):
    	dp = [False]*(len(s)+1)
    	dp[0] = True
    	for index in range(len(s)):
    		for pointer in range(index,-1,-1):
    			count+=1
    			if dp[pointer] and s[pointer:index+1] in wordDict:
    				dp[index+1] = True
    				break
    	return dp[len(s)]

if __name__ == '__main__':
	print Solution().wordBreak('leetcode', ['leet', 'code'])