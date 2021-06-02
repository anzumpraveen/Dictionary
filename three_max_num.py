d= {'a':50,'b':58, 'c':56,'d':40,'e':100,'f':20}
max=d["a"]
max2=0
for i in d:
    c=0
    for j in d:
        if d[i]>d[j]:
            max=d[i]
            c+=1
        if c==3:
            key=i
            print(max,key)
            break

# max number
d={"a":21,"b":3,"s":1,"d":65}
max1=d["a"]
for value in d:
    if d[value]>=max1:
        max1=d[value]
        a=value
print(max1)    