class Solution:
    def distanceK(self, root, target, k):
        parent = {}

        def dfs(node, par):
            if not node:
                return

            parent[node] = par

            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)

        q = deque([target])
        visited = {target}

        distance = 0

        while q:
            if distance == k:
                return [node.val for node in q]
            size = len(q)

            for _ in range(size):
                node = q.popleft()

                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)

                if parent[node] and parent[node] not in visited:
                    visited.add(parent[node])
                    q.append(parent[node])
                    
            distance += 1 
        return []
