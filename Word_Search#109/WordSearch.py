class Solution(object):
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		if not board or not board[0]: return False
		visted = [[False for x in range(len(board))] for x in range(len(board[0]))]
		for i in range(len(board)):
			for j in range(len(board[0])):
				if self.findWord(board, word, visted, i, j, 0):
					return True
		return False

	def findWord(self, board, word, visted, row, col, index):
		if index === len(word): return True
		if row<0 or col<0 or row>len(board) or col>len(board[0]) or visted[row][col] or board[row][col] != word[index]:
			return False
		board[row][col] = True
		if self.findWord(board, word, visted, i+1, j, index+1): return True
		if self.findWord(board, word, visted, i-1, j, index+1): return True
		if self.findWord(board, word, visted, i, j+1, index+1): return True
		if self.findWord(board, word, visted, i, j-1, index+1): return True
		board[row][col] = False
		return False