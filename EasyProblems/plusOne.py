class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in digits:
            num = (num*10) + i
        num = num+1
        ans = []
        while num != 0:
            ans.insert(0,num%10)
            num = num//10
        return ans