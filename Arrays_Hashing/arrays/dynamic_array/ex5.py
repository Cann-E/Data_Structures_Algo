def resize(self):
    self.capacity = 2 * self.capacity
    newarr = [0] * self.capacity
    
    for i in range(self.length):
        self.newarr[i] = self.arr[i]
        
    self.arr = newarr

def pushback(self,num): #adds the new number at the end of the length
    if self.length == self.capatcity:
        resize()
    
    self.arr[self.length] = num
    self.length +=1