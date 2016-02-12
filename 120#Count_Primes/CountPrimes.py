class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = [False] * n
        count = 0
        # using xrange when dealing with large range
        for i in xrange(2, n):
        	if b[i]:
        		continue
        	count += 1
        	for j in xrange(i, n, i):
        		b[j] = True

        return count

if __name__ == '__main__':
	print(Solution().countPrimes(20))