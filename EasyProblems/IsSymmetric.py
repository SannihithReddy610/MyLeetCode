# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):
        def isMirror(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            return isMirror(l.left, r.right) and isMirror(l.right, r.left)

        return isMirror(root, root)
