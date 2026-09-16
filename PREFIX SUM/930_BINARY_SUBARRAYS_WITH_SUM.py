class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = {0:1}
        count, total = 0 , 0  
        for i in range(len(nums)):
            total += nums[i]
            if total - goal in prefix_sum:
                count += prefix_sum[total - goal]
            prefix_sum[total] = prefix_sum.get(total,0) + 1 
        return count
