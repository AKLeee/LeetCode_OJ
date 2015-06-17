from MergeSortedList import Solution
from LinkedList import ListNode

head01 = ListNode(1)
head02 = ListNode(2)

p01 = ListNode(3)
p02 = ListNode(5)
p03 = ListNode(7)

q01 = ListNode(6)
q02 = ListNode(8)
q03 = ListNode(9)

head01.next = p01
p01.next = p02
p02.next = p03

head02.next = q01
q01.next = q02
q02.next =q03

test = Solution()

testHead = test.mergeTwoLists(head01, head02)

while testHead:
	print testHead.val
	testHead = testHead.next
