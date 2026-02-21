def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev


res = reverse_string("I Automate")
print(res)
