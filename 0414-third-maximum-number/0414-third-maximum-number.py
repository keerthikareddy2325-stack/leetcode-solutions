class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        c=1
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                c+=1
                if c==3:
                    return nums[i+1]
        return nums[0]
