s = "madam"


#using string slicing method
def palindrome_check(s):
    return s == s[::-1]


def without_slicing(s):
    rev = ""
    for i in s:
        rev = i + rev
    return s == rev


res = without_slicing(s)
print(res)
