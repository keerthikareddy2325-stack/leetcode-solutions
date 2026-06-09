class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=""
        strs=sorted(strs)
        f=strs[0]
        last=strs[-1]
        for i in range(min(len(f),len(last))):
            if(f[i]!=last[i]):
                return l
            l+=f[i]
        return l
        