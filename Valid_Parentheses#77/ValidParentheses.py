class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
    	if len(s) == 0 or not s:
    		return True

    	cache = []
    	for c in s:
    		if c == '(' or c == '[' or c == '{':
    			cache.append(c)
    			continue

    		if c == ')':
    			if len(cache) == 0 or cache.pop() != '(':
    				return False
    		if c == ']':
    			if len(cache) == 0 or cache.pop() != '[':
    				return False
    		if c == '}':
    			if len(cache) == 0 or cache.pop() != '{':
    				return False

    	if len(cache) != 0:
    		return False
    	return True

if __name__ == '__main__':
	print Solution().isValid(']')