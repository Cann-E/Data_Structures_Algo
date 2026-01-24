myArr = [1,3,5,0,0]
# length = 3
# capacity = 5

for i in range(len(myArr)):
    print(myArr[i])
    
def deleteend(arr,length):
    if length > 0:
        arr[length-1] = 0
        
deleteend(myArr,3)
print(myArr)

def deleteany(arr,index,length):
    for i in range(index+1,length):
        arr[i-1] = i
        
deleteany(myArr,3,5)
print(myArr)

def insertend(arr,num,length,capacity):
    if length < capacity :
        arr[length+1] = num
        
insertend(myArr,999,3,5)
print(myArr)

def insertany(arr,index,num,length):
    for i in range(length-1,index-1,-1):
        arr[i+1] = arr[index]
        
    arr[index] = num
    
insertany(myArr,4,1111,3)
print(myArr)