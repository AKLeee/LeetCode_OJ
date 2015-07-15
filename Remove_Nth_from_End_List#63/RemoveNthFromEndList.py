# Given a linked list, remove the nth node from the end of list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
    	#first we can count how many nodes in the list
    	#then make an other traversal, but it take more time
    	#if we want to implement it in one pass, we should use extra space
    	count = self.getNumberOfNodes(head)
    	if n <= count:
    		node = head
    		while node:
    			if count == n+1:
    				node.next = node.next.next
    				return head
    			if count == n:
    				head = node.next
    				node.next = None
    				return head
    			count -= 1
    			node = node.next
    	return head
    		


    def getNumberOfNodes(self, head):
    	count = 0
    	while head:
    		count += 1
    		head = head.next
    	return count

