
arr=[1,3,5,0,0,0]
# length=3
# capacity=6

for i in range(len(arr)):
    print(arr[i])
    
def insertend(arr,num,length,capacity):
    if length < capacity:
        arr[length] = num
        
# insertend(arr,999,3,6)
# print(arr)
    

    

def deleteend(arr,length):
    if length > 0:
        arr[length-1] = 0

# deleteend(arr,3)
# print(arr)

def insertany(arr,index,num,length):
    for i in range(length-1,index-1,-1):
        arr[i+1] = arr[i]
    arr[i] = num
        
# insertany(arr,0,1111,3)
# print(arr)

def deleteany(arr,index,length):
    for i in range(index+1,length):
        arr[i-1] = arr[i] 
        
deleteany(arr,1,3)
print(arr)