class Solution:
    def findLucky(self, arr: List[int]) -> int:
        x=-1
        for i in arr:
            if arr.count(i)==i:
                x=max(x,i)
        return x
        