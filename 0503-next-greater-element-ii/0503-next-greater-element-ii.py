class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        r=[]
        m=0
        a=nums+nums
        for i in range(len(nums)):
            b=nums[i]
            c=a[i+1:len(a)]
            for j in c:
                if j>b:
                    r.append(j)
                    break
            else:
                r.append(-1)
        return r