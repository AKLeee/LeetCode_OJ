# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ipComb = []
        ipNum = []

        self.findIPAddresses(s, 0, ipNum, ipComb)
        return ipComb

    def findIPAddresses(self, s, index, ipNum, ipComb):
    	if len(ipNum) == 4:
    		if index == len(s):
    			ipAddr = ipNum[0]
    			for i in range(1,4):
    				ipAddr += ('.'+ipNum[i])
    			ipComb.append(ipAddr)
    		return

    	currentNum = ''
    	i = index
    	while i<len(s) and i<index+3:
    		currentNum += s[i]
    		if self.isValid(currentNum):
    			ipNum.append(currentNum)
    			self.findIPAddresses(s, i+1, ipNum, ipComb)
    			ipNum.pop()
    		i += 1

    def isValid(self, s):
    	if len(s) == 0 or len(s) > 3:
    		return False
    	if s[0] == '0' and len(s) > 1:
    		return False
    	if len(s) == 3 and int(s) > 255:
    		return False
    	return True

if __name__ == '__main__':
	print Solution().restoreIpAddresses('25525511135')
