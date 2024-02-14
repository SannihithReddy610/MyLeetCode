class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            result.append(self.helper(result, i))
        return result[:numRows]

    def helper(self, f, num):
        a = []
        prev = f[num - 1]
        k = 0
        l = 1
        a.append(1)
        for i in range(1, num):
            a.append(prev[k] + prev[l])
            k += 1
            l += 1
        a.append(1)
        return a

