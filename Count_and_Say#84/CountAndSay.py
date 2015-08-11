class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
    	# s = str(n)
    	# num = s[0]
    	# count = 0
    	result = '1'
    	for idx in range(n-1):
    		s = result
    		num = s[0]
    		count = 0
    		result = ''
	    	for i in range(len(s)):
	    		#print num, count
	    		if i+1 == len(s):
	    			if s[i] == num:
	    				count += 1
	    				result += (str(count) + num)
	    				break
	    			else:
	    				result += (str(count) + num + '1' + s[i])
	    				break
	    		if s[i] == num:
	    			count += 1
	    		else:
	    			result += (str(count) + num)
	    			num = s[i]
	    			count = 1

    	return result

if __name__ == '__main__':
	print Solution().countAndSay(5)