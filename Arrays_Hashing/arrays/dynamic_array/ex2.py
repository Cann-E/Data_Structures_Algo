def resize(self):
    self.capacity = 2*self.capacity
    newarr = [0] *self.capacity
    
    for i in range(self.length):
        self.arr[i] = newarr[i]
    self.arr = newarr

def pushback(self,n):
    if self.length == self.capacity:
        resize()
    self.arr[self.length] = n 
    self.length += 1