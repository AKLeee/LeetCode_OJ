# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	def reverseList(self, head):
		if not head or not head.next:
			return head
		pre = None
		cur = head
		while cur.next:
			cache = cur.next
			cur.next = pre
			pre = cur
			cur = cache
		cur.next = pre
		return cur
		

