arr=[1,3,5,0,0]

def deleteend(arr,length):
    if length > 0:
        arr[length-1] = 0
        
def insertend(arr,num,length,capacity):
    if length < capacity:
        arr[length] = num
        
def deleteany(arr,index,length):
    for i in range(index+1,length):
        arr[i+1] = arr[i]
        
def insertany(arr,index,num,length):
    for i in range(length-1,index-1,-1):
        arr[i+1] = arr[i]
    
    arr[i] = num