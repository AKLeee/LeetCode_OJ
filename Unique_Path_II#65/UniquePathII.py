# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
    	cache = {}
        m = len(obstacleGrid)-1
        n = len(obstacleGrid[:][0])-1
        #print m, n
    	return self.count(obstacleGrid, cache, m, n)

    def count(self, obstacleGrid, cache, m, n):
    	if (m,n) in cache:
    		return cache[(m,n)]
    	if m < 0 or n < 0:
    		return 0
        if m >= 0 and n >= 0:
            if obstacleGrid[m][n] == 1:
                cache[(m,n)] = 0
                return 0
        if m == 0 and n == 0:
            return 1
        cache[(m,n)] = self.count(obstacleGrid, cache, m-1, n) + self.count(obstacleGrid,cache, m, n-1)
        # print cache[(m,n)]
    	return cache[(m,n)] 

if __name__ == '__main__':
	data = [
		  [1]
		]
	print Solution().uniquePathsWithObstacles(data)