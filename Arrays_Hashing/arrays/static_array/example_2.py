myArr = [1,3,4,6,0,0]
# length = 4
# capacity = 6

for i in range(len(myArr)):
    print(myArr[i])
    
def insertend(myArr,n,length,capacity):
    if length < capacity:
        myArr[length] = n
        
# insertend(myArr,99,4,6)
# print(myArr)
def insertany(myArr,index,num,length):
    for i in range(length-1,index-1,-1):
        myArr[i+1] = myArr[i]
    myArr[i] = num
    
insertany(myArr,1,99,4)
print(myArr)

def deletend(myArr,length):
    myArr[length-1] = 0
    
# deletend(myArr,4)
# print(myArr)

def deleteany(myArr,i,length):
    for index in range(i+1,length):#start from asked location until end of values
        myArr[index-1] = myArr[index]#move the index one left so its deleted 
        
# deleteany(myArr,2,4)
# print(myArr)


    
        