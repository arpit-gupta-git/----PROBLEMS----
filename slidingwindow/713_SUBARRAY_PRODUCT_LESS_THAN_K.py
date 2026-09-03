class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<= 1:
            return 0 
        l =0 
        size = 0
        count  = 0
        prod = 1 
        for i in range(len(nums)):
            prod = prod * nums[i]
            size += 1 
            while prod >= k :
                prod /= nums[l]
                size -= 1 
                l+= 1
            count += size 
        return  count 

    
