class Solution:
    # def printLL(self, head):
    #     while head is not None:
    #         print(head.data, end=" ")
    #         head = head.next

    def removeNthFromEnd(self, head, N):
        dummy = ListNode(0, head)
        dummy.next = head
        slow = dummy
        fast = dummy

        for _ in range(N+1):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next