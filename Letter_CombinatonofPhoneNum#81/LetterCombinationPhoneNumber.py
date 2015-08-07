class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        result = []
        if len(digits) == 0:
        	return result
        dic = {"2":"abc", "3":"def", "4":"ghi", 
        "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        comb = '0'*len(digits)
        self.findComb(digits,dic,0,comb,result)

        return result

    def findComb(self, digits, dic, index, comb, result):
    	if index == len(digits):
    		result.append(comb)
    		return

    	letters = dic.get(digits[index])
    	for i in range(len(letters)):
    		strList = list(comb)
    		strList[index] = letters[i]
    		comb = ''.join(strList)
    		self.findComb(digits,dic,index+1,comb,result)

if __name__ == '__main__':
	print Solution().letterCombinations('23')

