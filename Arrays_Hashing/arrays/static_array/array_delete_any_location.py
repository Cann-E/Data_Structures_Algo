myArr = [1,2,3,4]

def removemid(myArr,i,length):
    for index in range(i+1, length):
        myArr[index-1] = myArr[index]
    
removemid(myArr, 2, len(myArr))
print(myArr)