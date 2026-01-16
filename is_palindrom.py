def is_palindrome(s):
    length = len(s)
    first_index = 0
    last_index = -1
    if length == 1:
        return True
    while first_index < (length//2):
        if s.lower()[first_index] == s.lower()[last_index]:
            first_index += 1
            last_index -= 1
            continue
        else:
            return False
    return True


is_palindrome("racecar")
is_palindrome("ABBA")
is_palindrome("a")