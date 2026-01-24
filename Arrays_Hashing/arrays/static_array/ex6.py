def deleteend(arr,length):
    if length > 0 :
        arr[length-1] = 0
        
def inserendt(arr,num,length,capacity):
    if length < capacity:
        arr[length] = num
        
def deleteany(arr,index,length):
    for i in range(i+1,length):
        arr[index-1] = arr[index]
        
def insetany(arr,num,index,length):
    for i in range(length-1,index-1,-1):
        arr[i+1] = arr[i]
    arr[i] = num