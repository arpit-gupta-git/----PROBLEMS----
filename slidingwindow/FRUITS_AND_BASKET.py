class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic  = {}
        l =0 
        fruitsum = float('-inf')
        for i in range(len(fruits)):
            dic[fruits[i]] = dic.get(fruits[i],0) + 1 
            while len(dic) > 2 :
                dic[fruits[l]] -= 1 
                if dic[fruits[l]] == 0 :
                    dic.pop(fruits[l]) 
                l += 1
            fruitsum = max(fruitsum,i-l+1)
        return fruitsum   


        

        
