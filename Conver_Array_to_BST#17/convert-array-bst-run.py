from ConvertArrayBST import Solution
from TreeNode import TreeNode

data = [2,4,8,11,23,77]

test = Solution()

root = test.sortedArrayToBST(data)

print root.left.right.val
print root.right.left.val


