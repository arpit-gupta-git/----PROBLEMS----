class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = {0:-1}
        temp =0 
        for i in range(len(nums)):
            temp += nums[i]
            if temp % k  in prefix_sum:
                if i -  prefix_sum[temp%k] >= 2:
                    return True
            else:
                prefix_sum[temp%k] = i  
        return False
