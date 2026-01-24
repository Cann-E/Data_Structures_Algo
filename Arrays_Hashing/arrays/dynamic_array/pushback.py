def pushback(self,n): #to add new element to the end of array
    if self.length == self.capacity:
        self.resize()
    
    self.arr[self.length] = n #Put the new value at the end of the array.
    self.length += 1