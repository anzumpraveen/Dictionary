d={1:"srishti",3:"megha",2:"anzum"}
a=[]
b=[]
for key in d:
    a.append(key)
    b.append(d[key])
    dic={}
    i=0
    while i<len(b):
        dic[b[i]]=a[i]
        i=i+1
print(dic)