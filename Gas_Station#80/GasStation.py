class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
    	curSum, totalSum = 0, 0
    	start = 0
    	for i in range(len(cost)):
    		curSum += gas[i]-cost[i]
    		totalSum += gas[i]-cost[i]
    		if curSum < 0:
    			#if position i is not good, jump to i+1
    			curSum = 0
    			start = i+1

    	if totalSum < 0:
    		return -1
    	else:
    		return start

if __name__ == '__main__':
	print Solution().canCompleteCircuit([1,2,1],[2,1,1])