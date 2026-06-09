class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n=0
        p=0
        c=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c+=1
            else:
                n+=min(p,c)
                p=c
                c=1
        return n+min(p,c)
        