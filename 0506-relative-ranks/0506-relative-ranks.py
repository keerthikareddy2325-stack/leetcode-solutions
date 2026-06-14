class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s=sorted(score,reverse=True)
        r={}
        for i,n in enumerate(s):
            if i==0:
                r[n]="Gold Medal"
            elif i==1:
                r[n]="Silver Medal"
            elif i==2:
                r[n]="Bronze Medal"
            else:
                r[n]=str(i+1)
        return [r[n] for n in score]