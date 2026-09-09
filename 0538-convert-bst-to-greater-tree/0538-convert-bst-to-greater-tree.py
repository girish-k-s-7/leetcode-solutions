class Solution:

    def convertBST(self, root):

        self.total = 0

        def reverseInorder(node):

            if not node:
                return

            reverseInorder(node.right)

            self.total += node.val
            node.val = self.total

            reverseInorder(node.left)

        reverseInorder(root)

        return root