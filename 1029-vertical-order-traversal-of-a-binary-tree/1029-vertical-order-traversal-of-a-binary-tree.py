from collections import deque

class Solution:

    def verticalTraversal(self, root):

        if not root:
            return []

        nodes = {}

        todo = deque()
        todo.append((root, 0, 0))

        while todo:

            temp, x, y = todo.popleft()

            if x not in nodes:
                nodes[x] = {}

            if y not in nodes[x]:
                nodes[x][y] = []

            nodes[x][y].append(temp.val)

            if temp.left:
                todo.append((temp.left, x - 1, y + 1))

            if temp.right:
                todo.append((temp.right, x + 1, y + 1))

        ans = []

        for x in sorted(nodes.keys()):
            col = []

            for y in sorted(nodes[x].keys()):
                col.extend(sorted(nodes[x][y]))

            ans.append(col)

        return ans


