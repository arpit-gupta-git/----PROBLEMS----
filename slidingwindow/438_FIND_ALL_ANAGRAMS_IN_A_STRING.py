class Solution(object):
    def findAnagrams(self, s, p):
        result = []
        need = {}
        l=0
        for i in p :
            need[i] = need.get(i,0) +1
        mismatch = len(need)
        for j in range(len(s)):
            need[s[j]] = need.get(s[j],0) - 1
            if need[s[j]] == 0:
                mismatch  -= 1 
            if need[s[j]] == -1:
                mismatch += 1 
            if j-l+1 == len(p):
                if mismatch == 0 :
                    result.append(l)
                need[s[l]] += 1
                if need[s[l]] == 0:
                    mismatch -= 1 
                elif need[s[l]] == 1 :
                    mismatch += 1 
                l +=1
        return result


            
