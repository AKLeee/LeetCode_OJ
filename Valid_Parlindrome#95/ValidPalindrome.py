# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution(object):
    def isPalindrome(self, s):
    	if len(s) < 2 :
    		return True
    	left = 0
    	right = len(s)-1
    	while left < right:
    		#jump all non alopha char, care for boundary
    		while left < len(s) and not s[left].isalnum():
    			left += 1
    		while right >= 0 and not s[right].isalnum():
    			right -= 1
    		if left >= right:
    			return True
    		if s[left].lower() != s[right].lower():
    			return False
    		left += 1
    		right -= 1
    	return True

if __name__ == '__main__':
	print Solution().isPalindrome("1a2")