def isPalindrome(x):
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]
