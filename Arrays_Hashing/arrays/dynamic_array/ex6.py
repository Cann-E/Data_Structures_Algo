def resize(self):
    self.capacity = 2 * self.capacity
    newarr = [0] * self.capacity
    
    for i in range(self.length):
        newarr[i] = self.arr[i]
    self.arr = newarr 
    
def pushback(self,num):
    if self.capacicty == self.length:
        resize()
        
    self.arr[self.length] = num
    self.length +=1