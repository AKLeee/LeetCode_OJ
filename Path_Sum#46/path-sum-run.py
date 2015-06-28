from PathSum import Solution
from TreeNode import TreeNode

root = TreeNode(1)
node02 = TreeNode(2)
node03 = TreeNode(3)
node04 = TreeNode(4)
node05 = TreeNode(5)

root.left = node02
# root.right = node03

# node02.left = node04
#node02.right = node05

test = Solution()

print test.hasPathSum(root,1)