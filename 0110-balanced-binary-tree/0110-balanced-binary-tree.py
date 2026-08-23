class Solution:

    def height(self, root):

        if root is None:
            return 0

        leftHeight = self.height(root.left)

        if leftHeight == -1:
            return -1

        rightHeight = self.height(root.right)

        if rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1

        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root):

        return self.height(root) != -1