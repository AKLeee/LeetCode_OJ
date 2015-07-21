# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
    	result = []
    	if candidates is None or len(candidates) == 0:
    		return result
    	candidates.sort()
    	cache = []
    	self.findSum(candidates, 0, target, cache, result)
    	return result

    def findSum(self, candidates, start, target, cache, result):
    	if target < 0:
    		return

    	if target == 0:
    		result.append(list(cache))
    		return

    	for index in range(start, len(candidates)):
    		if index > start and candidates[index] == candidates[index-1]:
    			continue
    		cache.append(candidates[index])
    		self.findSum(candidates, index, target - candidates[index], cache, result)
    		cache.pop()


if __name__ == '__main__':
	print Solution().combinationSum([2,3,6,7],7)




