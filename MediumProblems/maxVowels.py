class Solution:
    def maxVowels(self, s: str, k: int):
        ans = 0
        count = 0
        vowels = 'aeiou'
        for i, v in enumerate(s):
            if i>=k:
                if s[i-k] in vowels:
                    count -= 1
            if v in vowels:
                count += 1
            ans = max(ans, count)
        return ans

