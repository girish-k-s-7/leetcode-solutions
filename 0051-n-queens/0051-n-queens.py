class Solution:
    def solve(self, col, board, n, leftrow, upperdiagonal, lowerdiagonal, ans):
        if col == n:
            ans.append(["".join(row) for row in board])
            return

        for row in range(n):
            if leftrow[row] == 0 and lowerdiagonal[row + col] == 0 and upperdiagonal[n-1 + col - row] == 0:
                board[row][col] = "Q"
                leftrow[row] = lowerdiagonal[row + col] = upperdiagonal[n - 1 + col - row] = 1
                self.solve(col + 1, board, n, leftrow, upperdiagonal, lowerdiagonal, ans)
                board[row][col]='.'
                leftrow[row] = lowerdiagonal[row + col] = upperdiagonal[n - 1 + col - row] = 0

    def solveNQueens(self, n):
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        leftrow = [0] * n
        lowerdiagonal = [0] * (2 * n -1)
        upperdiagonal = [0] * (2 * n -1)
        self.solve(0, board, n, leftrow, upperdiagonal, lowerdiagonal, ans)
        return ans