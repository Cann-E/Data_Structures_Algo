hashmap = ["can","asli","lyndsey","murat","can"]

countmap = {}

for i in hashmap:
    if i not in countmap:
        countmap [i] = 1
    else:
        countmap [i] += 1
        
print(countmap)
        