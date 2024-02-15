import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        regex = re.compile('[^a-z0-9]')
        s = regex.sub('', s)
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                return False
        return True


