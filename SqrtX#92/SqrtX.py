class Solution(object):
    def mySqrt(self, x):
    	if x<0: return -1
    	if x == 0: return 0
    	left = 1
    	right = x/2+1
    	while left <= right:
    		mid = (left+right)/2
    		if x >= mid*mid and x < (mid+1)*(mid+1):
    			return mid

    		if x > mid*mid:
    			left = m + 1
    		else:
    			right = m - 1

    	return 0

if __name__ == '__main__':
	print Solution().mySqrt()