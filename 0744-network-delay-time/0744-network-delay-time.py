class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        minHeap = [(0, k)]
        visited = set()

        maxTime = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)

            maxTime = max(maxTime, time)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (time + weight, neighbor) )

        return maxTime if len(visited) == n else -1