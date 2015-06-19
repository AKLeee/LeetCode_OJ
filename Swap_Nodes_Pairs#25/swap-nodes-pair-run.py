from SwapNodesPairs import Solution
from LinkedList import ListNode

head = ListNode(1)
h1 = ListNode(2)
h2 = ListNode(3)
h3 = ListNode(4)
h4 = ListNode(5)
h5 = ListNode(6)

head.next = h1
h1.next = h2
h2.next = h3
h3.next = h4
h4.next = h5

test = Solution()

result = test.swapPairs(head)

while result:
	print result.val
	result = result.next