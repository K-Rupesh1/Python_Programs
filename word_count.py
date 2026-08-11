words=['apple','ant','bat','ball']
count=0
for word in words:
    for ch in word:
        if word.startswith('a'):
            count+=1
print(count)






