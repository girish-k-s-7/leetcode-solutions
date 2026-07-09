class Solution():
    def spiralOrder(self, matrix):
        result = []
        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # traversing top row from left right right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            # traverse right column from top to bottom
            for i in range(top, bottom +1):
                result.append(matrix[i][right])
            right -= 1

            # check for remaining elements
            if top <= bottom:
                for i in range(right, left-1, -1):
                        result.append(matrix[bottom][i])
                bottom -= 1  # Move bottom boundary up

            # Check for remaining columns
            if left <= right:
                # Traverse left column from bottom to top
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Move left boundary right

        return result