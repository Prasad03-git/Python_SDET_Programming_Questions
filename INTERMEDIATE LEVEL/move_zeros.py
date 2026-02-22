"""
Rearrange Array:
Given [2, 0, 4, 0, 3, 0, 5, 0],
 rearrange it so all even numbers come first and odd numbers last, 
 like [0,0,0,0,2,4,3,5]. (Since no explanation was given, I assumed this approach. 
 Another possible way could be moving all 0s to the left and non-zeros to the right.)

"""

lst = [2, 0, 4, 0, 3, 0, 5, 0]


def move_zeros(lst):
    new_lst = []
    for i in lst:
        if i == 0:
            new_lst.append(i)
    for i in lst:
        if i%2==0 and i not in new_lst:
            new_lst.append(i)
        elif i%2!=0 and i not in new_lst:
            new_lst.append(i)
    return new_lst


res = move_zeros(lst)
print(res)
