class Solution:

    def cloneGraph(self, node):

        if node is None:
            return None

        visited = {}

        def dfs(node):

            # If already cloned, return the clone
            if node in visited:
                return visited[node]

            # Create a clone
            clone = Node(node.val)

            # Store mapping
            visited[node] = clone

            # Clone all neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)