class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        size = 0
        l =0 
        maxfreq  = 0 
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i],0) + 1 
            maxfreq = max(maxfreq,dic[s[i]])
            while((i-l+1)-maxfreq> k ):
                dic[s[l]] = dic[s[l]] - 1 
                l +=1 
            size = max(i-l+1, size)
        return size 
        
