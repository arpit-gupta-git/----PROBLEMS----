from collections import deque
class Solution:
    def firstNegInt(self, arr, k):
        result = []
        q = deque()
        l =0 
        for i in range(len(arr)):
            if arr[i] < 0 :
                q.append(arr[i])
            if i - l + 1 == k :
                result.append(q[0]) if q else result.append(0)
                if arr[l] < 0 :
                    q.popleft()
                l += 1 
        return result
