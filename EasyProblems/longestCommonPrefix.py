class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        ans = ""
        sortedStrs = sorted(strs)
        firstStr = sortedStrs[0]
        lastStr = sortedStrs[-1]
        for i in range(min(len(firstStr), len(lastStr))):
            if(firstStr[i] != lastStr[i]):
                return ans
            else:
                ans += lastStr[i]
        return ans