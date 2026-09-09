class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum , count = 0,0
        prefix_sum = {0:1}
        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum - k in prefix_sum :
                count += prefix_sum[running_sum - k] 
            prefix_sum[running_sum] = prefix_sum.get(running_sum,0) + 1 
        return count 
 # main logic        
# |---------s--------------|
# |----s - k ----|----k----|  
