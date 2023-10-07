def check_palindrome(s: str, start: int, end: int) -> bool:
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def validPalindrome(s: str) -> bool:
    start, end = 0, len(s) - 1
    while start <= end:
        if s[start] != s[end]:
            return check_palindrome(s, start + 1, end) or check_palindrome(
                s, start, end - 1
            )
        start += 1
        end -= 1
    return True
