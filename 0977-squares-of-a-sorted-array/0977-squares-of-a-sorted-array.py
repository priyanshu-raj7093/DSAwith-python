class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        j=n-1
        k=n-1
        ans=[0]*n
        while i<=j:
            if abs(nums[i])>abs(nums[j]):
                ans[k]=nums[i]*nums[i]
                i+=1
            else:
                ans[k]=nums[j]*nums[j]
                j-=1
            k-=1
        return ans            
