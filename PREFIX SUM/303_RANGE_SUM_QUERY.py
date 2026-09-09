class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        temp = 0 
        for i in nums:
            temp+= i 
            self.prefix_sum.append(temp)
    def sumRange(self, left: int, right: int) -> int:
        l = self.prefix_sum[left -1 ] if left > 0 else 0 
        r = self.prefix_sum[right] 
        return r-l
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
