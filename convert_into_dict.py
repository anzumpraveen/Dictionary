list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]

d=dict(zip(list1,list2))
print(d)

# second method
list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
d={list1[key]:list2[key]for key in range(len(list1))}
print(d)