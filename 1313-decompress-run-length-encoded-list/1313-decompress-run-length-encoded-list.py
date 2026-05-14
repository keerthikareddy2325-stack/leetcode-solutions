class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n%2==0:
            a=[]
            for i in range(0,n,2):
                freq=nums[i]
                val=nums[i+1]
                for j in range(freq):
                    a.append(val)
            return a


        