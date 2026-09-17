class Solution:
    def dfs(self, node, adj, visited, pathVisited):
        visited[node] = True
        pathVisited[node] = True

        for neighbor in adj[node]:
            if not visited[neighbor]:
                if self.dfs(neighbor, adj, visited, pathVisited):
                    return True
            elif pathVisited[neighbor]:

                return True
        pathVisited[node] = False
        return False


    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj[prereq].append(course)

        visited = [False] * numCourses
        pathVisited = [False] * numCourses

        for i in range(numCourses):
            if not visited[i]:
                if self.dfs(i, adj, visited, pathVisited):
                    return False
        return True