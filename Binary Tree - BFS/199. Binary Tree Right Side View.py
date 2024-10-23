# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        q = deque([root])
        outputList = []

        while q:
            outputList.append(q[-1].val)
            level = []

            for node in q:
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
            q = level

        return outputList


        