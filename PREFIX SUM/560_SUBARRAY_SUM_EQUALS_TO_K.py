class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        need = {0:1}
        prefix_sum , count= 0,0 
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in need:
                count += need[prefix_sum-k]
            need[prefix_sum] = need.get(prefix_sum,0) + 1
        return count

        
