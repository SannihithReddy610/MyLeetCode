class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ans = []
        for i in range(len(set(target))):
            t_count = target.count(target[i])
            s_count = s.count(target[i])
            if s_count >= t_count:
                ans.append(s_count//t_count)
            else:
                return 0
        return min(ans)