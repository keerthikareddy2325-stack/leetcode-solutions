class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avgs=sum(nums[:k])
        m=avgs
        for i in range(k,len(nums)):
            avgs=avgs+nums[i]-nums[i-k]
            m=max(m,avgs) 
        return m/k       
        