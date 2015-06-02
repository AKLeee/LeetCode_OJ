# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
    	result = head
    	if not head:
    		return head
    	while head.next and head:
    		currentVal = head.val
    		nextVal = head.next.val

    		if currentVal == nextVal:
    			if(head.next.next == None):
    				head.next = None
    			else:
    				cacheNode = head.next.next
    				head.next = cacheNode
    				#the duplicate may bigger than 2
    				continue
    		head = head.next
    		if not head:
    			break
    	return result