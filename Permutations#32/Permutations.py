# Given a collection of numbers, return all possible permutations.

class Solution:
	# @param {integer[]} nums
	# @return {integer[][]}
	def permute(self, nums):
		result = []
		used = [False]*len(nums)
		per = []
		self.findPermutation(nums, used, per, result)
		return result

	def findPermutation(self, nums, used, per, result):
		if len(per) == len(nums):
			result.append(list(per))
			return

		for i in range(len(nums)):
			#print nums
			#print i
			if used[i]:
				continue
			#print used[i]
			used[i] = True
			per.append(nums[i])
			self.findPermutation(nums, used, per, result)
			used[i] = False
			per.pop()

if __name__ == '__main__':
	nums = [1,2,3]
	result = Solution().permute(nums)
	print result
