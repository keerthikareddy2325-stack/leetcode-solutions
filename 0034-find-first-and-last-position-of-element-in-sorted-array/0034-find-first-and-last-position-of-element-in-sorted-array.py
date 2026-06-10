class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        f=0
        last=len(nums)-1
        while f<=last and nums[f]!=target:
            f+=1
        while last>=f and nums[last]!=target:
            last-=1
        if f<=last:
            return[f,last]
        return[-1,-1]

