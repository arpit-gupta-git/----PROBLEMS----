class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        l = 0
        bestmatch = float('inf')
        beststart = -1 
        for i in t :
            need[i] = need.get(i,0) + 1
        requirements = len(need)  
        for i in range(len(s)):
            if s[i] in need:
                need[s[i]] -= 1 
                if need[s[i]] == 0:
                    requirements -= 1 
            while requirements ==0 :
                if i -l +1  < bestmatch :
                    bestmatch = i-l+1 
                    beststart  = l 
                if s[l] in need  :
                    need[s[l]] += 1
                    if need[s[l]] == 1 :
                        requirements += 1
                l +=1 
        return "" if beststart  == -1 else s[beststart:beststart+bestmatch]       
