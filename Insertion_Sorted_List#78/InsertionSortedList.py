# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
    	newHead = ListNode(0)
    	while head:
    		cur = head
    		pre = newHead
    		head = head.next
    		while pre.next and pre.next.val <= cur.val:
    			pre = pre.next
    		cur.next = pre.next
    		pre.next = cur

    	return newHead.next