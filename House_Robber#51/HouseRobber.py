# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    # We don't care about exact combination of position
    # the dp[i] it self already store the combination that match the rules
    # for this kind of problem, we should find the base case and
    # all the possiblilities, then generate the formula
    def rob(self, nums):
    	if not nums:
            return 0
        n = len(nums)
        if n < 2:
            return nums[0]

        dp = {}
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[n-1]
