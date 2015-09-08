class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
        	return s
        result = ''
        #calculate the interval
        interval = (numRows-1)*2
        for i in range(numRows):
        	j = i
        	midNum = (numRows-i-1)*2
        	while j < len(s):
        		result += s[j]
        		#check boundary of midNum
        		if midNum != 0 and midNum != interval and j+midNum < len(s):
        			result += s[j+midNum]
        		j += interval
        return result