from BTLevelOrderTraversalII import Solution
from TreeNode import TreeNode

root = TreeNode(1)
node02 = TreeNode(2)
node03 = TreeNode(3)
node04 = TreeNode(4)

root.left = node02
root.right = node03

node02.left = node04

test = Solution()

result = test.levelOrderBottom(root)

print result