# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
    	#first try is to store all the data in a array and then convert it to BST
    	if head is None:
    		return None

    	slow = head
    	fast = head
    	#temp is only used for breaking the link
    	temp = None

    	while fast.next is not None and fast.next.next is not None:
    		fast = fast.next.next
    		temp = slow
    		slow = slow.next

    	#find the mid node
    	if temp is None:
    		head = None
    	else:
    		temp.next = None #break the link

    	root = TreeNode(slow.val)
    	root.left = self.sortedListToBST(head)
    	root.right = self.sortedListToBST(slow.next)

    	return root


