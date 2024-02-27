class Solution:
    def removeAnagrams(self, words):
        x = [words[0]]
        for i in range(1, len(words)):
            if sorted(x[-1]) != sorted(words[i]):
                x.append(words[i])
        return x

