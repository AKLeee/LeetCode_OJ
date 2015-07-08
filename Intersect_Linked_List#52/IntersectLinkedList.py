# Write a program to find the node at which the intersection of two singly linked lists begins.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
    	lenA = self.getLen(headA)
    	lenB = self.getLen(headB)

    	dif = lenA - lenB
    	startA = headA
    	startB = headB
    	if dif >= 0:
    		for x in range(abs(dif)):
    			startA = startA.next
    	else:
    		for x in range(abs(dif)):
    			startB = startB.next

    	while startA and startB:
    		if startA == startB:
    			return startA
    		startA = startA.next
    		startB = startB.next

    	return None

    def getLen(self, head):
    	length = 0
    	while head:
    		length += 1
    		head = head.next
    	return length

#If two linked lists have intersection, we can find two observations:

# They must have same tail from the intersection point.
# L1+L2 must have same tail from the intersection point as L2 + L1. For example,


# To implement L1+L2 as well as L2+L1, we can simply jump to another list's head after traveling through certain list!

# But, you need to notice that if the two lists have no intersection at all, you should stop after checking L1+L2, so we need a flag to ensure it!

# def getIntersectionNode(self, headA, headB):
#     if not headA or not headB:
#         return None
#     ptA, ptB, jumpA = headA, headB, False
#     while True:
#         if id(ptA) == id(ptB):
#             return ptA
#         ptA, ptB = ptA.next, ptB.next
#         if not ptA:
#             if not jumpA:
#                 jumpA = True
#                 ptA = headB
#             else:
#                 return None
#         if not ptB:
#             ptB = headA
