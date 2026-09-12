class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        heap = []

        for r in range(n):
            heapq.heappush(heap, (matrix[r][0], r, 0))
        for _ in range(k):
            val, r, c = heapq.heappop(heap)

            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
                
        return val