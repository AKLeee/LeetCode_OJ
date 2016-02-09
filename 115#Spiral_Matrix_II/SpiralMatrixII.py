class Solution(object):
    def generateMatrix(self, n):
        if n == 0: return []
        result = [[None] * n for _ in xrange(n)]

        directionX, directionY = 0, 1
        x, y = 0, 0
        for num in xrange(1, n*n+1):
            result[x][y] = num
            if x+directionX >= n or y+directionY >= n or result[x+directionX][y+directionY] is not None:
                # change direction
                directionX, directionY = directionY, -directionX
            x += directionX
            y += directionY
        return result

# class Solution(object):
#     def generateMatrix(self, n):
#         result =[[None] * n for _ in xrange(n)]

#         mid, val = n/2, 1

#         for i in range(mid):
#             last = n-1-i
#             for j in range(i, last):
#                 val += 1
#                 result[i][j] = val
#             for j in range(i, last):
#                 val += 1
#                 result[j][last] = val
#             for j in range(last, i, -1):
#                 val += 1
#                 result[last][j] = val
#             for j in range(last, i, -1):
#                 val += 1
#                 result[j][i] = val
#         if n%2 == 1:
#             result[n/2][n/2] = val
#         return result