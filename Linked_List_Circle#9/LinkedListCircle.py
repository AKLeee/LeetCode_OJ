# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
    	quickHead = None
    	slowHead = None
    	if not head:
    		return False
    	if head.next is not None:
    		quickHead = head.next
    		slowHead = head.next
    	else:
    		return False

    	while quickHead and quickHead.next:
    		quickHead = quickHead.next.next
    		slowHead = slowHead.next
    		if quickHead == slowHead:
    			return True
    	return False