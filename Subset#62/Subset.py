# Given a set of distinct integers, nums, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.

# class Solution:
# 	# @param {integer[]} nums
# 	# @return {integer[][]}
# 	def subsets(self, nums):
# 		nums.sort()
# 		result = [[]]
# 		cache = []
# 		#result.append([])
# 		for indexOne in range(len(nums)):
# 			insideRange = len(result)
# 			#print result
# 			for indexTwo in range(insideRange):
# 				cache = result[indexTwo]
# 				#print cache
# 				cache.append(nums[indexOne])
# 				#print cache
# 				result.append(list(cache))
# 		return result

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.sort()
        result = [[]]
        for num in nums:
            # add current number into result
            result.extend([subset + [num] for subset in result])

        return result

if __name__ == "__main__":
	print Solution().subsets([1,2])