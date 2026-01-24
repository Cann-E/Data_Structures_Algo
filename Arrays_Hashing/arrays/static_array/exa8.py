arr=[1,2,3,0,0,0]
#length = 3
#capac = 6

for i in range(len(arr)):
    print(arr[i])
    
def deleteend(arr,length):
    if length > 0:
        arr[length-1] = 0
        
# deleteend(arr,3)
# print(arr)

def insertend(arr,num,length,capacity):
    if length < capacity:
        arr[length] = num
        
# insertend(arr,999,3,6)
# print(arr)

def deleteany(arr,index,lenght):
    for i in range(index+1,lenght):#starting from the elemnt after the one we want to delete to end
        arr[i-1] =  arr[i]  #mopve every element one position left

        
# deleteany(arr,0,3)
# print(arr)

def insertanmy(arr,index,num,length):
    for i in range(length-1,index-1,-1):
        arr[i+1] = arr[i]
        
    arr[i] = num
    
insertanmy(arr,0,9999,3)
print(arr)