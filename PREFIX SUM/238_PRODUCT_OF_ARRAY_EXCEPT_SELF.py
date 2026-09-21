class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_sum = []
        suffix_sum = []
        result = []
        n = len(nums)
        temp = 1
        for i in nums:
            temp *= i 
            prefix_sum.append(temp)
        temp =1
        for i in nums[-1::-1]:
            temp *= i 
            suffix_sum.append(temp) 
        suffix_sum = suffix_sum[-1::-1]
        result.append(suffix_sum[1])
        for i in range(1,len(nums)-1):
            result.append(prefix_sum[i-1] * suffix_sum[i+1])
        result.append(prefix_sum[n-2])
        return result 
        
