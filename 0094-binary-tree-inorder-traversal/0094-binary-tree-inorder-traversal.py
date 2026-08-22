class Solution:
    def inorderTraversal(self, root):
        st = []
        node = root
        inorder = []
        while True:
            if node is not None:
                st.append(node)
                node = node.left
            else:
                if not st:
                    break
                node = st.pop()
                inorder.append(node.val)
                node = node.right
        return inorder
        