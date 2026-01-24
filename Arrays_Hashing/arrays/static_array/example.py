myArr = [1,3,4,0,0]
#length = how many slots filled in my array
#capacity = how big is my array

for i in range(len(myArr)): #1- traversing array
    print(myArr[i])
    
def insertend(myArr,num,length,capacity): #2- inserting end
    if length < capacity:
        myArr[length] = num
        
def insertanylocation(myArr,i,num,length): #3- insert any location
    for index in range(length-1,i-1,-1): #start from last number walk backwards -1 (length-1) and stop when you find given i location (i-1)
        myArr[index+1]= myArr[index] #move one stop right
        
    myArr[i] = num
    
def deletend(myArr,length): #4-delete from end
    if length > 0:
        myArr[length-1] = 0
        
def deleteany(myArr,i,length): #5-delete from any location
    for index in range(i+1, length):#start from asked location go till the end of the values thats inside array
        myArr[index-1] = myArr[index] #move one step left
    