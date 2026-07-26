class Solution:
    def findPeakGrid(self, mat):

        rows = len(mat)
        cols = len(mat[0])

        low = 0
        high = cols - 1

        while low <= high:

            mid = low + (high - low) // 2

            # Find the row having the maximum element in the middle column
            maxRow = 0
            for i in range(rows):
                if mat[i][mid] > mat[maxRow][mid]:
                    maxRow = i

            left = -1
            if mid > 0:
                left = mat[maxRow][mid - 1]

            right = -1
            if mid < cols - 1:
                right = mat[maxRow][mid + 1]

            # Peak element found
            if mat[maxRow][mid] > left and mat[maxRow][mid] > right:
                return [maxRow, mid]

            # Move to the left half
            elif left > mat[maxRow][mid]:
                high = mid - 1

            # Move to the right half
            else:
                low = mid + 1