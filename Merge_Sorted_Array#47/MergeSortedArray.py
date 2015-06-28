# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# # You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.


#Can I use insert from Python
class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
    	result = []
    	i, j = 0, 0
    	count = 0
    	if m == 0:
    		nums1 = nums2
    		return nums1
    	if n == 0:
    		return nums1
    	for idx in range(m+n):
    		if i >= m:
    			nums1.extend(nums2[j:])
    			return nums1
    		if j >= n:
    			return nums1
    		if nums2[j] >= nums1[i]:
    			i += 1
    			count += 1
    		else:
    			nums1.insert(i, nums2[j])
    			i += 1
    			j += 1

    	return nums1
