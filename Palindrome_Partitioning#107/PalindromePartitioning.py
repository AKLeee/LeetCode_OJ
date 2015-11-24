class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        sList = list(s)
        result = []
        part = []
        isPal = [[False for x in range(n)] for x in range(n)]
        for i in range(n-1, -1, -1):
        	for j in range(i, n):
        		if (i+1 >= j-1 or isPal[i+1][j-1]) and sList[i] == sList[j]:
        			isPal[i][j] = True
        #print isPal
        self.findPartitions(s, 0, isPal, part, result)
        return result

    def findPartitions(self, s, start, isPal, part, result):
    	#print part
    	if start == len(s):
    		result.append(list(part))
    		return

    	for i in range(start, len(s)):
    		if isPal[start][i]:
    			length = i - start + 1
    			#print start, length, i
    			part.append(s[start:start+length])
    			# if start == i:
    			# 	print list(s)[start]
    			# 	part.append(list(s)[start])
    			# else:
    			# 	print s[start:i-start+1]
    				#print s[2:5]
    			# 	part.append(s[start:i-start+1])
    			self.findPartitions(s, i+1, isPal, part, result)
    			part.pop()

if __name__ == '__main__':
	print Solution().partition('addcdd')