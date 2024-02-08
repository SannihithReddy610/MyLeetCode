class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        x = haystack.replace(needle, '$' * len(needle))
        return x.index('$')
