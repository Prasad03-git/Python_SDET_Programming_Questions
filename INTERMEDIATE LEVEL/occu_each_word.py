# 2️⃣ Count Word Occurrences in a Sentence:
# Given a string like "my name is Rohan Rohan", the goal is to print each word along with how many times it appears.
# "Rohan" → 2 times
# Other words → 1 time each

sentence="my name is Rohan Rohan"
def occ_words(s):
    words=s.split(" ")
    freq={}
    for i in words:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq

res=occ_words(sentence)
print(res)