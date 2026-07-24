class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maximum=0
        while i<j:
            water=min(height[i],height[j])*(j-i)
            maximum=max(maximum,water)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maximum                
        