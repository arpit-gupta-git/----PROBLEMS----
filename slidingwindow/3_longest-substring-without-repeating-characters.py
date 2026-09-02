class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 =set()
        size = 0 
        l,size=0,0 
        for i in range(len(s)):
            while s[i] in set1:
                set1.remove(s[l])
                l += 1 
            set1.add(s[i])
            size = max(size,i-l+1)
        return size
