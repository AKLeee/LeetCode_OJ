# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

class Solution(object):
    def minimumTotal(self, triangle):
    	# buttom up methode
    	if not triangle:
    		return 0
    	lastLevel = triangle[-1]
    	for i in xrange(len(triangle)-2,-1,-1):
    		for j in range(len(triangle[i])):
    			#we update the last level of triangle to sored the updated min path of all combination 
    			lastLevel[j] = min(lastLevel[j],lastLevel[j+1])+triangle[i][j]
    	return lastLevel[0]