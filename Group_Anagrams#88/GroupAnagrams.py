class Solution(object):
	def groupAnagrams(self, strs):
		dic = {}
		result = []

		for item in strs:
			sortStr = ''.join(sorted(item))
			if sortStr in dic:
				dic[sortStr].append(item)
			else:
				dic.update({sortStr:[item]})

		for key, value in dic.iteritems():
			if len(value) > 0:
				value.sort()
				result.append(list(value))
		return result

if __name__ == '__main__':
	print Solution().groupAnagrams(["cba","abc","efg"])
