# 5 multiply an even number will contribute one tailing zero. The factorial list never short of even number. Basically, how many '5' within the list determines the number of tailing zero. The code bellow count how many 5 in the list from 1 to n.


class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        res=0
        while n>0:
            n=int(n/5) 
            res+=n 
        return res