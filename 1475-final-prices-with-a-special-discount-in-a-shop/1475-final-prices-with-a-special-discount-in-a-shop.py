class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s=[]
        prices.reverse()
        for i in range(len(prices)):
            x=prices[i]
            while s and x<s[-1]:
                s.pop()
            if s:
                prices[i]-=s[-1]
            s.append(x)
        prices.reverse()
        return prices

        