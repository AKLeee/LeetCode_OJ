class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) is 0:
        	return result
        used = [False]*len(nums)
        nums.sort()
        per = []
        self.findpermutation(nums, used, per, result)
        return result

    def findpermutation(self, nums, used, per, result):
    	if len(per) == len(nums):
    		result.append(list(per))
    		return

    	for i in range(len(nums)):
    		if used[i]: continue
    		if i > 0 and (nums[i] == nums[i-1]) and (used[i-1] == False): continue
    		used[i] = True
    		per.append(nums[i])
    		self.findpermutation(nums, used, per, result)
    		used[i] = False
    		per.pop()

if __name__ == '__main__':
	print Solution().permuteUnique([1,1,2])