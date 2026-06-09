class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        m=0
        while left<right:
            t=min(height[left],height[right])*(right-left)
            if t>m:
                m=t
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return m
        