class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        def height(node):
            if node is None:
                return 0

            leftHeight = height(node.left)
            rightHeight = height(node.right)

            self.diameter = max(self.diameter, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)
            
        height(root)
        return self.diameter