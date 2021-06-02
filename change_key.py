sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}
key=["name","age"]
for i in key:
    x={i:sampleDict[i]}
    print(x)

# second question
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sampleDict["location"]=sampleDict.pop("city")
print(sampleDict)