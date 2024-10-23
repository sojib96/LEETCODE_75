# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        minLevel = 0
        currLevel = 0
        q = deque([root])
        while q:
            currLevel += 1
            level = len(q)
            lvlSum = 0
            for _ in range(level):
                currNode = q.popleft()
                lvlSum += currNode.val
                if currNode.left: q.append(currNode.left)
                if currNode.right: q.append(currNode.right)
            
            if lvlSum > maxSum: 
                maxSum = lvlSum
                minLevel = currLevel
            
        return minLevel