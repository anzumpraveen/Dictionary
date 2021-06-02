d={"one":"1","two":"2","three":"3"}
a={}
for key in d:
    newlist = {x for x in d}
    a[key]=newlist
print(a)