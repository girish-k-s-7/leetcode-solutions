class Solution:

    def findOrder(self, numCourses, prerequisites):

        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        q = deque()

        # Add all nodes with indegree 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:

            node = q.popleft()
            topo.append(node)

            for neighbor in adj[node]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(topo) == numCourses:
            return topo

        return []