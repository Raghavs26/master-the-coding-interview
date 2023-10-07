def valid_palindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i <= j:
        if s[i] == " " or not s[i].isalnum():
            i += 1
            continue
        elif s[j] == " " or not s[j].isalnum():
            j -= 1
            continue
        elif s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True
