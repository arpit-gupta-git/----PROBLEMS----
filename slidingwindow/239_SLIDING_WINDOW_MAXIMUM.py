from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        q.append(float('-inf'))
        l=0
        for i in range(len(nums)):
            #leftmost : 0 
            # rightmost : -1
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            if i-l+1 == k :
                ans.append(q[0])
                if q[0] == nums[l]:
                    q.popleft()
                l+=1
        return ans 



                





            
        
