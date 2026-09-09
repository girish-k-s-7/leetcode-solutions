class Solution:

    def balanceBST(self, root):

        nodes = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)

        def build(left, right):

            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nodes[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        inorder(root)

        return build(0, len(nodes) - 1)