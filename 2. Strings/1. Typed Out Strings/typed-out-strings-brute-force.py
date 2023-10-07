def buildString(string: str):
    build_array = []
    for ch in string:
        if ch != "#":
            build_array.append(ch)
        else:
            build_array.pop()
    return build_array


def backSpaceCompare(s: str, t: str) -> bool:
    final_s = buildString(s)
    final_t = buildString(t)
    if len(final_s) != len(final_t):
        return False
    else:
        for i in range(final_s):
            if final_s[i] != final_t[i]:
                return False
    return True
