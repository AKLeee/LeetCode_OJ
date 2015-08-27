class Solution(object):
    def nextPermutation(self, nums):
    	if len(nums)<2:
    		return
    	tail = len(nums)
    	pointer = tail - 2
    	while pointer >= 0 and nums[pointer]>=nums[pointer+1]:
    		pointer -= 1

    	if pointer < 0:
    		nums = sorted(nums)
    		return nums

    	#find next bigger than pointer
    	nextBigger = pointer + 1
    	while nextBigger < tail and nums[nextBigger] > nums[pointer]:
    		nextBigger += 1
    	nextBigger = nextBigger - 1

    	#swap nextBigger and pointer
    	nums[nextBigger], nums[pointer] = nums[pointer], nums[nextBigger]

    	nums[pointer+1:tail] = sorted(nums[pointer+1:tail])
    	#nums[2:4].sort()

    	return nums

if __name__ == '__main__':
	print Solution().nextPermutation([3,2,1])

