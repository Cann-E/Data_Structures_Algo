
myArr = [1,3,5]

def removend(myArr,length):
    if length > 0 :
        myArr[length-1] = 0
        
removend(myArr,3)
print(myArr)
        