class Solution:
    def firstUniqChar(self, s: str) -> int:
        f={}
        for ch in s:
            f[ch]=f.get(ch,0)+1
        for i in range(len(s)):
            if f[s[i]]==1:
                return i
        return -1
        