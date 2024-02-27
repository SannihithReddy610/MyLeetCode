class Solution:
    def countAndSay(self, n: int) -> str:
        ans = ['1', '11']
        if n <= 2:
            return ans[n - 1]
        for i in range(3, n+1):
            ans.append(self.helper(i, ans))
        return ans[n-1]

    def helper(self, n, ans):
        prev = ans[n-2]
        count = 1
        res = ''
        for i in range(len(prev)-1):
            if prev[i] == prev[i+1]:
                count += 1
            else:
                res += str(count) + prev[i]
                count = 1
        res += str(count) + prev[len(prev)-1]
        return res