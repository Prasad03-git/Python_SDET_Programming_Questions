# How do you calculate the factorial of a number in Python?
#input num=5 fact=5x4x3x2x1 =120

num = 5


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)  #recursion method


#using loop
def facto(num):
    res = 1
    if num == 0:
        return res
    for i in range(1, num + 1):
        res = i * res

    return res
res = facto(0)
print(res)
