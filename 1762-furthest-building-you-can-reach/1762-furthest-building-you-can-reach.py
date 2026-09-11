class Solution:
    def furthestBuilding(self, heights, bricks, ladders):

        minHeap = []

        for i in range(len(heights) - 1):

            climb = heights[i + 1] - heights[i]

            if climb > 0:
                heapq.heappush(minHeap, climb)

            if len(minHeap) > ladders:
                bricks -= heapq.heappop(minHeap)

            if bricks < 0:
                return i

        return len(heights) - 1