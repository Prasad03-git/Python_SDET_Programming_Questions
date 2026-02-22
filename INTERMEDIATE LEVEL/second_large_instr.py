# Second Largest Digit in a String:
inp = "str1025rts"


def second_large(s):
    nums = []

    for i in s:
        if i.isdigit():
            nums.append(int(i))
    return (sorted(nums,reverse=True))[1]


res1 = second_large(inp)
print(res1)
