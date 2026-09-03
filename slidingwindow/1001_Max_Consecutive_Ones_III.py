class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l =0
        zero_freq = 0 
        count =0 
        for i in range(len(nums)):
            if nums[i] ==0 :
                zero_freq += 1
            while zero_freq > k :
                if nums[l] == 0:
                    zero_freq -= 1 
                l += 1 
            count = max(count, i-l+1)
        return count
