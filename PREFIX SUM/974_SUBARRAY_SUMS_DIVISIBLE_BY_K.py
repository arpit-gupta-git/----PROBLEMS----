class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0 
        prefix_sum = {0:1}
        total =0 
        for i in range(len(nums)):
            total += nums[i]
            rem = total % k 
            if rem in prefix_sum :
                count += prefix_sum[rem] 
            prefix_sum[rem] = prefix_sum.get(rem,0) + 1
        return count        
