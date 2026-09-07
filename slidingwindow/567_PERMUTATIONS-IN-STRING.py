class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        need = {}
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1
        mismatches = len(need)
        l = 0 
        for r in range(len(s2)):
            need[s2[r]] = need.get(s2[r], 0) - 1
            if need[s2[r]] == 0:
                mismatches -= 1
            elif need[s2[r]] == -1:
                mismatches += 1
            if r - l + 1 == len(s1):
                if mismatches == 0:
                    return True
                need[s2[l]] += 1
                if need[s2[l]] == 0:
                    mismatches -= 1
                elif need[s2[l]] == 1:
                    mismatches += 1
                l += 1
        
        return False

        
