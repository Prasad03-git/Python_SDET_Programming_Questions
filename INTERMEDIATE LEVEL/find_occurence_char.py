#Write a program to count the occurrences of each character in a string.
s="testautomation"

def count_chars(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return freq

res = count_chars(s)
print(res)