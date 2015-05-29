from LinkedListCircle import Solution
from LinkedList import ListNode

node01 = ListNode(1)
node02 = ListNode(2)
node03 = ListNode(3)
node04 = ListNode(4)
node05 = ListNode(5)

node01.next = node02
node02.next = node03
node03.next = node04
node04.next = node05
node05.next = node04

test = Solution()

print test.hasCycle(node01)