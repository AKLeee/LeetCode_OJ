# Sort a linked list in O(n log n) time using constant space complexity.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.mergeSort(head)

    def mergeSort(self,head):
    	if not head or not head.next:
    		return head
    	slow = head
    	quick = head
    	#find the mid point of list
    	while quick.next and quick.next.next:
    		slow = slow.next
    		quick = quick.next.next
    	headTwo = slow.next
    	slow.next = None
    	headOne = head
    	headOne = mergeSort(headOne)
    	headTwo = mergeSort(headTwo)
    	return merge(headOne,headTwo)

    def merge(self,headOne,headTwo):
    	dummy = ListNode(0)
    	dummy.next = headOne
    	pre = dummy
    	while headOne and headTwo:
    		if headOne.val < headTwo.val:
    			headOne = headOne.next
    		else:
    			next = headTwo.next
    			headTwo.next = pre.next
    			pre.next = headTwo
    			headTwo = next
    		pre = pre.next
    	if headTwo:
    		pre.next = headTwo
    	return dummy.next


