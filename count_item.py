d=  {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}
c=0
for i in d:
    for x  in d[i]:
        c+=1
print(c)