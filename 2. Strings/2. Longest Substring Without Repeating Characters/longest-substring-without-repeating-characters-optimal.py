# abcbdaac


def longest_substring(s: str) -> int:
    mp = {}
    start, res = 0, 0
    for end, val in enumerate(s):
        if val in mp:
            start = max(start, mp[val] + 1)
        res = max(res, end - start + 1)
        mp[val] = end
    return res
