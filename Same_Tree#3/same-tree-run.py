from SameTree import Solution
from TreeNode import TreeNode

rootP = TreeNode(1)
node02 = TreeNode(2)
node03 = TreeNode(3)
node04 = TreeNode(4)

rootP.left = node02
rootP.right = node03

node02.left = node04

rootQ = TreeNode(1)
nodeQ02 = TreeNode(2)
nodeQ03 = TreeNode(3)
nodeQ04 = TreeNode(4)

rootQ.left = nodeQ02
rootQ.right = nodeQ03

nodeQ02.left = nodeQ04

test = Solution()

print test.isSameTree(rootP, rootQ)