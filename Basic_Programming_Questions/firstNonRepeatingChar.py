I="aabbcde"

def non_repeate(I):
    freq={}
    for i in I:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    for key,val in freq.items():
        if val==1:
            return key
re=non_repeate(I)
print(re)