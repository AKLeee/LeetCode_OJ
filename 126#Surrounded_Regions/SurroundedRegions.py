from Queue import Queue

class Solution(object):
    def mark_untakable_point(self, board, i, j, bool):
        bfs = Queue()
        bfs.put((i, j))
        while bfs.qsize() > 0:
            i, j = bfs.get()
            if bool[i][j] == 'O':
                bool[i][j] = '#'
                if i + 1 < len(board) and bool[i + 1][j] == 'O':
                    bfs.put((i + 1, j))
                if i > 0 and bool[i - 1][j] == 'O':
                    bfs.put((i - 1, j))
                if j + 1 < len(board[0]) and bool[i][j + 1] == 'O':
                    bfs.put((i, j + 1))
                if j > 0 and bool[i][j - 1] == 'O':
                    bfs.put((i, j - 1))

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        bool = board
        for i in xrange(len(board[0])):
            if bool[0][i] == 'O':
                self.mark_untakable_point(board, 0, i, bool)
        for i in xrange(len(board[-1])):
            if bool[-1][i] == 'O':
                self.mark_untakable_point(board, len(board) - 1, i, bool)
        for i in xrange(len(board)):
            if bool[i][0] == 'O':
                self.mark_untakable_point(board, i, 0, bool)
        for i in xrange(len(board)):
            if bool[i][-1] == 'O':
                self.mark_untakable_point(board, i, len(board[0]) - 1, bool)

        for i in xrange(len(bool)):
            for j in xrange(len(bool[i])):
                if bool[i][j] == 'O':
                    board[i][j] = 'X'
                elif bool[i][j] == '#':
                    board[i][j] = 'O'