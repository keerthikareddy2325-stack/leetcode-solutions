class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c=[0]*26
        l=0
        m=0
        a=0
        for r in range(len(s)):
            i=ord(s[r])-ord('A')
            c[i]+=1
            m=max(m,c[i])
            while(r-l+1)-m>k:
                c[ord(s[l])-ord('A')]-=1
                l+=1
            a=max(a,r-l+1)
        return a

        
        