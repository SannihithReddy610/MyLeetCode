class Solution:
    def intersection(self, nums):
        ans = set(nums[0])
        for num in nums[1:]:
            ans &= set(num)

        ans = list(ans)
        return sorted(ans)

