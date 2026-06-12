class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        c=0
        for i in range(len(grumpy)):
            if grumpy[i]==0:
                c+=customers[i]
        extra=0
        for i in range(len(grumpy)-minutes+1):
            s=0
            for j in range(i,i+minutes):
                if grumpy[j]==1:
                    s=s+customers[j]
            extra=max(extra,s)
        return c+extra