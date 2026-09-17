class Solution:
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        visited = [[False] * cols for _ in range(rows)]
        distance = [[0] * cols for _ in range(rows)]

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c, 0))
                    visited[r][c] = True
        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        while q: 
            row, col, dist = q.popleft()
            distance[row][col] = dist
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if (0 <= nr < rows and 0 <=nc < cols and not visited[nr][nc]):
                    visited[nr][nc] = True

                    q.append((nr, nc, dist + 1))
        return distance