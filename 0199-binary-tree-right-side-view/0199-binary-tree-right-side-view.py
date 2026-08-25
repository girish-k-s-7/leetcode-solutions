class Solution:
    def rightdfs(self, node, level, res):
        if not node:
            return
        if len(res) == level:
            res.append(node.val)
        self.rightdfs(node.right, level + 1, res)
        self.rightdfs(node.left, level + 1, res)

    def rightSideView(self, root):
        res = []
        self.rightdfs(root, 0, res)
        return res