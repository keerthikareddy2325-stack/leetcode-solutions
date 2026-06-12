class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=prices[0]
        p=0
        for i in prices:
            m=min(m,i)
            pp=i-m
            p=max(p,pp)
        return p