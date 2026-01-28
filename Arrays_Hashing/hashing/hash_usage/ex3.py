hashmap = ["can" , "mike" , "chris" , "alice" , "can"]

hm = {}

for name in hashmap:
    if name not in hm:
        hm[name] = 1
        
    else:
        hm[name] += 1
        
print(hm)