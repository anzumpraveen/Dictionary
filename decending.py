d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
f={}
for i in d:
    for j in d:
        if d[i]>d[j]:
            swap=d[i]
            d[i]=d[j]
            d[j]=swap
print(d)