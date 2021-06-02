fruit={}
def addone(index):
    if index in fruit:
        fruit[index]+=1
    else:
        fruit[index]=1
addone("apple")
addone("banana")
addone("Apple")
addone("apple")
print(len(fruit))
print(fruit)