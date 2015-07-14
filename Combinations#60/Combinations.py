# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    result = []
    def combine(self, n, k):
    	if k > n or n == 0:
    		return self.result
    	cache = []
    	self.helper(cache, n, k, 1)
    	#print self.result
    	return self.result

    def helper(self, cache, n, k, start):
    	for num in range(start,n+1):
    		cache.append(num)
    		if len(cache) == k:
    			self.result.append(cache[:])
    			cache.pop()
    			continue
    		if num < n:
    			self.helper(cache, n, k, num+1)
    		cache.pop()

    #def main(self):
    	#print self.combine(4,2) 

if __name__ == "__main__":
    result = Solution().combine(2,1)
    print result
    #for r in result:
    	#print r