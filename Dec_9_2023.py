# 94. Binary Tree Inorder Traversal
# Easy
# 12.8K
# 702
# Companies
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?







# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []

        def dfs(node):
            # each time you can visit an existing node
            if node:
                # recursevily visit it left
                dfs(node.left)
                # store value of a node
                nums.append(node.val)
                # and right child
                dfs(node.right)
        
        # start dfs
        dfs(root)

        return nums