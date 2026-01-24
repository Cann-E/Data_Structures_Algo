def resize(self):
    self.capacity = 2* self.capacity
    newArr = [0] *self.capacity #creating new array empty with zeroes [0,0,0,0]
    
    for i in range(self.length): #carrying over elements from opld array to new array
        newArr[i] = self.arr[i]
    self.arr = newArr