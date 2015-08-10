class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        ret, l = '', len(strs)
        for t in zip(*strs):
            if t == tuple(t[0] * l):
                ret += t[0]
            else:
                break
        return ret