class Solution:
    def findDifference(self, nums1, nums2):
        ans = []
        ans.append(set(nums1) - set(nums2))
        ans.append(set(nums2) - set(nums1))
        return ans