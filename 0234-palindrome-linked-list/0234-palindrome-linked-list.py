class Solution:
    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

    def isPalindrome(self, head):

        
        if head is None or head.next is None:
            return True

       
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        secondHalf = self.reverse(slow.next)

        # Step 3: Compare both halves
        first = head
        second = secondHalf
        isPal = True

        while second:
            if first.val != second.val:
                isPal = False
                break

            first = first.next
            second = second.next

        # Step 4: Restore the original list
        slow.next = self.reverse(secondHalf)

        return isPal