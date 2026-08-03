class Solution:
    def reverseBetween(self, head, left, right):

        # If there is only one node or no reversal is needed
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Move prev to the node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        current = prev.next

        # Reverse the sublist
        for _ in range(right - left):
            nextNode = current.next
            current.next = nextNode.next
            nextNode.next = prev.next
            prev.next = nextNode

        return dummy.next