class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in dic:
                stack.append(i)
            elif len(stack) == 0 or dic[stack.pop()] != i:
                return False
        return stack == []