class Solution(object):
	def reverse(self, x):
		y=abs(x)    
		string=str(y)
		#reverse a string
		result=int(string[::-1])
		if result < 2147483648:
			if x<0:
				return -1*result
			else:
				return result
		else:
			return 0