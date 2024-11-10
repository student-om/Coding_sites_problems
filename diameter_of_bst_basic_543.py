# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #diameter is sum of the left and the right subtrees
    #height of subtree with root2 + height of subtree with node 3
    #2+1=3(in the given example).
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0

        def height(root):
            nonlocal diameter
            if not root:
                return 0
            left_height=height(root.left)
            right_height=height(root.right)
            diameter=max(diameter,left_height+right_height)
            return max(left_height,right_height)+1
        height(root)
        return diameter
