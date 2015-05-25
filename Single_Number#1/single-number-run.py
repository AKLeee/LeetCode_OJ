from SingleNumber import Solution

#make better test cases
#unsigned short 0 ~ 2^15-1 (65535)
#unsigned long 0 ~ 2^31-1 (4294967295)
data = [1, -89, 23, -89, 65300, 11111111, 457, 33, 65300, 11111111, 33, 457, 1]

test = Solution()

print test.singleNumber(data)