def longest_substring(s: str) -> int:
    n = len(s)
    res = 0
    for i in range(n):
        mp = {}
        for j in range(i, n):
            if s[j] in mp:
                res = max(res, j - i)
                break
            else:
                mp[s[j]] = j
    return res


print(longest_substring("aabbcc"))
print(longest_substring("adbbcc"))


