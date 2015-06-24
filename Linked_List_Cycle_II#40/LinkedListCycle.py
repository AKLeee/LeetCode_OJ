# Given a linked list, return the node where the cycle begins. If there is no cycle, return null

# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
    	fast = head
    	slow = head
    	start = head
    	while fast:
    		if fast.next is None:
    			return None
    		if fast.next.next is not None:
    			fast = fast.next.next
    			slow = slow.next
    		else:
    			return None
    		if slow == fast:
    			newStart = slow
    			while newStart != start:
    				start = start.next
    				newStart = newStart.next
    			return start
    	return None