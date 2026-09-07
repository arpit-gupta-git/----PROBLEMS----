def solution(s, k):
    l = 0
    size = 0
    dic = {}
    for i in range(len(s)):
        dic[s[i]] = dic.get(s[i], 0) + 1
        while len(dic) > k:
            dic[s[l]] = dic[s[l]] - 1
            if dic[s[l]] == 0:
                dic.pop(s[l])
            l += 1
        size = max(size, i - l + 1)
    return 0 if k==0 else size
