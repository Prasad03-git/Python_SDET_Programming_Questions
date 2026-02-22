#using set()
def remove_duplicate(data):
    return list(set(data))

#keeping order same
def remove_duplicate_(data):
    dupli=[]
    seen=[]
    for i in data:
        if i in seen:
            dupli.append(i)
        else:
            seen.append(i)
    return seen

data=[1,3,2,1,1]
res=remove_duplicate_(data)
print(res)
