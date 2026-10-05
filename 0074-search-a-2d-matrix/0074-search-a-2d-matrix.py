class Solution:
    def searchMatrix(self, matrix, target):

        # Binary Search on Rows
        left = 0
        right = len(matrix) - 1

        while left <= right:

            mid_row = (left + right) // 2

            if target < matrix[mid_row][0]:
                right = mid_row - 1

            elif target > matrix[mid_row][-1]:
                left = mid_row + 1

            else:
                break

        # No row found
        if left > right:
            return False

        # Binary Search inside the row
        row = matrix[mid_row]

        left = 0
        right = len(row) - 1

        while left <= right:

            mid = (left + right) // 2

            if row[mid] == target:
                return True

            elif row[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False

