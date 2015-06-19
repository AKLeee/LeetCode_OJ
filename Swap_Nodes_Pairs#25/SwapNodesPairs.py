# Given a linked list, swap every two adjacent nodes and return its head.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head:
            return None
    	if not head.next:
    		return head
    	h1 = head    	
    	h2 = head.next
    	pre = h1
    	head = head.next

    	while h1 and h2:
    		if not h2.next:
    			h1.next = None
    			if pre != h1:
    				pre.next = h2
    			h2.next = h1
    			break
    		else:
    			h1.next = h2.next
    			h2.next = h1
    			if pre != h1:
    				pre.next = h2
    			pre = h2.next
    			h1 = h1.next
    			if h1.next:
    				h2 = h1.next
    			else:
    				break

    	return head