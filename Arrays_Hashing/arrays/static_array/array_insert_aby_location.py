myArr = [1,2,3,0,0]
def insertMiddle(arr, i, n, length):

    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]
    

    arr[i] = n
    
insertMiddle(myArr,1,999,3)
print(myArr)