class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        string = ""
        seen  = set()
        repeated = set()
        for i in range(len(s)-9):
            string = s[i:i+10]
            if string in seen:
                repeated.add(string)
            else:
                seen.add(string)
        return list(repeated)
