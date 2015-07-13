class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
    	if x < 0:
    		return False

    	if x < 10:
    		return True

    	div = 1
    	# get tatal number of digits
    	while x/div >= 10:
    		div *= 10

    	while x:
    		left = x/div
    		right = x%10
    		if left != right:
    			return False
    		# remove first and last digit
    		x = (x%div)/10
    		div = div/100

    	return True