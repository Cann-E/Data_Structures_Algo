

arr = [1,2,3,0,0]
#length=3
#capacity=5

for i in range(len(arr)):
    print(arr[i])
    
def deleteend(arr,length):
    if length > 0 :
        arr[length-1] = 0
        
# deleteend(arr,3)
# print(arr)

def insertend(arr,length,capacity,num):
    if length < capacity:
        arr[length] = num
        
# insertend(arr,3,5,999)
# print(arr)

def deleteany(arr,length,index):
    for i in range(index+1,length):
        arr[i-1] = arr[i]
    return length-1
        
# deleteany(arr,3,0)
# print(arr)

def insertany(arr,length,num,index):
    for i in range(length-1,index-1,-1):
        arr[i+1] = arr[i]
        
    arr[index] = num
    
insertany(arr,3,1111,0)
print(arr)
    