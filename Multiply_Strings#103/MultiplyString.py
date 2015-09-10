# Given two numbers represented as strings, return multiplication of the numbers as a string.

# Note: The numbers can be arbitrarily large and are non-negative.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) == 0 or len(num2) == 0:
        	return ""
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0]*(len(num1)+len(num2))

        for i in range(len(num2)):
        	carry = 0
        	val = int(num2[i])
        	for j in range(len(num1)):
        		carry += int(num1[j])*val + int(result[i+j])
        		result[i+j] = carry%10
        		carry /= 10
        	if carry != 0:
        		result[len(num1)+i] = carry
        result = result[::-1]

        count = 0
        while count < len(result)-1 and result[count] == 0:
        	count += 1
        result = result[count:]
        return ''.join(map(str,result))

if __name__ == '__main__':
	print Solution().multiply('98','9')