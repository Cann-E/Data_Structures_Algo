def rehash(self):
    self.capacity = 2 * self.capacity
    newHashmap = []
    
    for i in range(self.capacity):
        newHashmap.append(None)
        
    oldMap = self.map
    self.map = newHashmap
    self.size = 0
    
    for pair in oldMap:
        if pair:
            self.put(pair.key,pair.val)