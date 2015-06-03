# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    # @param {integer} n
    # @return {integer}

    # Can work, but takes too much time
    # def climbStairs(self, n):
    # 	if n < 1:
    # 		return None
    # 	if n == 1:
    # 		return 1
    # 	if n == 2:
    # 		return 2
    # 	return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs(self, n):
    	if n == 1:
    		return 1
    	if n == 2:
    		return 2
    	cacheStep = [None]*(n+1)
    	cacheStep[1] = 1
    	cacheStep[2] = 2
    	for num in range(3,n+1):
    		cacheStep[num] = cacheStep[num-1] + cacheStep[num-2]
    	return cacheStep[n]