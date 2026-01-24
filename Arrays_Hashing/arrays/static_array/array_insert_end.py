myArr = [1,2,3,4,0,0,0]


def insertend(myArr, number, length, capacity):
    if length < capacity :
        myArr[length] = number
        
insertend(myArr,21,4,7)
print(myArr)