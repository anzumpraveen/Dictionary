a="MISSISSIPPI"
d={}
for i in a:
    c=0
    for j in a:
        if [i]==[j]:
            c+=1
        d[i]=c
print(d)