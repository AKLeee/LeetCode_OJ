# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        # create dummy node
        dummy = ListNode(0)
        prev, current = dummy, head
        while current is not None:
            next = current.next
            # check if reaching end of list or current has unique value
            if (next is None) or (current.val != next.val):
                # attach current to prev and set prev to current
                prev.next = current
                prev = current
            else:
                # iterate through list till different value appears
                while (next is not None) and (next.val == current.val):
                    next = next.next
                # attach next to prev, but keep prev untouched
                prev.next = next
            current = next

        return dummy.next

if __name__ == '__main__':
	n1 = ListNode(1)
	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(3)
	n1.next = n2
	n2.next = n3
	n3.next = n4
	result = Solution().deleteDuplicates(n1)
	while result:
		print result.val
		result = result.next



