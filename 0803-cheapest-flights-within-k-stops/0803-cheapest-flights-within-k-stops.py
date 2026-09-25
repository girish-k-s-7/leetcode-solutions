

class Solution:

    def findCheapestPrice(
        self,
        n,
        flights,
        src,
        dst,
        k
    ):

        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))

        dist = [float("inf")] * n
        dist[src] = 0

        q = deque()
        q.append((0, src, 0))

        while q:

            stops, node, cost = q.popleft()

            if stops > k:
                continue

            for neighbor, price in graph[node]:

                newCost = cost + price

                if newCost < dist[neighbor]:

                    dist[neighbor] = newCost

                    q.append(
                        (
                            stops + 1,
                            neighbor,
                            newCost
                        )
                    )

        return dist[dst] if dist[dst] != float("inf") else -1