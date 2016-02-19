from string import ascii_lowercase

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        queue = [(beginWord, 1)]
        visited = set()

        while queue:
        	word, dist = queue.pop(0)
        	if word == endWord:
        		return dist
        	for i in range(len(endWord)):
        		for j in ascii_lowercase:
        			tmp = word[:i] + j + word[i+1:]
        			if tmp not in visited and tmp in wordList:
        				print 'in'
        				visited.add(tmp)
        				queue.append((tmp, dist+1))
        return 0

if __name__ == '__main__':
	print Solution().ladderLength('a','c',['a','b','c'])