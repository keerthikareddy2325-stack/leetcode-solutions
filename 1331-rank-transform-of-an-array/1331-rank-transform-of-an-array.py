class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = sorted(set(arr))
        d = {}
        for i in range(len(s)):
            d[s[i]] = i + 1
        return [d[x] for x in arr]