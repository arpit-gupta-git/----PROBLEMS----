class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total,l = 0,0
        size = float('inf') 
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                size = min(i-l +1,size)
                total -= nums[l]
                l += 1 
        return 0 if size==float('inf') else size 
