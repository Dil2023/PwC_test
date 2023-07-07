input = "babad"

def is_palindrome(s):
    return s == s[::-1]

def longest_palindromic_substring(s):
    s = s.lower()  # make the string case-insensitive
    max_length = 0
    start = 0

    # Check all substrings one by one
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j + 1]
            if is_palindrome(substr) and len(substr) > max_length:
                start = i
                max_length = len(substr)

    return s[start:start + max_length]

longest_palindromic_substring(input)