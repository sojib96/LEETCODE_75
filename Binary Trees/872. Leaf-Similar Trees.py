# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root) -> List:
            leafList = []
            stack = [root]
            while stack:
                element = stack.pop()
                if element.right: stack.append(element.right)
                if element.left: stack.append(element.left)
                if not element.right and not element.left:
                    leafList.append(element.val)
            return leafList

        if dfs(root1)!= dfs(root2):
            return False
        else:
            return True
