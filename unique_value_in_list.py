d=[ 
    {"first":"1"},
    {"second": "2"},
    {"third": "1"},
    {"four": "5"},
    {"five":"5"},
    {"six":"9"},
    {"seven":"7"}
    ]
print("The original list : " +  str(d)) 
res = list(set(val for dic in d for val in dic.values()))   
print("The unique values in list are : " + str(res)) 