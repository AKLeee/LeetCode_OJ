class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        if not head: return None
        p1h = ListNode(0)    # handle
        p1 = p1h             # append <  node on p1 node
        p2h = ListNode(0)    # handle
        p2 = p2h             # append >= node on p2 node
        while head:
            if head.val < x: # extend p1
                p1.next = head
                p1 = p1.next
            else:            # extend p2
                p2.next = head
                p2 = p2.next
            head = head.next
        p2.next = None       # set p2 end to None
        p1.next = p2h.next   # connect p1 to p2
        return p1h.next