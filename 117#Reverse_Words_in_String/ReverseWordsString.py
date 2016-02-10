class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        j = len(s)
        for i in range(len(s)-1, -1, -1):
        	if s[i] == ' ':
        		j = i
        	elif i == 0 or s[i-1] == ' ':
        		if len(result) != 0:
        			result += ' '
        		result += s[i:j]
        return result

if __name__ == '__main__':
	print(Solution().reverseWords('abc  one two three'))