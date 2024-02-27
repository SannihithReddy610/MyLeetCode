class Solution:
    def subarraySum(self, nums, k: int) -> int:
        ans = 0
        prefix_sum = 0
        dic = {0: 1}

        for num in nums:
            prefix_sum = prefix_sum + num
            if prefix_sum - k in dic:
                ans += dic[prefix_sum - k]
            if prefix_sum not in dic:
                dic[prefix_sum] = 1
            else:
                dic[prefix_sum] += 1

        return ans
